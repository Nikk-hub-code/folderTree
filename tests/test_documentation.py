from pathlib import Path

from folderTree.generators.documentation import DocumentationGenerator
from folderTree.scanner.scanner import ProjectScanner


SAMPLE_PROJECT = Path("sample_projects/python_project")


def get_documentation() -> str:
    """
    Generate documentation for the sample project.
    """
    scanner = ProjectScanner()
    project = scanner.scan(SAMPLE_PROJECT)

    generator = DocumentationGenerator()

    return generator.generate(project)


def test_generator_returns_string():
    """
    Documentation generator should return a string.
    """
    documentation = get_documentation()

    assert isinstance(documentation, str)


def test_contains_title():
    """
    Documentation should contain the main title.
    """
    documentation = get_documentation()

    assert "# Project Documentation" in documentation


def test_contains_project_information():
    """
    Documentation should contain the project information section.
    """
    documentation = get_documentation()

    assert "## Project Information" in documentation
    assert "python_project" in documentation


def test_contains_statistics():
    """
    Documentation should contain the statistics section.
    """
    documentation = get_documentation()

    assert "## Statistics" in documentation
    assert "Total Files" in documentation
    assert "Total Folders" in documentation
    assert "Total Size" in documentation


def test_contains_languages():
    """
    Documentation should contain the languages section.
    """
    documentation = get_documentation()

    assert "## Languages" in documentation
    assert "Python" in documentation


def test_contains_tree():
    """
    Documentation should contain the folder tree.
    """
    documentation = get_documentation()

    assert "## Folder Structure" in documentation
    assert "```text" in documentation
    assert "src/" in documentation