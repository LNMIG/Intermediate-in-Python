def read():
    numbers= []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for number in f:
            numbers.append(int(number))
        print(numbers)

def write():
    names= ["Pepe", "Juan", "Diego", "Ariel", "Fiona"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for each in names:
            f.write(each + "\n")

            # for each in names:
            #     f.write(each)
            #     f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()