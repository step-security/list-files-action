import json
import os
import sys

def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_EXT"]

    matched = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                matched.append(os.path.join(root, file))

    paths = json.dumps(matched)
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f'paths={paths}\n', file=f)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()
