from pathlib import Path


class MarkdownExporter:
    """
    Exports documentation as a Markdown file.
    """

    def export(
        self,
        content: str,
        output_path: Path,
    ) -> Path:
        """
        Write Markdown content to a file.
        """
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            content,
            encoding="utf-8",
        )

        return output_path