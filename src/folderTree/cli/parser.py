from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    """
    Create and configure the FolderTree CLI parser.
    """

    parser = ArgumentParser(
        prog="folderTree",
        description="Generate project documentation.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a project directory.",
    )

    scan_parser.add_argument(
        "path",
        help="Path to the project directory.",
    )

    scan_parser.add_argument(
        "-o",
        "--output",
        help="Output file (.md or .txt).",
    )

    return parser