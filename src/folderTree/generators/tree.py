from __future__ import annotations

from folderTree.models import Project, Folder


class TreeGenerator:
    """
    Generates a tree representation from a Project model.
    """

    def generate(self, project: Project) -> str:
        """
        Generate a tree string from a project.
        """

        lines: list[str] = []

        lines.append(f"{project.name}/")

        self._build_tree(
            folder=project.root_folder,
            prefix="",
            lines=lines,
        )

        return "\n".join(lines)

    def _build_tree(
        self,
        folder: Folder,
        prefix: str,
        lines: list[str],
    ) -> None:
        """
        Recursively build tree lines from a folder.
        """

        entries = sorted(
            [
                *folder.folders,
                *folder.files
            ],
            key = lambda entry: (
                not isinstance(entry, Folder),
                entry.name.lower(),
            )
        )

        for index, entry in enumerate(entries):

            is_last = index == len(entries) - 1

            if is_last:
                connector = "└── "
                next_prefix = prefix + "    "
            else:
                connector = "├── "
                next_prefix = prefix + "│   "

            if isinstance(entry, Folder):

                lines.append(
                    f"{prefix}{connector}{entry.name}/"
                )

                self._build_tree(
                    folder=entry,
                    prefix=next_prefix,
                    lines=lines,
                )

            else:

                lines.append(
                    f"{prefix}{connector}{entry.name}"
                )