from pathlib import Path
from fnmatch import fnmatch

from folderTree.config import Config


class IgnoreEngine:
    """
    Handles all ignore logic for files and directories.
    """

    def __init__(self, config: Config):
        self.config = config

    def should_ignore(self, path: Path) -> bool:
        if not self.config.show_hidden and self.is_hidden(path):
            return True

        if self.matches_ignore_pattern(path):
            return True

        return False


    def matches_ignore_pattern(self, path: Path) -> bool:
        for pattern in self.config.ignore_patterns:
            if fnmatch(path.name, pattern):
                return True
        return False


    @staticmethod
    def is_hidden(path: Path) -> bool:
        """
        Return True if the path is hidden.
        """
        return path.name.startswith(".")