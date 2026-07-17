from pathlib import Path

from folderTree.cli.main import scan


SAMPLE_PROJECT = Path(
    "sample_projects/python_project"
)


def test_scan_prints_documentation(capsys):
    """
    Scan without output should print documentation.
    """

    scan(
        SAMPLE_PROJECT,
        None,
    )

    captured = capsys.readouterr()

    assert "# Project Documentation" in captured.out


def test_scan_creates_markdown_file(tmp_path):
    """
    Scan with .md output should create markdown file.
    """

    output = tmp_path / "PROJECT.md"

    scan(
        SAMPLE_PROJECT,
        str(output),
    )

    assert output.exists()


def test_scan_creates_txt_file(tmp_path):
    """
    Scan with .txt output should create txt file.
    """

    output = tmp_path / "PROJECT.txt"

    scan(
        SAMPLE_PROJECT,
        str(output),
    )

    assert output.exists()


def test_scan_rejects_unknown_format(tmp_path):
    """
    Unsupported extensions should raise an error.
    """

    output = tmp_path / "PROJECT.pdf"

    try:
        scan(
            SAMPLE_PROJECT,
            str(output),
        )

    except ValueError as error:
        assert "Unsupported output format" in str(error)

    else:
        assert False