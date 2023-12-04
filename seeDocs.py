import sys
import os
import getopt

"""This module allows you to see the documentation of all functions.
"""


def seeDocs(module):
    try:
        help(module)
    except Exception as e:
        print(str(e))
        sys.exit(1)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:a", ["help", "module=", "all"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        print("Usage: seeDocs.py <flags> <module_name>")
        sys.exit(2)
    output = None
    for o, a in opts:
        if o in ("-h", "--help"):
            print(
                "Usage: seeDocs.py <flags> <module_name>\n Example: seeDocs.py -m modules.randomData"
            )
            sys.exit()
        elif o in ("-m", "--module"):
            output = a
            seeDocs(a)
        elif o in ("-a", "--all"):
            output = "all"
            # List all py files in dir .
            # Get all Python files in the directory and its subdirectories, excluding 'env' directory
            python_files = []
            for root, dirs, files in os.walk("."):
                # Exclude 'env' directory
                if "env" in dirs:
                    dirs.remove("env")

                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        # Remove "./" prefix and replace slashes with dots
                        relative_path = file_path.replace("." + os.sep, "").replace(
                            os.sep, "."
                        )
                        # Remove ".py" extension
                        python_files.append(os.path.splitext(relative_path)[0])
            for file in python_files:
                seeDocs(file)


# Path: modules/seeDocs.py
if __name__ == "__main__":
    main()
