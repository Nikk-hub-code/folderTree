from folderTree.cli.parser import create_parser


def test_scan_command():
    """
    Parser should accept the scan command.
    """
    parser = create_parser()

    args = parser.parse_args([
        "scan",
        ".",
    ])

    assert args.command == "scan"
    assert args.path == "."
    assert args.output is None


def test_scan_with_output():
    """
    Parser should accept an output file.
    """
    parser = create_parser()

    args = parser.parse_args([
        "scan",
        ".",
        "-o",
        "PROJECT.md",
    ])

    assert args.command == "scan"
    assert args.path == "."
    assert args.output == "PROJECT.md"


def test_scan_with_txt_output():
    """
    Parser should accept a txt output file.
    """
    parser = create_parser()

    args = parser.parse_args([
        "scan",
        ".",
        "--output",
        "PROJECT.txt",
    ])

    assert args.command == "scan"
    assert args.path == "."
    assert args.output == "PROJECT.txt"