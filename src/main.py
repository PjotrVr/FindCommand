import os
import argparse

from sys import exit
from art import text2art
from search import search_dir, search_file, search_dirfile
from search import search_functions

parser = argparse.ArgumentParser(add_help=False)

# arguments for searching
group_search = parser.add_mutually_exclusive_group(required=False)
group_search.add_argument("-d", "--dir", action="store_true", help="Search for directories")
group_search.add_argument("-f", "--file", action="store_true", help="Search for files")
group_search.add_argument("-df", "--dirfile", action="store_true", default=True, help="Search for both files and directories")

# other arguments
parser.add_argument("-cs", "--case_sensitive", action="store_true", help="Is case sensitive to passed name")
parser.add_argument("--name", default="", type=str, help="Name pattern for files and directories")
parser.add_argument("start_path", type=str, help="Starting path of the search")

# parsing args, if illegal flag occours then help message printed
try:
    args = parser.parse_args()

except SystemExit:
    with open("../help.txt") as f:
        help_text = f.read()

    print(text2art("FindCommand", font="small"))
    print(help_text)
    exit(1)

if args.dir:
    search_type = "dir"

elif args.file:
    search_type = "file"
    
else:
    search_type = "dirfile"
    
search_function = search_functions[search_type]
search_function(args.start_path, args.name, args.case_sensitive)