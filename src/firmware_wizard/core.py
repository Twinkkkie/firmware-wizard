from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class FirmwarePackage:
    device: str
    version: str
    file: Path
    sha256: str


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(64 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: str | Path) -> list[FirmwarePackage]:
    manifest = Path(path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    return [
        FirmwarePackage(str(item["device"]), str(item["version"]), (manifest.parent / item["file"]).resolve(), str(item["sha256"]))
        for item in payload["firmware"]
    ]


def build_dry_run_command(package: FirmwarePackage, port: str, executable: str = "sam-ba") -> tuple[str, ...]:
    if not port.strip():
        raise ValueError("A serial port is required")
    if sha256_file(package.file).lower() != package.sha256.lower():
        raise ValueError("Firmware integrity check failed")
    return executable, "--port", port, "--firmware", str(package.file)
