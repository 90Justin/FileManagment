import os
import shutil

EXTENSIONS = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.pdf': 'Text', '.doc': 'Text', '.docx': 'Text', '.txt': 'Text',
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
    '.mp4': 'Video', '.avi': 'Video', '.mkv': 'Video',
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
    '.3mf': '3dPrints',
}

def get_destination_folder(file_extension: str, base_path: str, misc_folder: str) -> str:
    if file_extension in EXTENSIONS:
        return os.path.join(base_path, EXTENSIONS[file_extension])
    return misc_folder

def handle_duplicate_filename(destination_folder: str, filename: str, extension: str) -> str:
    destination = os.path.join(destination_folder, filename + extension)
    counter = 0
    
    while os.path.exists(destination):
        counter += 1
        new_filename = f"{filename}({counter}){extension}"
        destination = os.path.join(destination_folder, new_filename)
    
    return destination

def move_file(source: str, destination: str) -> bool:
    try:
        shutil.move(source, destination)
        print(f"Moved {os.path.basename(source)} to {os.path.basename(os.path.dirname(destination))} "
              f"as {os.path.basename(destination)}")
        return True
    except Exception as e:
        print(f"Error moving {os.path.basename(source)}: {e}")
        return False

def organize_files(source_directory: str) -> None:
    files_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Files') #Change this to the path of the folders you want to use to organize your files
    misc_folder = os.path.join(files_path, 'Misc')

    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)
        if os.path.isdir(file_path):
            continue

        file_name, extension = os.path.splitext(file)
        destination_folder = get_destination_folder(extension, files_path, misc_folder)
        destination = handle_duplicate_filename(destination_folder, file_name, extension)
        move_file(file_path, destination)

def main():
    directory = input("Enter the directory path to organize: ")
    if os.path.exists(directory):
        organize_files(directory)
        print("Organization complete!")
    else:
        print("Directory does not exist!")

if __name__ == "__main__":
    main()