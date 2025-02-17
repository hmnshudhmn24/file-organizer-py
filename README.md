# File Organizer

## Description
This Python script automatically organizes files in a given directory into categorized folders based on file extensions.

## Features
- Categorizes files into predefined folders (Images, Documents, Videos, etc.)
- Moves unclassified files to an 'Others' folder
- Creates missing category folders automatically

## Usage
1. Clone this repository.
2. Run the script:
   ```bash
   python file_organizer.py path_to_directory
   ```
3. The script will automatically sort files into respective folders.

## Requirements
- Python 3.x
- `shutil` and `os` modules (built-in)

## Example
Before:
```
Downloads/
  file1.jpg
  file2.pdf
  file3.mp4
```
After running the script:
```
Downloads/
  Images/
    file1.jpg
  Documents/
    file2.pdf
  Videos/
    file3.mp4
```
