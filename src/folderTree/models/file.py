from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .metadata import Metadata


@dataclass(slots=True)
class File:
    """
    Represents a file in the scanned project.
    """

    name: str
    path: Path
    extension: str
    metadata: Metadata

    language: str | None = None

    @property
    def size(self) -> int:
        """
        Returns the file size in bytes.
        """
        return self.metadata.size

    @property
    def created_at(self) -> datetime:
        """
        Returns the file creation timestamp.
        """
        return self.metadata.created_at

    @property
    def modified_at(self) -> datetime:
        """
        Returns the file's last modification timestamp.
        """
        return self.metadata.modified_at

    @property
    def size_kb(self) -> float:
        """
        Returns the file size in kilobytes.
        """
        return self.size / 1024

    @property
    def size_mb(self) -> float:
        """
        Returns the file size in megabytes.
        """
        return self.size / (1024 * 1024)