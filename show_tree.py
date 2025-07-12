import os

def tree(dir_path, indent=""):
    for item in os.listdir(dir_path):
        path = os.path.join(dir_path, item)
        print(indent + "|-- " + item)
        if os.path.isdir(path):
            tree(path, indent + "    ")

tree(".")

