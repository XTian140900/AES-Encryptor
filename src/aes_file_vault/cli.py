
from getpass import getpass

from .file_ops import encrypt_file, decrypt_file


APP_NAME = "AES File Vault"
VERSION = "0.1.0"


def show_menu() -> None:
    print(f"\n{'=' * 38}")
    print(f"  {APP_NAME} v{VERSION}")
    print("  Local File Encryption Tool")
    print(f"{'=' * 38}")
    print("  [1] Encrypt a file")
    print("  [2] Decrypt a file")
    print("  [0] Exit")
    print(f"{'=' * 38}")


def ask_file_path() -> str:
    return input("File path: ").strip().strip('"').strip("'")


def ask_output_path() -> str:
    return input(
        "Output path (Enter for default): "
    ).strip().strip('"').strip("'")


def handle_encrypt() -> None:
    source = ask_file_path()

    if not source:
        print("Path file required.")
        return

    password = getpass("Password: ")
    confirmation = getpass("Confirm password: ")

    if not password:
        print("Passwod required.")
        return

    if password != confirmation:
        print("Password not match.")
        return

    output = ask_output_path()

    result = encrypt_file(
        source,
        password,
        output or None,
    )

    print(f"\nEncrytion success: {result}")


def handle_decrypt() -> None:
    source = ask_file_path()

    if not source:
        print("Path file required.")
        return

    password = getpass("Password: ")

    if not password:
        print("Password required.")
        return

    output = ask_output_path()

    result = decrypt_file(
        source,
        password,
        output or None,
    )

    print(f"\nDecrytion success: {result}")


def main() -> None:
    while True:
        show_menu()
        choice = input("Menu: ").strip()

        try:
            if choice == "1":
                handle_encrypt()
            elif choice == "2":
                handle_decrypt()
            elif choice == "0":
                print("Bye.")
                break
            else:
                print("Not valid.")

        except (ValueError, FileNotFoundError, FileExistsError, OSError) as exc:
            print(f"\nOperation error: {exc}")

        input("\nPress Enter to back...")


if __name__ == "__main__":
    main()
