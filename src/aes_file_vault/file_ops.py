
from pathlib import Path
from typing import Optional

from .crypto import encrypt_data, decrypt_data


def _write_new_file(output_path: Path, data: bytes) -> None:
    """Create a new file without overwriting an existing file."""
    with output_path.open("xb") as file:
        file.write(data)


def encrypt_file(
    input_path: str,
    password: str,
    output_path: Optional[str] = None,
) -> Path:
    """Encrypt a file and save it as a new file."""
    source = Path(input_path).expanduser().resolve()

    if not source.is_file():
        raise FileNotFoundError(f"File tidak ditemukan: {source}")

    destination = (
        Path(output_path).expanduser().resolve()
        if output_path
        else Path(str(source) + ".enc")
    )

    if source == destination:
        raise ValueError("File keluaran tidak boleh sama dengan file sumber.")

    encrypted = encrypt_data(source.read_bytes(), password)
    _write_new_file(destination, encrypted)

    return destination


def decrypt_file(
    input_path: str,
    password: str,
    output_path: Optional[str] = None,
) -> Path:
    """Decrypt a file and save the recovered data."""
    source = Path(input_path).expanduser().resolve()

    if not source.is_file():
        raise FileNotFoundError(f"File tidak ditemukan: {source}")

    if output_path:
        destination = Path(output_path).expanduser().resolve()
    
    elif source.name.endswith(".enc"):
        original_name = source.name[:-4]
        original_path = Path(original_name)

        destination = source.with_name(
            f"{original_path.stem}.decrypted{original_path.suffix}"
        )

    else:
        destination = source.with_name(source.name + ".decrypted")

    if source == destination:
        raise ValueError("File keluaran tidak boleh sama dengan file sumber.")

    # Decryption and authentication finish before creating the output file.
    decrypted = decrypt_data(source.read_bytes(), password)
    _write_new_file(destination, decrypted)

    return destination
