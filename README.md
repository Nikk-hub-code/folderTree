# FolderTree

A lightweight command-line tool that automatically analyzes a project directory and generates clean, well-structured project documentation.

FolderTree scans your project, collects metadata, analyzes project statistics, detects programming languages, generates a folder tree, and exports documentation in Markdown or TXT format.

---

## Features

- 📁 Scan any project directory
- 🌳 Generate a beautiful folder tree
- 📊 Analyze project statistics
- 💻 Detect programming languages
- 📝 Generate project documentation
- 📄 Export documentation as Markdown or TXT
- ⚡ Fast and simple CLI interface

---

## Requirements

- Python **3.11** or later

---

## Installation

```bash
pip install folderTree-cli
```

After installation, the `folderTree` command will be available globally.

---

## Usage

### Show available commands

```bash
folderTree --help
```

---

### Generate documentation in the terminal

```bash
folderTree scan .
```

or

```bash
folderTree scan path/to/project
```

Example

```bash
folderTree scan sample_projects/python_project
```

---

### Export as Markdown

```bash
folderTree scan . -o PROJECT_DOCUMENTATION.md
```

---

### Export as TXT

```bash
folderTree scan . -o PROJECT_DOCUMENTATION.txt
```

---

## Example Output

```text
# Project Documentation

## Project Information

- Project Name: folderTree
- Project Location: D:\Projects\folderTree
- Project Created: 2026-07-10
- Documentation Generated: 2026-07-19

## Statistics

- Total Files: 59
- Total Folders: 22
- Total Size: 41.94 KB

## Languages

- Python: 47
- Markdown: 4
- TOML: 1
- HTML: 1
- CSS: 1
- JavaScript: 1

## Folder Structure

folderTree/
├── src/
│   └── folderTree/
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

---

## Project Structure

```text
folderTree/
│
├── src/
│   └── folderTree/
│       ├── analyzers/
│       ├── cli/
│       ├── exporters/
│       ├── generators/
│       ├── models/
│       ├── scanner/
│       └── utils/
│
├── tests/
├── docs/
├── README.md
├── LICENSE
├── CHANGELOG.md
└── pyproject.toml
```

---

## Development

Clone the repository:

```bash
git clone https://github.com/Nikk-hub-code/folderTree.git
```

Move into the project directory:

```bash
cd folderTree
```

Install in editable mode:

```bash
pip install -e .
```

Run the test suite:

```bash
pytest
```

---

## License

This project is licensed under the MIT License.