import os



def files_listing_error_handling(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:.

        print("pls check the folder doesnot exist" + folder)
        return None, "Folder not found"
    except PermissionError:
        print("You donot have permission to aces the folder" + folder)
        return None, "Permission denied"
def main():
    folders = input("please provide the folders list with spaces:").split()
    print(folders)

    for folder in folders:
        files, Errors = files_listing_error_handling(folder)
        if files:
            print(f"files exist in {folder}")
            for file in files:
                print(file)
        else:
            print(f"files does not exist in {folder}: {Errors}")
# this if statement is useful when we import into other progame as module.if we only use main() it is useful while we run program directly
if __name__ == "__main__"
    main()

