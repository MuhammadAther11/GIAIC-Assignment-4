SENTENCE_START : str = "Panaversity is fun. I learned to program and used Python to make my " 

def main():

    adjective : str = input("Enter a adjective and press Enter: ")
    noun : str = input("Enter a noun and press Enter: ")
    verb : str = input("Enter a verb and press Enter: ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


if __name__ == '__main__':
    main()