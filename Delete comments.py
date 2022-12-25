import os


def deleteComments(file):
    try:
        my_file = open(file, 'r')
        data = my_file.read()
        clean = ""
        comments_count = 0
        for i in data.split('\n'):
            if i[0] == "#":
                clean += i
                clean += '\n'
                comments_count += 1
            else:
                pass
        name = os.path.basename(path)
        with open("clean-" + name, "w") as f:
            f.write(clean)
            f.close()
        my_file.close()
        return comments_count

    except:
        print("An error occurred with accessing the files")
        return file








