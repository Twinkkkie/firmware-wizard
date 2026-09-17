from __future__ import annotations

import argparse
from .core import build_dry_run_command, load_manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Dry-run firmware deployment portfolio demo")
    parser.add_argument("manifest")
    parser.add_argument("--device", required=True)
    parser.add_argument("--port", default="COM-DEMO")
    args = parser.parse_args()
    packages = load_manifest(args.manifest)
    selected = next((p for p in packages if p.device == args.device), None)
    if selected is None:
        raise SystemExit(f"No firmware found for device: {args.device}")
    command = build_dry_run_command(selected, args.port)
    print("DRY RUN")
    print(" ".join(command))


if __name__ == "__main__":
    main()
