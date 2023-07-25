import wget
import os
import requests

GITHUB_USERNAME = "MM4096"
GITHUB_REPOSITORY = "updatingtest"


def Download(file, name):
    path = "https://raw.githubusercontent.com/" + GITHUB_USERNAME + "/" + GITHUB_REPOSITORY + "/master/" + file
    r = requests.get(path)
    if r.status_code == 200:
        try:
            with open(name, 'x') as fi:
                fi.write(r.text)
        except FileExistsError:
            with open(name, "w") as fi:
                fi.write(r.text)
    else:
        print("Couldn't download file: " + file)


if __name__ == '__main__':
    version = "0.0.0"
    if not os.path.exists('Data/'):
        os.mkdir('Data/')
    elif not os.path.exists('Data/version.txt'):
        pass
    else:
        with open('Data/version.txt', 'r') as f:
            version = f.read()
    Download("version.txt", "Data/version.txt")
    newVersion = ""
    with open('Data/version.txt', 'r') as f:
        newVersion = f.read()

    print("saved version: " + version + "\nnew version: " + newVersion)
    version = version.split('.')
    newVersion = newVersion.split('.')

    if int(newVersion[0]) > int(version[0]):
        print("Major update")
    elif int(newVersion[1]) > int(version[1]):
        print("Minor update")
    elif int(newVersion[2]) > int(version[2]):
        print("Patch")

    if not version == newVersion:
        wget.download("https://raw.githubusercontent.com/" + GITHUB_USERNAME + "/" + GITHUB_REPOSITORY + "/master/main.exe", "main.exe")

    a = input("Press enter to continue")
