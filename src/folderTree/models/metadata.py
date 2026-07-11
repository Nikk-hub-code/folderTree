from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Metadata:
    """
    Filesystem metadata associated with a file or folder.
    """

    size: int
    created_at: datetime
    modified_at: datetime