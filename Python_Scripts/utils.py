# utils.py

from pathlib import Path


def read_file(path):

    path = Path(path)

    if not path.exists():
        print(f"File not found: {path}")
        return ""

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_markdown_folder(folder):

    folder = Path(folder)

    if not folder.exists():
        print(f"Folder not found: {folder}")
        return ""

    content = []

    # SORT FILES FOR CONSISTENT ORDER
    files = sorted(folder.glob("*.md"))

    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                content.append(
                    f"\n# FILE: {file.name}\n\n{f.read()}"
                )

        except Exception as e:

            print(
                f"Error reading {file.name}: {e}"
            )

    return "\n".join(content)


def save_file(path, content):

    path = Path(path)

    # AUTO CREATE PARENT FOLDER
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)