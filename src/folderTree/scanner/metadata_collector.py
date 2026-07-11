from datetime import datetime
from pathlib import Path

from folderTree.models import Metadata


class MetadataCollector:
    """
    Collects metadata from filesystem paths.
    """

    @staticmethod
    def collect(path: Path) -> Metadata:
        stats = path.stat()

        return Metadata(
            size=stats.st_size,
            created_at=datetime.fromtimestamp(stats.st_ctime),
            modified_at=datetime.fromtimestamp(stats.st_mtime),
        )