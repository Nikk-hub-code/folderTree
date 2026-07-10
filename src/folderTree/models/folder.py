from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .file import File


@dataclass(slots=True)
class Folder:
    """
    Represents a folder in the scanned project.
    """

    name: str
    path: Path

    files: list[File] = field(default_factory=list)
    folders: list["Folder"] = field(default_factory=list)

    @property
    def file_count(self) -> int:
        return len(self.files)

    @property
    def folder_count(self) -> int:
        return len(self.folders)

    @property
    def total_size(self) -> int:
        size = sum(file.size for file in self.files)

        for folder in self.folders:
            size += folder.total_size

        return size