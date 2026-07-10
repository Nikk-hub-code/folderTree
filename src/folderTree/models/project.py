from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from .folder import Folder


@dataclass(slots=True)
class Project:
    """
    Represents the scanned project.
    """

    name: str
    root_path: Path
    root_folder: Folder

    scanned_at: datetime = field(default_factory=datetime.now)