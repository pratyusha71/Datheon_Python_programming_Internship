# Automated File Organizer & Cleanup Utility

## 1. Project Overview

The Automated File Organizer & Cleanup Utility is a Python-based application designed to organize files automatically based on their file extensions.

It scans a selected directory, identifies different file types, creates appropriate folders, and moves files into their respective categories.

The application also provides a preview mode that allows users to review the changes before organizing their files.

## 2. Problem Statement

Managing large numbers of files manually can be time-consuming and confusing.

This project provides an automated solution to organize files efficiently, reduce clutter, and improve file management.

## 3. Objectives

- Automate file organization.
- Identify files based on extensions.
- Create category folders automatically.
- Prevent accidental file overwriting.
- Handle permission errors.
- Provide a preview before moving files.
- Display an execution summary.

## 4. Technologies Used

- Programming Language: Python
- Libraries:
  - os
  - shutil
  - pathlib
  - logging

## 5. Key Features

### Automatic File Categorization
Organizes files into:
- Documents
- Images
- Videos
- Audio
- Archives
- Code
- Others

### Preview Mode
Displays the files and their proposed destinations before moving them.

### Duplicate File Handling
Prevents overwriting by generating unique filenames.

### Error Handling
Handles permission errors and file movement issues.

### Execution Summary
Displays the total number of files moved and category-wise counts.

### File Restoration
Includes a separate utility to restore organized files to the Downloads folder.

## 6. Project Structure

Task_3_File_Organizer/
│
├── organizer.py
├── restore_files.py
└── README.md

## 7. How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

   python organizer.py

5. Enter the folder path.
6. Review the preview.
7. Enter yes to organize files or no to cancel.

## 8. Restoration Utility

To restore files from the category folders:

   python restore_files.py

## 9. Expected Output

The application displays:

- Files identified.
- Proposed file categories.
- Organization confirmation.
- Total files moved.
- Category-wise file counts.
- Files skipped.

## 10. Conclusion

The Automated File Organizer & Cleanup Utility simplifies file management through Python automation.

It reduces manual effort, improves directory organization, and provides a safer and more efficient way to manage files.