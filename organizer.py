FILE_CATEGORIES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Archives": [".zip", ".7z", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".js", ".ts", ".html", ".css"],
}

import os
import shutil
import sys

folder_path = input("Enter file path: ").strip('/"')
decoded_folder_path = os.fsdecode(folder_path)
os.chdir(f'{decoded_folder_path}')
os.makedirs('Organizer-Folder/SubFolder-1')


'''
def create_folders(dir_path, FILE_CATEGORIES):
    for key in FILE_CATEGORIES:
        if key not in 
    pass


def get_files(filepath):
    for file in os.listdir(filepath):
        filename = os.fsdecode(file)
        print(filename)


if __name__ == "__main__":
    filepath = sys.argv[0]
    get_files(filepath)

'''