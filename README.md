# Firmware Wizard

Desktop firmware management and deployment application developed as part of commercial software work at PassatInnovation.

> **Portfolio case study.** Proprietary firmware, bootloaders, device packs, credentials, internal endpoints, and company source code are intentionally excluded.

## What the application does

Firmware Wizard provides a desktop workflow for selecting firmware from a local source or cloud storage, preparing it for deployment, selecting a connected device/COM port, and launching the firmware flashing process through a SAM-BA-compatible workflow.

### Core capabilities

- Local and cloud firmware selection
- Cloud firmware discovery and download
- Access-token refresh flow for remote storage integration
- Encrypted firmware processing and decryption
- Serial/COM port detection and selection
- Firmware flashing orchestration
- Background download worker to keep the UI responsive
- Progress and error reporting
- Multi-language UI switching
- Unit-test coverage for core model/controller behavior

## Technology stack

- Python
- PyQt5
- Requests / HTTP APIs
- pyserial
- cryptography
- AES / PBKDF2-based firmware processing
- subprocess integration
- SAM-BA-compatible flashing workflow
- unittest / mocks
- Git

## My contribution

- Developed the Python desktop application and UI workflow
- Implemented cloud firmware retrieval and token refresh logic
- Implemented encrypted firmware processing
- Integrated serial device selection and external flashing tools
- Added asynchronous/background task handling and progress reporting
- Worked with embedded firmware artifacts and device programming workflows

## Security note

Credentials and tokens used by the historical internal application are not included. Production secrets should be stored outside source control using environment variables or a secrets manager.

## Public demo implementation

The `src/` folder contains a **clean-room, dry-run reimplementation** of the deployment workflow. It uses a local synthetic manifest and a fake firmware file, verifies SHA-256 integrity, and builds a SAM-BA-style command without flashing real hardware.

It intentionally does **not** include the original employer code, Dropbox credentials, production endpoints, encryption keys, firmware binaries, bootloaders, or vendor SDKs.

```bash
python -m pip install -e .
firmware-demo examples/manifest.json --device PiDemo --port COM7
python -m unittest discover -s tests -v
```
