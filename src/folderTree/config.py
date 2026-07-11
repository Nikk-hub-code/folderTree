from dataclasses import dataclass, field

from folderTree.utils.constants import DEFAULT_IGNORES


@dataclass(slots=True)
class Config:
    """
    Runtime configuration for FolderTree.
    """

    max_depth: int | None = None
    show_hidden: bool = False
    follow_symlinks: bool = False
    ignore_patterns: set[str] = field(
        default_factory=lambda: set(DEFAULT_IGNORES)
    )