import os
import re


def search_file(start_path, name):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if re.match(name, file):
                print(os.path.normpath(os.path.join(root, file)))

                
def search_dir(start_path, name):
    for root, dirs, _ in os.walk(start_path):
        for directory in dirs:
            if re.match(name, directory):
                print(os.path.normpath(os.path.join(root, directory)))
              
  
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