# FolderTree

A CLI tool that automatically analyzes a project folder and generates clean project documentation.

FolderTree scans your project structure, collects metadata, analyzes statistics, detects programming languages, generates a folder tree, and creates documentation in Markdown or TXT format.

---

## Features

- 📁 Scan any project directory
- 🌳 Generate folder structure tree
- 📊 Analyze project statistics
- 💻 Detect programming languages
- 📝 Generate project documentation
- 📄 Export documentation as Markdown or TXT
- ⚡ Simple CLI interface

---

## Installation

Install using pip:

```bash
pip install folderTree
```

After installation, the `folderTree` command will be available globally.

---

## Usage

### View documentation in terminal

```bash
folderTree scan .
```

Example:

```bash
folderTree scan sample_projects/python_project
```

---

### Save documentation as Markdown

```bash
folderTree scan . -o PROJECT_DOCUMENTATION.md
```

---

### Save documentation as TXT

```bash
folderTree scan . -o PROJECT_DOCUMENTATION.txt
```

---

## Generated Documentation Example

FolderTree generates documentation containing:

```
# Project Documentation

## Project Information

- Project Name
- Project Location
- Project Created
- Last Modified
- Documentation Generated

## Statistics

- Total Files
- Total Folders
- Total Size

## Languages

- Python
- Markdown
- Text
- Other detected languages

## Folder Structure

project/
├── src/
│   ├── main.py
│   └── utils.py
└── README.md
```

---

## Project Structure

```
folderTree/
│
├── src/
│   └── folderTree/
│       ├── analyzers/
│       ├── cli/
│       ├── exporters/
│       ├── generators/
│       ├── models/
│       └── scanner/
│
├── tests/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
└── pyproject.toml
```

---

## Development

Clone the repository:

```bash
git clone <https://github.com/Nikk-hub-code/folderTree>
```

Install in editable mode:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

---

## License

This project is licensed under the MIT License.