def write_file():
    with open("notes.txt","w") as file:
        file.write("I love you.\n")
        file.write("I love you.\n")
        file.write("I love you.\n")
        file.close()
def read_file():
    with open("notes.txt","r") as file:
        return file.read()

def main():
    write_file()
    print(read_file())
if __name__=="__main__":
    main()