from pathlib import Path

from folderTree.exporters.markdown import MarkdownExporter


def test_export_creates_file(tmp_path):
    """
    Exporter should create a markdown file.
    """
    exporter = MarkdownExporter()

    output = tmp_path / "PROJECT_DOCUMENTATION.md"

    exporter.export(
        "# Hello",
        output,
    )

    assert output.exists()


def test_export_writes_content(tmp_path):
    """
    Exporter should write the provided content.
    """
    exporter = MarkdownExporter()

    output = tmp_path / "PROJECT_DOCUMENTATION.md"

    content = "# Project Documentation"

    exporter.export(
        content,
        output,
    )

    assert output.read_text(encoding="utf-8") == content


def test_export_creates_parent_directories(tmp_path):
    """
    Exporter should create missing parent directories.
    """
    exporter = MarkdownExporter()

    output = (
        tmp_path
        / "docs"
        / "generated"
        / "PROJECT_DOCUMENTATION.md"
    )

    exporter.export(
        "# Documentation",
        output,
    )

    assert output.exists()


def test_export_returns_output_path(tmp_path):
    """
    Exporter should return the output path.
    """
    exporter = MarkdownExporter()

    output = tmp_path / "PROJECT_DOCUMENTATION.md"

    returned = exporter.export(
        "# Documentation",
        output,
    )

    assert returned == output


def test_export_empty_string(tmp_path):
    """
    Exporter should support empty content.
    """
    exporter = MarkdownExporter()

    output = tmp_path / "PROJECT_DOCUMENTATION.md"

    exporter.export(
        "",
        output,
    )

    assert output.read_text(encoding="utf-8") == ""