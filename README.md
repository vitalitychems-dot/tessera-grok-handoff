# Screened Tessera/Grok handoff

This public repository contains the unique, reviewed Tessera/Grok handoff materials selected from the workspace. It is not a full Replit account or workspace export.

## Rebuild the archives

The GitHub connector rejected the archives as single uploads. They are stored as numbered 2 MiB parts. Download this repository with **Code → Download ZIP** or clone it, extract that repository ZIP, and run:

```bash
python3 reassemble_handoff.py
```

The script reconstructs both archives and verifies each SHA-256. Then extract `grok-handoff.zip` and `grok-handoff-images.zip` into the same folder so the PNG originals merge at their indexed paths.

- Main handoff files (excluding its manifest): 712
- PNG image originals: 132
- Main archive parts: 23
- Image companion parts: 30

## Compression and encryption

The archives use standard, lossless ZIP/Deflate compression at level 9. PNG and WebP assets are already compressed, so further lossless savings are limited; no image content was changed. The files are **not encrypted**: this is a public repository, and encryption would prevent readers from opening the handoff unless a private decryption key were distributed separately. SHA-256 checksums detect corruption but are not encryption.

## Privacy and rights boundary

Excluded: customer/user records, payment-card data, credentials, environment values, private runtime stores/logs/backups, private user-supplied share identifiers, unreviewed archive contents, duplicate files, and code/configuration/service paths that can access customer or transaction data. Storefront-integrated Tessera routes and private-data handling internals are omitted. The included simulation gateway is only a screened source excerpt; it relies on an injected Tessera-owned store, and production isolation is unverified.

The handoff does not establish that historical generated records are genuine conversations, that an external service is deployed, or that third-party sources are cleared for reuse. This repository grants no license to third-party code, text, images, models, or datasets.

## Archive SHA-256

- `grok-handoff.zip`: `24b61d5c582b1342637f41611c093bfcc7834b50e1117c6cd642f660c77fd9d4`
- `grok-handoff-images.zip`: `6fd76ff535819bdf50aacccc1ccb0bf557a514e78ae830861ce059fc6c3f37c6`
