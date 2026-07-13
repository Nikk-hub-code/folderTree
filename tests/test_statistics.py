from pathlib import Path

from folderTree.analyzers.statistics import Statistics, StatisticsAnalyzer
from folderTree.scanner.scanner import ProjectScanner


SAMPLE_PROJECT = Path("sample_projects/python_project")


def get_project():
    """
    Helper function to scan the sample project.
    """
    scanner = ProjectScanner()

    return scanner.scan(SAMPLE_PROJECT)


def test_analyzer_returns_statistics():
    """
    StatisticsAnalyzer should return a Statistics object.
    """
    project = get_project()

    analyzer = StatisticsAnalyzer()

    statistics = analyzer.analyze(project)

    assert isinstance(statistics, Statistics)


def test_total_files():
    """
    Total files should be counted correctly.
    """
    project = get_project()

    analyzer = StatisticsAnalyzer()

    statistics = analyzer.analyze(project)

    assert statistics.total_files == 6


def test_total_folders():
    """
    Total folders should be counted correctly.
    """
    project = get_project()

    analyzer = StatisticsAnalyzer()

    statistics = analyzer.analyze(project)

    assert statistics.total_folders == 3


def test_total_size():
    """
    Total project size should be non-negative.
    """
    project = get_project()

    analyzer = StatisticsAnalyzer()

    statistics = analyzer.analyze(project)

    assert statistics.total_size >= 0


def test_extension_counts():
    """
    File extensions should be counted correctly.
    """
    project = get_project()

    analyzer = StatisticsAnalyzer()

    statistics = analyzer.analyze(project)

    assert statistics.extension_counts[".py"] == 4
    assert statistics.extension_counts[".md"] == 1
    assert statistics.extension_counts[".txt"] == 1