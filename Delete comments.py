import os


def deleteComments(file):
    try:
        my_file = open(file, 'r')
        data = my_file.read()
        clean = ""
        comment = 0
        for i in data.split('\n'):
            if i[0] == "#":
                clean += i
                clean += '\n'
                comment += 1
            else:
                pass
        name = os.path.basename(path)
        with open("clean-" + name, "w") as f:
            f.write(clean)
            f.close()
        my_file.close()
        return comment





    except:
        print("An error occurred with accessing the files")
        return file


print(deleteComments("comments.txt"))
