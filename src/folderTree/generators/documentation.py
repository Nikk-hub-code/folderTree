from datetime import datetime

from folderTree.utils.formatter import Formatter
from folderTree.analyzers.languages import LanguageAnalyzer
from folderTree.analyzers.statistics import StatisticsAnalyzer
from folderTree.generators.tree import TreeGenerator
from folderTree.models import Project


class DocumentationGenerator:
    """
    Generates Markdown documentation for a project.
    """

    def __init__(self):
        self.tree_generator = TreeGenerator()
        self.statistics_analyzer = StatisticsAnalyzer()
        self.language_analyzer = LanguageAnalyzer()

    def generate(
        self,
        project: Project,
    ) -> str:
        """
        Generate complete project documentation.
        """
        return "\n\n".join(
            [
                "# Project Documentation",
                "",
                self._project_information(project),
                self._statistics_section(project),
                self._languages_section(project),
                self._tree_section(project),
            ]
        )

    def _project_information(
        self,
        project: Project,
    ) -> str:
        """
        Generate the project information section.
        """

        metadata = project.root_folder.metadata

        return (
            "## Project Information\n\n"
            f"- **Project Name:** {project.name}\n"
            f"- **Project Location:** {project.root_path.resolve()}\n"
            f"- **Project Created:** "
            f"{Formatter.format_datetime(metadata.created_at)}\n"
            f"- **Last Modified:** "
            f"{Formatter.format_datetime(metadata.modified_at)}\n"
            f"- **Documentation Generated:** "
            f"{Formatter.format_datetime(datetime.now())}\n"
        )

    def _statistics_section(
        self,
        project: Project,
    ) -> str:
        """
        Generate the statistics section.
        """

        statistics = self.statistics_analyzer.analyze(project)

        return (
            "## Statistics\n\n"
            f"- **Total Files:** {statistics.total_files}\n"
            f"- **Total Folders:** {statistics.total_folders}\n"
            f"- **Total Size:** {Formatter.format_bytes(statistics.total_size)}\n"
        )

    def _languages_section(
        self,
        project: Project,
    ) -> str:
        """
        Generate the languages section.
        """

        statistics = self.language_analyzer.analyze(project)

        lines = [
            "## Languages",
            "",
        ]

        for language, count in sorted(
            statistics.language_counts.items()
        ):
            lines.append(
                f"- **{language}:** {count}"
            )

        return "\n".join(lines)

    def _tree_section(
        self,
        project: Project,
    ) -> str:
        """
        Generate the folder tree section.
        """

        tree = self.tree_generator.generate(project)

        return (
            "## Folder Structure\n\n"
            "```text\n"
            f"{tree}\n"
            "```\n"
        )