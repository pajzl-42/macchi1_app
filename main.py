from classes import *

def main():
    data = gui()
    output = constructor(data)
    print(output[0])
    st.button("Vypsat data do souboru", writer(output[0], output[1]))


if __name__ == '__main__':
    main()


