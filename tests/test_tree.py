from pathlib import Path

from folderTree.generators.tree import TreeGenerator
from folderTree.scanner.scanner import ProjectScanner


SAMPLE_PROJECT = Path("sample_projects/python_project")


def get_project():
    """
    Helper function to create a scanned project.
    """
    scanner = ProjectScanner()

    return scanner.scan(SAMPLE_PROJECT)


def test_tree_generator_returns_string():
    """
    TreeGenerator should return a string output.
    """
    project = get_project()

    generator = TreeGenerator()

    tree = generator.generate(project)

    assert isinstance(tree, str)


def test_tree_contains_project_name():
    """
    Generated tree should contain the project root name.
    """
    project = get_project()

    generator = TreeGenerator()

    tree = generator.generate(project)

    assert project.name in tree


def test_tree_contains_files():
    """
    Generated tree should contain scanned files.
    """
    project = get_project()

    generator = TreeGenerator()

    tree = generator.generate(project)

    assert "main.py" in tree
    assert "README.md" in tree


def test_tree_contains_folders():
    """
    Generated tree should contain folders.
    """
    project = get_project()

    generator = TreeGenerator()

    tree = generator.generate(project)

    assert "src/" in tree
    assert "tests/" in tree


def test_tree_contains_nested_files():
    """
    Nested files should appear in the generated tree.
    """
    project = get_project()

    generator = TreeGenerator()

    tree = generator.generate(project)

    assert "app.py" in tree
    assert "utils.py" in tree
    assert "test_app.py" in tree