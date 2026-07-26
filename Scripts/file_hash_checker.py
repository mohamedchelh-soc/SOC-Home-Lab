import hashlib
import sys
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python file_hash_checker.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File not found")
        sys.exit(1)

    file_hash = calculate_hash(file_path)

    print("File:", file_path)
    print("SHA256:", file_hash)
