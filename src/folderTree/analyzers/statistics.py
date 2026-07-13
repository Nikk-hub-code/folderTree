from __future__ import annotations

from dataclasses import dataclass, field

from folderTree.models import Folder, Project


@dataclass(slots=True)
class Statistics:
    """
    Stores statistics about a scanned project.
    """

    total_files: int = 0
    total_folders: int = 0
    total_size: int = 0

    extension_counts: dict[str, int] = field(default_factory=dict)


class StatisticsAnalyzer:
    """
    Analyzes a Project and generates statistics.
    """

    def analyze(self, project: Project) -> Statistics:
        """
        Analyze a project and return statistics.
        """

        statistics = Statistics()

        self._walk_folder(
            project.root_folder,
            statistics,
        )

        return statistics

    def _walk_folder(
        self,
        folder: Folder,
        statistics: Statistics,
    ) -> None:
        """
        Recursively walk through folders and collect statistics.
        """

        # Count the current folder
        statistics.total_folders += 1

        # Process files in the current folder
        for file in folder.files:

            statistics.total_files += 1

            statistics.total_size += file.size

            extension = file.extension.lower()

            statistics.extension_counts[extension] = (
                statistics.extension_counts.get(extension, 0) + 1
            )
        
        # Recursively process subfolders
        for subfolder in folder.folders:
            self._walk_folder(
                subfolder,
                statistics,
            )