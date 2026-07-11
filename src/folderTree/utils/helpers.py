from pathlib import Path


def validate_path(path: str | Path) -> Path:
    """
    Validate that a path exists and return it as a resolved Path object.
    """
    path = Path(path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    return path


def is_hidden(path: Path) -> bool:
    """
    Return True if the file or folder is hidden.
    """
    return path.name.startswith(".")


def get_extension(path: Path) -> str:
    """
    Return the file extension in lowercase.
    """
    return path.suffix.lower()


def format_size(size: int) -> str:
    """
    Convert bytes into a human-readable string.
    """
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024