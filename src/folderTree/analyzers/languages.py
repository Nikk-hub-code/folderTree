from __future__ import annotations

from dataclasses import dataclass, field

from folderTree.models import Folder, Project
from folderTree.utils.constants import EXTENSION_TO_LANGUAGE


@dataclass(slots=True)
class LanguageStatistics:
    """
    Stores language statistics for a project.
    """

    language_counts: dict[str, int] = field(default_factory=dict)


class LanguageAnalyzer:
    """
    Analyzes programming languages used in a project.
    """

    def analyze(self, project: Project) -> LanguageStatistics:
        """
        Analyze the project and return language statistics.
        """

        statistics = LanguageStatistics()

        self._walk_folder(
            project.root_folder,
            statistics,
        )

        return statistics

    def _walk_folder(
        self,
        folder: Folder,
        statistics: LanguageStatistics,
    ) -> None:
        """
        Recursively walk through folders.
        """
        # Process files in the current folder
        for file in folder.files:

            language = EXTENSION_TO_LANGUAGE.get(
                file.extension.lower(),
                "Unknown",
            )

            file.language = language

            statistics.language_counts[language] = (
                statistics.language_counts.get(language, 0) + 1
            )

        # Recursively process subfolders
        for subfolder in folder.folders:

            self._walk_folder(
                subfolder,
                statistics,
            )