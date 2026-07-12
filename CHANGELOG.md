# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**,
and this project follows **Semantic Versioning (SemVer)**.

## [Unreleased]

### Added
- Project structure following the `src` layout.
- Core data models (`Project`, `Folder`, `File`, `Metadata`).
- Configuration system.
- Helper utilities.
- Ignore engine for hidden files and ignore patterns.
- Metadata collector for filesystem information.
- Recursive project scanner.
- Initial scanner test suite.

### Changed
- Refactored metadata into a dedicated `Metadata` model.
- Updated `File` and `Folder` models to use shared metadata.

### Fixed
- Corrected scanner recursion and folder creation.
- Added proper package configuration using `pyproject.toml`.

---

## [0.1.0] - 2026-07-12

### Added
- Initial project setup.