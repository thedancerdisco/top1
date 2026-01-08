with open("hello.txt", "w", encoding = "utf-8") as file:
    print(file)

class  Filewriter:
    def __init__(self, filename:str)->None:
        self.filename = filename
        self.file = None


    def __enter__(self)->"FileWriter":
        self.file = open(self.file, "w")
        return self


    def write(self, text:str)->None:

        # self.file = open(self.filename, "w")
        self.file.write(text)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"errpr:{}")
        self.file.close()
        return True




with Filewriter("text.txt") as fw:
    fw.write("poka poka")

print()
print()
