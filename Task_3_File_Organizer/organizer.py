import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

FILE_TYPES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".cpp": "Code"
}


def get_unique_path(destination):

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            destination.stem
            + f"_{counter}"
            + destination.suffix
        )

        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path!")
        return

    if folder.resolve() in [
        (folder / category).resolve()
        for category in FILE_TYPES.values()
    ]:
        print("Invalid folder selection!")
        return

    files_to_move = []

    print("\nSCANNING FILES...")
    print("-----------------------------")

    try:
        for entry in os.scandir(folder):

            if not entry.is_file():
                continue

            source = Path(entry.path)

            if source.name == Path(__file__).name:
                continue

            extension = source.suffix.lower()

            category = FILE_TYPES.get(
                extension, "Others"
            )

            destination_folder = folder / category

            destination = get_unique_path(
                destination_folder / source.name
            )

            files_to_move.append(
                (source, destination, category)
            )

    except PermissionError:
        print("Permission denied!")
        return

    # Preview mode
    print("\n========== PREVIEW MODE ==========")

    if not files_to_move:
        print("No files found to organize.")
        return

    for source, destination, category in files_to_move:
        print(
            f"{source.name} --> {category}"
        )

    print("----------------------------------")
    print(f"Total files found: {len(files_to_move)}")

    choice = input(
        "\nDo you want to organize these files? (yes/no): "
    ).strip().lower()

    if choice not in ("yes", "y"):
        print("\nOrganization cancelled.")
        return

    # File movement
    moved_count = 0
    skipped_count = 0
    category_count = {}

    print("\nORGANIZATION STARTED...")
    print("-----------------------------")

    for source, destination, category in files_to_move:

        try:
            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            # Recheck destination to avoid overwriting
            destination = get_unique_path(destination)

            shutil.move(
                str(source),
                str(destination)
            )

            moved_count += 1

            category_count[category] = (
                category_count.get(category, 0) + 1
            )

            logging.info(
                f"Moved {source.name} to {category}"
            )

        except (PermissionError, OSError, shutil.Error) as error:
            skipped_count += 1

            logging.error(
                f"Could not move {source.name}: {error}"
            )

    # Summary
    print("\n========== SUMMARY ==========")

    print(f"Files moved: {moved_count}")

    for category, count in category_count.items():
        print(f"{category}: {count} files")

    print(f"Files skipped: {skipped_count}")

    print("=============================")
    print("Organization completed!")


if __name__ == "__main__":

    print("===================================")
    print(" AUTOMATED FILE ORGANIZER")
    print("===================================")

    folder_path = input(
        "\nEnter folder path (Enter for Downloads): "
    ).strip().strip('"')

    if not folder_path:
        folder_path = str(Path.home() / "Downloads")

    organize_files(folder_path)