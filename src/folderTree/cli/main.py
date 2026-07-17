from pathlib import Path

from folderTree.exporters.markdown import MarkdownExporter
from folderTree.exporters.txt import TXTExporter
from folderTree.generators.documentation import DocumentationGenerator
from folderTree.scanner.scanner import ProjectScanner
from folderTree.cli.parser import create_parser


def main() -> None:
    """
    Entry point for the FolderTree CLI.
    """

    parser = create_parser()

    args = parser.parse_args()

    if args.command == "scan":
        scan(Path(args.path), args.output)


def scan(
    project_path: Path,
    output: str | None,
) -> None:
    """
    Scan a project and generate documentation.
    """
    scanner = ProjectScanner()

    project = scanner.scan(project_path)

    generator = DocumentationGenerator()

    documentation = generator.generate(project)

    if output is None:
        print(documentation)
        return

    output_path = Path(output)

    suffix = output_path.suffix.lower()

    if suffix == ".md":
        exporter = MarkdownExporter()

    elif suffix == ".txt":
        exporter = TXTExporter()

    else:
        raise ValueError(
            f"Unsupported output format: {suffix}"
        )

    exporter.export(
        documentation,
        output_path,
    )

    print("✓ Documentation generated successfully.")
    print(f"Output: {output_path}")

if __name__ == "__main__":
    main()