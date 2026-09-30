#!/usr/bin/env python3
"""Read-only structural validator for a PROJECT_START_PACKAGE."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_/-]{1,127}\]")
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt", ".toml", ".html", ".css", ".js", ".ts"}
CORE_FILES = {
    "PROJECT_PROFILE.json",
    "ASSEMBLY_MANIFEST.json",
    "PACKAGE_BUILD_REPORT.json",
    "HANDOVER.md",
    "STARTPROMPT_PROJECT.md",
    "AGENT_PROJECT_ARCHITEKT.md",
}
PLACEHOLDER_SCAN_EXCLUDE = {
    "PROJECT_PROFILE.json",
    "ASSEMBLY_MANIFEST.json",
    "PACKAGE_BUILD_REPORT.json",
}
MANIFESTED_CORE_TARGETS = {
    "HANDOVER.md",
    "STARTPROMPT_PROJECT.md",
    "AGENT_PROJECT_ARCHITEKT.md",
}
MINIMUM_REQUIRED_TARGETS = {
    "MISSION.md",
    "PROJECT_BUILD_RECORD.md",
    "DEVELOPMENT_LOG.json",
    "PINWALL.md",
}
MINIMUM_CONCEPT_TARGETS = {"PROJECT_CONCEPT.md", "PROJECT_ARCHITECTURE.md"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe manifest target: {value!r}")
    return path


def validate(package_root: Path) -> dict[str, Any]:
    package_root = package_root.resolve()
    profile = load_json(package_root / "PROJECT_PROFILE.json")
    manifest = load_json(package_root / "ASSEMBLY_MANIFEST.json")
    build_report = load_json(package_root / "PACKAGE_BUILD_REPORT.json")

    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "package_root": str(package_root),
        "project_id": profile.get("project_id"),
        "manifest_id": manifest.get("manifest_id"),
        "missing": [],
        "unexpected": [],
        "modified": [],
        "unresolved": [],
        "stringency_findings": [],
        "verdict": "PASS",
    }

    if profile.get("project_id") != manifest.get("project_id"):
        report["stringency_findings"].append("project_id differs between profile and manifest")
    if build_report.get("manifest_id") != manifest.get("manifest_id"):
        report["stringency_findings"].append("manifest_id differs between manifest and build report")
    if profile.get("status") != "CONFIRMED":
        report["unresolved"].append("PROJECT_PROFILE is not CONFIRMED")

    expected = set(CORE_FILES)
    targets_lower: set[str] = set()
    manifest_by_target: dict[str, dict[str, Any]] = {}
    for item in manifest.get("files", []):
        target = safe_relative(str(item.get("target", ""))).as_posix()
        lower = target.lower()
        if lower in targets_lower:
            report["stringency_findings"].append(f"Duplicate manifest target: {target}")
        targets_lower.add(lower)
        manifest_by_target[target] = item
        expected.add(target)
        target_path = package_root / Path(target)
        if item.get("required") and not target_path.is_file():
            report["missing"].append(target)

    for target in sorted(MANIFESTED_CORE_TARGETS | MINIMUM_REQUIRED_TARGETS):
        item = manifest_by_target.get(target)
        if item is None:
            report["stringency_findings"].append(f"Required target is not declared in manifest: {target}")
        elif not item.get("required"):
            report["stringency_findings"].append(f"Required target is optional in manifest: {target}")

    concept_targets = MINIMUM_CONCEPT_TARGETS & set(manifest_by_target)
    if not concept_targets:
        report["stringency_findings"].append(
            "Manifest must declare PROJECT_CONCEPT.md or PROJECT_ARCHITECTURE.md"
        )
    elif not any(manifest_by_target[target].get("required") for target in concept_targets):
        report["stringency_findings"].append(
            "PROJECT_CONCEPT.md or PROJECT_ARCHITECTURE.md must be required"
        )

    if manifest.get("profile_ref") != "PROJECT_PROFILE.json":
        report["stringency_findings"].append("profile_ref must bind PROJECT_PROFILE.json")
    next_agent = manifest.get("next_agent") or {}
    if next_agent.get("agent_file") != "AGENT_PROJECT_ARCHITEKT.md":
        report["stringency_findings"].append("next_agent.agent_file is not AGENT_PROJECT_ARCHITEKT.md")
    if next_agent.get("startprompt") != "STARTPROMPT_PROJECT.md":
        report["stringency_findings"].append("next_agent.startprompt is not STARTPROMPT_PROJECT.md")
    if next_agent.get("expected_takeover_state") != "TAKEOVER_ACCEPTED":
        report["stringency_findings"].append("next_agent takeover state is not TAKEOVER_ACCEPTED")
    validation = manifest.get("validation") or {}
    for flag in ("stringency_required", "diff_required", "external_session_required"):
        if validation.get(flag) is not True:
            report["stringency_findings"].append(f"Manifest validation flag is not true: {flag}")

    for core in sorted(CORE_FILES):
        if not (package_root / core).is_file():
            report["missing"].append(core)

    actual = {
        path.relative_to(package_root).as_posix()
        for path in package_root.rglob("*")
        if path.is_file()
    }
    report["unexpected"] = sorted(actual - expected)

    built_by_target = {
        str(item.get("target")): item
        for item in build_report.get("files", [])
        if isinstance(item, dict) and item.get("target")
    }
    for target, item in manifest_by_target.items():
        built = built_by_target.get(target)
        if item.get("required") and built is None:
            report["stringency_findings"].append(f"Required manifest target absent from build report: {target}")
        elif built is not None:
            for field in ("source_root", "source", "required"):
                if built.get(field) != item.get(field):
                    report["stringency_findings"].append(
                        f"Build report differs from manifest for {target}: {field}"
                    )

    if build_report.get("status") != "BUILT":
        report["unresolved"].append({"build_status": build_report.get("status")})
    for finding in build_report.get("missing_optional", []):
        report["unresolved"].append({"missing_optional": finding})
    for finding in build_report.get("unresolved_placeholders", []):
        report["unresolved"].append({"build_placeholder": finding})
    for target in sorted(expected - CORE_FILES):
        path = package_root / Path(target)
        built = built_by_target.get(target)
        if path.is_file() and built and built.get("target_sha256"):
            actual_hash = hash_file(path)
            if actual_hash != built["target_sha256"]:
                report["modified"].append({
                    "file": target,
                    "built_sha256": built["target_sha256"],
                    "actual_sha256": actual_hash,
                })

    for rel in sorted(actual):
        if rel in PLACEHOLDER_SCAN_EXCLUDE:
            continue
        path = package_root / Path(rel)
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for placeholder in sorted(set(PLACEHOLDER_RE.findall(text))):
            report["unresolved"].append({"file": rel, "placeholder": placeholder})

    accepted_gaps = set((manifest.get("validation") or {}).get("accepted_gaps") or [])
    for decision in manifest.get("selection_decisions", []):
        if decision.get("decision") == "GAP" and decision.get("subject") not in accepted_gaps:
            report["unresolved"].append({
                "gap": decision.get("subject"),
                "reason": decision.get("reason"),
            })
    for decision in profile.get("open_decisions", []):
        report["unresolved"].append({"open_decision": decision})

    report["missing"] = sorted(set(report["missing"]))
    if report["missing"] or report["modified"] or report["stringency_findings"]:
        report["verdict"] = "FAIL"
    elif report["unresolved"]:
        report["verdict"] = "HOLD"
    elif report["unexpected"]:
        report["verdict"] = "PASS_WITH_WARNINGS"
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True, help="PROJECT_START_PACKAGE directory")
    parser.add_argument("--report", help="Optional output path outside the package")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = validate(Path(args.package))
        payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.report:
            Path(args.report).write_text(payload, encoding="utf-8")
        print(payload, end="")
        return 0 if report["verdict"] in {"PASS", "PASS_WITH_WARNINGS"} else 1
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
