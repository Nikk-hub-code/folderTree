from pathlib import Path

from folderTree.config import Config
from folderTree.models import File, Folder, Project
from folderTree.scanner.ignore import IgnoreEngine
from folderTree.scanner.metadata_collector import MetadataCollector
from folderTree.utils.helpers import validate_path, get_extension


class ProjectScanner:
    """
    Scans a directory and builds a Project model.
    """

    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self.ignore_engine = IgnoreEngine(self.config)
        self.metadata_collector = MetadataCollector()

    def scan(self, path: str | Path) -> Project:
        """
        Scan the given project directory.
        """
        root_path = validate_path(path)

        if not root_path.is_dir():
            raise NotADirectoryError(f"{root_path} is not a directory.")

        root_folder = self._scan_folder(root_path)

        return Project(
            name=root_path.name,
            root_path=root_path,
            root_folder=root_folder,
        )

    def _scan_folder(self, path: Path, depth: int = 0) -> Folder:
        """
        Recursively scan a folder and return a Folder model.
        """

        # Stop recursion if max depth is reached
        if (
            self.config.max_depth is not None
            and depth > self.config.max_depth
        ):
            metadata = self.metadata_collector.collect(path)

            return Folder(
                name=path.name,
                path=path,
                metadata=metadata,
            )

        metadata = self.metadata_collector.collect(path)

        folder = Folder(
            name=path.name,
            path=path,
            metadata=metadata,
        )

        try:
            entries = sorted(
                path.iterdir(),
                key=lambda entry: (entry.is_file(), entry.name.lower())
            )
        except (PermissionError, FileNotFoundError, OSError):
            return folder

        for entry in entries:

            if self.ignore_engine.should_ignore(entry):
                continue

            if entry.is_dir():

                try:
                    subfolder = self._scan_folder(
                        entry,
                        depth + 1,
                    )

                    folder.folders.append(subfolder)
                except (PermissionError, FileNotFoundError, OSError):
                    continue

            elif entry.is_file():
                
                try:
                    file = self._create_file(entry)

                    folder.files.append(file)
                except (PermissionError, FileNotFoundError, OSError):
                    continue

        return folder

    def _create_file(self, path: Path) -> File:
        """
        Create a File model from a filesystem path.
        """
        metadata = self.metadata_collector.collect(path)

        return File(
            name = path.name,
            path = path,
            extension = get_extension(path),
            metadata = metadata,
            language = None
        )