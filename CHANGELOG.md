# Changelog

All notable changes to this project will be documented in this file.

The format is based on Semantic Versioning.

---

## [0.1.0] - 2026-07-17

### Added

- Initial release of FolderTree CLI tool
- Scan project directories and analyze structure
- Recursive folder tree generation
- File metadata collection
- Project statistics analysis:
  - Total files
  - Total folders
  - Total size
  - File extension counts
- Programming language detection
- Automatic project documentation generation
- Terminal documentation preview
- Markdown documentation export
- TXT documentation export
- CLI interface with:
  - `folderTree scan .`
  - `folderTree scan . -o PROJECT.md`
  - `folderTree scan . -o PROJECT.txt`
- Configurable ignore handling
- Complete test suite covering core functionality