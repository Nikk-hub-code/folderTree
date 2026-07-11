from pathlib import Path

from folderTree.config import Config


class IgnoreEngine:
    """
    Handles all ignore logic for files and directories.
    """

    def __init__(self, config: Config):
        self.config = config

    def should_ignore(self, path: Path) -> bool:
        """
        Return True if the given path should be skipped.
        """
        if not self.config.show_hidden and self.is_hidden(path):
            return True

        if path.name in self.config.ignore_patterns:
            return True

        return False

    @staticmethod
    def is_hidden(path: Path) -> bool:
        """
        Return True if the path is hidden.
        """
        return path.name.startswith(".")