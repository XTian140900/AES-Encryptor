# AES File Vault

A local command-line application for file encryption and decryption using AES-256-GCM.

## Features

- Encrypt files using AES-256-GCM.
- Decrypt files using the correct password.
- Derive encryption keys from passwords using Scrypt.
- Detect incorrect passwords and modified encrypted data.
- Preserve original files during encryption.
- Prevent accidental overwriting of existing output files.
- Process files locally without uploading them to a server.

## Requirements

- Python 3.10 or newer
- pip
- Git (optional, for cloning the repository)

## Installation

Clone the repository:

```bash
git clone https://github.com/XTian140900/AES-Encryptor.git
cd AES-Encryptor
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the application:

```bash
python -m pip install .
```

## Usage

Start the application:

```bash
aes-file-vault
```

The interactive menu provides three options:

- `1` — Encrypt a file
- `2` — Decrypt a file
- `0` — Exit

Follow the prompts to enter the file path and password.

By default, encrypted files are saved with the `.enc` suffix. Decrypted files are saved with a `.decrypted` suffix in the filename.

## Security Notes

- Keep your passwords secure. Lost passwords cannot be recovered by this application.
- Encrypted files should be tested through decryption before the original files are deleted.
- File processing currently loads the entire file into memory, so very large files may require substantial RAM.
- This project is an educational prototype and has not undergone an independent security audit.
- Local processing avoids uploading files to a server, but does not protect against malware or unauthorized access to the computer.

## Development and Tests

Install the project and its dependencies, then run:

```bash
python -m unittest discover -s tests -v
```

## License

See the `LICENSE` file for licensing terms.