from pathlib import Path


class TXTExporter:
    """
    Exports text content to a .txt file.
    """

    def export(
        self,
        content: str,
        output_path: Path,
    ) -> None:
        """
        Write text content to the given file.
        """

        # Create parent directories if they don't exist
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Write the content to the file
        output_path.write_text(
            content,
            encoding="utf-8",
        )