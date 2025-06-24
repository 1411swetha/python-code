import os

folders = input("please provide the folders list with spaces:").split()
print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("pls provide valid folder name:" +folder)
        break
    except PermissionError:
        print("you dont have permission to folder name:" +folder)
        break
    print("listing files in folders:" + folder)
    for file in files:
        print(file)