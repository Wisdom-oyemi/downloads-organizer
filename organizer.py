

import os
import shutil
import sys

def create_folders(FILE_CATEGORIES, filepath):
    for key in FILE_CATEGORIES:
        if key not in os.listdir(filepath):
            os.mkdir(os.path.join(filepath, key))





if __name__ == "__main__":
    filepath = "C:/Users/oyemi/Downloads"
    FILE_CATEGORIES = {
        "PDFs": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Archives": [".zip", ".7z", ".rar", ".tar", ".gz"],
        "Code": [".py", ".java", ".cpp", ".c", ".js", ".ts", ".html", ".css"],
    }
