import os
import shutil
import argparse

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".html", ".css"],
    "Executables": [".exe", ".msi", ".apk", ".dmg"],
    "Others": []
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Error: Directory does not exist!")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(directory, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"Moved: {file} -> {category}/")
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(directory, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"Moved: {file} -> Others/")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by type.")
    parser.add_argument("directory", type=str, help="Path to the directory to organize")
    args = parser.parse_args()

    organize_files(args.directory)
    print("File organization complete!")

if __name__ == "__main__":
    main()
