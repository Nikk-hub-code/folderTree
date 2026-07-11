"""
Application constants.
"""

APP_NAME = "FolderTree"
VERSION = "0.1.0"

TREE_BRANCH = "├── "
TREE_LAST_BRANCH = "└── "
TREE_PIPE = "│   "
TREE_SPACE = "    "

DEFAULT_IGNORES = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "node_modules",
    ".DS_Store",
}