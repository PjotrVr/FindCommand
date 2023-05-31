import os
import re
from highlight import highlight_terminal

def search_file(start_path, name):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            full_path = os.path.normpath(os.path.join(root, file))
            match = re.search(name, file)
            if match:
                start_index = match.start() + len(root) + 1 # added + 1 so it doesn't include slashes
                end_index = match.end() + len(root)
                highlight_terminal(full_path, start_index, end_index)


def search_dir(start_path, name):
    for root, dirs, _ in os.walk(start_path):
        for directory in dirs:
            full_path = os.path.normpath(os.path.join(root, directory))
            match = re.search(name, directory)
            if match:
                start_index = match.start() + len(root) + 1 # added + 1 so it doesn't include slashes
                end_index = match.end() + len(root)
                highlight_terminal(full_path, start_index, end_index)             
  

def search_dirfile(start_path, name):
    search_file(start_path, name)
    search_dir(start_path, name)


# map the search types to the functions
search_functions = {
    "file": search_file,
    "dir": search_dir,
    "dirfile": search_dirfile,
}

if __name__ == "__main__":
    search_dir("D:/", "Karpathy")
    #search_file("D:/Programming", "main.*")