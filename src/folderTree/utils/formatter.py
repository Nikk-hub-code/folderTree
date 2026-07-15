from __future__ import annotations

from datetime import datetime


class Formatter:
    """
    Utility class for formatting values for output.
    """

    @staticmethod
    def format_bytes(size: int) -> str:
        """
        Format bytes into a human-readable string.
        """

        units = ["bytes", "KB", "MB", "GB", "TB"]

        value = float(size)

        for unit in units:

            if value < 1024 or unit == units[-1]:
                if unit == "bytes":
                    return f"{int(value)} {unit}"

                return f"{value:.2f} {unit}"

            value /= 1024

    @staticmethod
    def format_datetime(value: datetime) -> str:
        """
        Format a datetime object.
        """
        return value.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def heading(
        text: str,
        level: int = 1,
    ) -> str:
        """
        Return a Markdown heading.
        """
        return f'{"#" * level} {text}'

    @staticmethod
    def bullet(text: str) -> str:
        """
        Return a Markdown bullet.
        """
        return f"- {text}"