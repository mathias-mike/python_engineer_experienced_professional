import os
import glob
from sniff_json_schema import run

def retrieve_files(path):
    return glob.glob(os.path.join(path, "*.json"))

def main():
    input_path = "data"

    files = retrieve_files(input_path)
    for file in files:
        run(file)

if __name__ == "__main__":
    main()


