import os

def listFiles_errorHandling(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "fie not found"
    except PermissionError:
        return None, "permssion denied"
def main():
    folders = input("please provide the folders list with spaces:").split()
    print(folders)

    for folder in folders:
        files, Error = listFiles_errorHandling(folder)
        if files:
            print(f"files exist in {folder}" )
            for file in files:
                print(file)
        else:
            print(f"Error while fetching files in {folder}:  {Error}")
##calling the main function

#main()
if __name__ == "__main__":
    main()