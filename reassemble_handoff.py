#!/usr/bin/env python3
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "grok-handoff.zip": "24b61d5c582b1342637f41611c093bfcc7834b50e1117c6cd642f660c77fd9d4",
    "grok-handoff-images.zip": "6fd76ff535819bdf50aacccc1ccb0bf557a514e78ae830861ce059fc6c3f37c6",
}

for archive, expected_hash in EXPECTED.items():
    parts = sorted(ROOT.glob(archive + ".part-*"))
    if not parts:
        raise SystemExit(f"Missing parts for {archive}")
    output = ROOT / archive
    digest = hashlib.sha256()
    try:
        with output.open("wb") as dst:
            for part in parts:
                with part.open("rb") as src:
                    while block := src.read(1024 * 1024):
                        dst.write(block)
                        digest.update(block)
        actual = digest.hexdigest()
        if actual != expected_hash:
            raise ValueError(f"SHA-256 mismatch for {archive}: {actual}")
    except Exception:
        output.unlink(missing_ok=True)
        raise
    print(f"Verified {archive} from {len(parts)} parts: {actual}")
