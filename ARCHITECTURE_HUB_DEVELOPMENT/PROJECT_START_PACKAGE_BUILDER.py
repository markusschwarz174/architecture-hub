#!/usr/bin/env python3
"""Build a PROJECT_START_PACKAGE from a confirmed profile and manifest.

The builder is deliberately deterministic: it copies declared files, applies
explicit replacements and records hashes. It does not make architecture
decisions and never modifies the Architecture Hub library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TEXT_SUFFIXES = {
    ".md", ".json", ".yaml", ".yml", ".py", ".txt", ".toml", ".html", ".css", ".js", ".ts"
}
PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_/-]{1,127}\]")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: str, field: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe {field}: {value!r}")
    return path


def within(root: Path, candidate: Path) -> Path:
    root = root.resolve()
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Path escapes root {root}: {resolved}") from exc
    return resolved


def write_atomic(path: Path, data: bytes, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise FileExistsError(f"Target already exists: {path}")
    temp = path.with_name(path.name + ".tmp")
    temp.write_bytes(data)
    temp.replace(path)


def apply_replacements(data: bytes, suffix: str, replacements: dict[str, str]) -> bytes:
    if not replacements:
        return data
    if suffix.lower() not in TEXT_SUFFIXES:
        raise ValueError("Replacements requested for a non-text file")
    text = data.decode("utf-8")
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text.encode("utf-8")


def validate_minimum(profile: dict[str, Any], manifest: dict[str, Any]) -> None:
    if profile.get("status") != "CONFIRMED":
        raise ValueError("PROJECT_PROFILE status must be CONFIRMED")
    if manifest.get("status") not in {"HUMAN_CONFIRMED", "BUILDABLE"}:
        raise ValueError("ASSEMBLY_MANIFEST status must be HUMAN_CONFIRMED or BUILDABLE")
    if profile.get("project_id") != manifest.get("project_id"):
        raise ValueError("project_id differs between profile and manifest")
    if not isinstance(manifest.get("files"), list) or not manifest["files"]:
        raise ValueError("Manifest files list is empty")


def build(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    profile_path = Path(args.profile).resolve()
    manifest_path = Path(args.manifest).resolve()
    roots = {
        "LIBRARY": Path(args.library_root).resolve(),
        "HUB_DEVELOPMENT": Path(args.hub_development_root).resolve(),
    }
    output_root = Path(args.output).resolve()

    profile = load_json(profile_path)
    manifest = load_json(manifest_path)
    validate_minimum(profile, manifest)

    if output_root.exists() and any(output_root.iterdir()) and not args.overwrite:
        raise FileExistsError(f"Output directory is not empty: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)

    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "project_id": profile["project_id"],
        "manifest_id": manifest.get("manifest_id"),
        "built_at": datetime.now(timezone.utc).isoformat(),
        "output_root": str(output_root),
        "status": "BUILT",
        "files": [],
        "missing_required": [],
        "missing_optional": [],
        "hash_mismatches": [],
        "unresolved_placeholders": [],
    }

    profile_bytes = profile_path.read_bytes()
    manifest_bytes = manifest_path.read_bytes()
    write_atomic(output_root / "PROJECT_PROFILE.json", profile_bytes, args.overwrite)
    write_atomic(output_root / "ASSEMBLY_MANIFEST.json", manifest_bytes, args.overwrite)

    seen_targets: set[str] = set()
    for item in manifest["files"]:
        source_root_name = item.get("source_root")
        if source_root_name not in roots:
            raise ValueError(f"Unknown source_root: {source_root_name!r}")
        source_rel = safe_relative(str(item.get("source", "")), "source")
        target_rel = safe_relative(str(item.get("target", "")), "target")
        target_key = target_rel.as_posix().lower()
        if target_key in seen_targets:
            raise ValueError(f"Duplicate target in manifest: {target_rel}")
        seen_targets.add(target_key)

        source_path = within(roots[source_root_name], roots[source_root_name] / source_rel)
        target_path = within(output_root, output_root / target_rel)
        required = bool(item.get("required"))

        if not source_path.is_file():
            bucket = "missing_required" if required else "missing_optional"
            report[bucket].append({"source": str(source_path), "target": target_rel.as_posix()})
            continue

        source_data = source_path.read_bytes()
        source_hash = sha256_bytes(source_data)
        declared_hash = item.get("source_sha256")
        if declared_hash and declared_hash.lower() != source_hash:
            report["hash_mismatches"].append({
                "source": str(source_path),
                "expected": declared_hash.lower(),
                "actual": source_hash,
            })
            if required:
                continue

        replacements = item.get("replacements") or {}
        if not isinstance(replacements, dict):
            raise ValueError(f"replacements must be an object for {target_rel}")
        target_data = apply_replacements(source_data, source_path.suffix, replacements)
        write_atomic(target_path, target_data, args.overwrite)

        placeholders: list[str] = []
        if target_path.suffix.lower() in TEXT_SUFFIXES:
            placeholders = sorted(set(PLACEHOLDER_RE.findall(target_data.decode("utf-8"))))
            for placeholder in placeholders:
                report["unresolved_placeholders"].append({
                    "file": target_rel.as_posix(), "placeholder": placeholder
                })

        report["files"].append({
            "source_root": source_root_name,
            "source": source_rel.as_posix(),
            "target": target_rel.as_posix(),
            "required": required,
            "source_sha256": source_hash,
            "target_sha256": sha256_bytes(target_data),
            "unresolved_placeholders": placeholders,
        })

    if report["missing_required"] or report["hash_mismatches"]:
        report["status"] = "FAIL"
    elif report["unresolved_placeholders"]:
        report["status"] = "BUILT_WITH_UNRESOLVED_PLACEHOLDERS"

    report_bytes = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    write_atomic(output_root / "PACKAGE_BUILD_REPORT.json", report_bytes, True)
    return report, 1 if report["status"] == "FAIL" else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Confirmed PROJECT_PROFILE.json")
    parser.add_argument("--manifest", required=True, help="Confirmed ASSEMBLY_MANIFEST.json")
    parser.add_argument("--library-root", required=True, help="ARCHITECTURE_HUB_LIBRARY path")
    parser.add_argument("--hub-development-root", required=True, help="ARCHITECTURE_HUB_DEVELOPMENT path")
    parser.add_argument("--output", required=True, help="Target PROJECT_START_PACKAGE directory")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite declared target files; never deletes extras")
    return parser.parse_args()


def main() -> int:
    try:
        report, code = build(parse_args())
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return code
    except Exception as exc:  # bounded CLI error reporting
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
