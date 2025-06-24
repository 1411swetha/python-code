def update_server_config(file_path, key, value):
    with open("file.txt", "r") as file:
        lines = file.readlines()
    with open("file.txt", "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value)
            else:
                file.write(line)

update_server_config("file.txt", "Max_Connections", "1000")
