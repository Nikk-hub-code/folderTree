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
    "env",
    "test_env",
    "build",
    "dist",
    "*.egg-info",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "node_modules",
    ".DS_Store",
}

EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",

    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",

    ".json": "JSON",
    ".xml": "XML",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".ini": "INI",

    ".md": "Markdown",
    ".txt": "Text",

    ".sh": "Shell",
    ".bat": "Batch",
    ".ps1": "PowerShell",

    ".sql": "SQL",

    ".dockerfile": "Docker",
    ".env": "Environment",
}