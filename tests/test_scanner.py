from pathlib import Path

from folderTree.models import Project, Folder
from folderTree.scanner.scanner import ProjectScanner


SAMPLE_PROJECT = Path("sample_projects/python_project")


def test_scan_returns_project():
    """
    Scanner should return a Project object.
    """
    scanner = ProjectScanner()

    project = scanner.scan(SAMPLE_PROJECT)

    assert isinstance(project, Project)


def test_project_name():
    """
    Project name should match the root directory name.
    """
    scanner = ProjectScanner()

    project = scanner.scan(SAMPLE_PROJECT)

    assert project.name == SAMPLE_PROJECT.name


def test_root_folder():
    """
    Root folder should be a Folder object.
    """
    scanner = ProjectScanner()

    project = scanner.scan(SAMPLE_PROJECT)

    assert isinstance(project.root_folder, Folder)


def test_root_path():
    """
    Root path should match the scanned directory.
    """
    scanner = ProjectScanner()

    project = scanner.scan(SAMPLE_PROJECT)

    assert project.root_path == SAMPLE_PROJECT.resolve()


def test_root_contains_files_or_folders():
    """
    Root folder should contain at least one file or folder.
    """
    scanner = ProjectScanner()

    project = scanner.scan(SAMPLE_PROJECT)

    root = project.root_folder

    assert root.file_count > 0 or root.folder_count > 0


def test_invalid_path():
    """
    Scanning a non-existent directory should raise FileNotFoundError.
    """
    scanner = ProjectScanner()

    import pytest

    with pytest.raises(FileNotFoundError):
        scanner.scan("this_directory_does_not_exist")