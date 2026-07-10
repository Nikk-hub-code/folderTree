from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class File:
    """
    Represents a file in the scanned project.
    """

    name: str
    path: Path
    extension: str
    size: int
    created_at: datetime
    modified_at: datetime
    language: str | None = None

    @property
    def size_kb(self) -> float:
        return self.size / 1024

    @property
    def size_mb(self) -> float:
        return self.size / (1024 * 1024)