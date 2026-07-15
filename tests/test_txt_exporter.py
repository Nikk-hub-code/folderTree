from pathlib import Path

from folderTree.exporters.txt import TXTExporter


def test_export_creates_file(tmp_path):
    """
    Exporter should create the output file.
    """
    exporter = TXTExporter()

    output_file = tmp_path / "tree.txt"

    exporter.export(
        content="Hello FolderTree",
        output_path=output_file,
    )

    assert output_file.exists()


def test_export_writes_content(tmp_path):
    """
    Exporter should write the correct content.
    """
    exporter = TXTExporter()

    output_file = tmp_path / "tree.txt"

    expected = """Project
├── src
└── tests
"""

    exporter.export(
        content=expected,
        output_path=output_file,
    )

    actual = output_file.read_text(
        encoding="utf-8",
    )

    assert actual == expected


def test_export_creates_parent_directories(tmp_path):
    """
    Exporter should automatically create parent directories.
    """
    exporter = TXTExporter()

    output_file = (
        tmp_path
        / "output"
        / "docs"
        / "tree.txt"
    )

    exporter.export(
        content="FolderTree",
        output_path=output_file,
    )

    assert output_file.exists()


def test_export_empty_string(tmp_path):
    """
    Exporting an empty string should create an empty file.
    """
    exporter = TXTExporter()

    output_file = tmp_path / "empty.txt"

    exporter.export(
        content="",
        output_path=output_file,
    )

    assert output_file.read_text(
        encoding="utf-8",
    ) == ""