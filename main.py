from classes import *

def main():
    data = gui()
    output = constructor(data)
    print(output[0])
    writer(output[0], output[1])
    download_file(output[0], output[1])


if __name__ == '__main__':
    main()


