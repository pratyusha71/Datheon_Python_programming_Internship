import shutil
from pathlib import Path

downloads = Path.home() / "Downloads"

categories = [
    "Documents",
    "Images",
    "Videos",
    "Audio",
    "Archives",
    "Code",
    "Others"
]

restored = 0

print("Starting File Restoration...")
print("-----------------------------")

for category in categories:

    folder = downloads / category

    if folder.exists():

        for file in list(folder.iterdir()):

            if file.is_file():

                destination = downloads / file.name
                counter = 1

                while destination.exists():
                    destination = downloads / (
                        f"{file.stem}_{counter}{file.suffix}"
                    )
                    counter += 1

                shutil.move(str(file), str(destination))
                restored += 1

                print(f"Restored: {file.name}")

        if not any(folder.iterdir()):
            folder.rmdir()

print("-----------------------------")
print("RESTORATION COMPLETED!")
print(f"Total files restored: {restored}")