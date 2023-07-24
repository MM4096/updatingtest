import wget
import os

GITHUB_USERNAME = "MM4096"
GITHUB_REPOSITORY = "updatingtest"


def Download(file, name):
    wget.download(f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPOSITORY}/master/{file}", name)


if __name__ == '__main__':
    version = "0.0.0"
    if not os.path.exists('Data/version.txt'):
        pass
    else:
        with open('Data/version.txt', 'r') as f:
            version = f.read()
    Download("version.txt", "Data/version.txt")
