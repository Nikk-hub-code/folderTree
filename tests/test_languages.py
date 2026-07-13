from pathlib import Path

from folderTree.analyzers.languages import (
    LanguageAnalyzer,
    LanguageStatistics,
)
from folderTree.scanner.scanner import ProjectScanner


SAMPLE_PROJECT = Path("sample_projects/python_project")


def get_project():
    """
    Helper function to scan the sample project.
    """
    scanner = ProjectScanner()

    return scanner.scan(SAMPLE_PROJECT)


def get_all_files(folder):
    """
    Recursively collect all files from a folder.
    """
    files = list(folder.files)

    for subfolder in folder.folders:
        files.extend(get_all_files(subfolder))

    return files


def test_analyzer_returns_language_statistics():
    """
    LanguageAnalyzer should return a LanguageStatistics object.
    """
    project = get_project()

    analyzer = LanguageAnalyzer()

    statistics = analyzer.analyze(project)

    assert isinstance(statistics, LanguageStatistics)


def test_language_counts():
    """
    Languages should be counted correctly.
    """
    project = get_project()

    analyzer = LanguageAnalyzer()

    statistics = analyzer.analyze(project)

    assert statistics.language_counts["Python"] == 4
    assert statistics.language_counts["Markdown"] == 1
    assert statistics.language_counts["Text"] == 1


def test_every_file_has_language():
    """
    Every scanned file should have its language assigned.
    """
    project = get_project()

    analyzer = LanguageAnalyzer()

    analyzer.analyze(project)

    files = get_all_files(project.root_folder)

    assert len(files) > 0

    for file in files:
        assert file.language is not None


def test_unknown_extension():
    """
    Unknown extensions should not cause failures.
    """
    project = get_project()

    analyzer = LanguageAnalyzer()

    statistics = analyzer.analyze(project)

    assert "Unknown" not in statistics.language_counts