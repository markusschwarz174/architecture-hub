"""Wiederverwendbares Begriffsskelett fuer einen lokalen Python-SCRIPT.

Template-Metadaten
------------------
status: TEMPLATE
version: 1.0.0
created_at: 2026-09-30
functional_area: TOOLING
canonical_file_type: SCRIPT
target_suffix: .py
authority: HUMAN_CONFIRMED_FILE_TYPE
local_authority: ARCHITECTURE_HUB_LIBRARY/_STANDARDS/NAMING_LOCAL.md#5-tooling
source_check: NAMING_LOCAL.md#provenienz-und-source-check-fuer-tooling

Vor Verwendung kopieren, aussagekraeftig benennen und alle TODO-Markierungen
ersetzen. Lokal bezeichnet SCRIPT ausschliesslich ein Python-Script. Andere
implementierende Dateien sind SOURCE CODE.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    """Validierte Eingaben des Scripts."""

    input_path: Path
    output_path: Path | None
    dry_run: bool


class ScriptError(RuntimeError):
    """Erwarteter fachlicher Fehler mit verstaendlicher Meldung."""


def build_parser() -> argparse.ArgumentParser:
    """Definiert die stabile Kommandozeilen-Schnittstelle."""

    parser = argparse.ArgumentParser(
        description="TODO: Zweck und beobachtbaren Effekt des Scripts angeben."
    )
    parser.add_argument("input_path", type=Path, help="TODO: erwarteten Input beschreiben")
    parser.add_argument("--output", dest="output_path", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan und Validierung zeigen, ohne eine Mutation auszufuehren.",
    )
    return parser


def validate_args(args: argparse.Namespace) -> Config:
    """Prueft Vorbedingungen vor jeder Wirkung."""

    input_path = args.input_path.resolve()
    if not input_path.exists():
        raise ScriptError(f"Input fehlt: {input_path}")

    output_path = args.output_path.resolve() if args.output_path else None
    return Config(input_path=input_path, output_path=output_path, dry_run=args.dry_run)


def execute(config: Config) -> str:
    """Fuehrt die kleinste deterministische Operation aus.

    TODO:
    - bestehende Quelle lesen;
    - Zielzustand berechnen;
    - bei dry_run nur den Plan liefern;
    - bei Wirkung atomar oder anderweitig recoverable schreiben;
    - Nachpruefung ausfuehren und Evidenz zurueckgeben.
    """

    raise ScriptError("TEMPLATE_NOT_IMPLEMENTED: execute() fachlich implementieren")


def main() -> int:
    """CLI-Einstieg mit explizitem Erfolgs- und Fehlercode."""

    try:
        config = validate_args(build_parser().parse_args())
        print(execute(config))
        return 0
    except ScriptError as exc:
        print(f"HOLD: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
