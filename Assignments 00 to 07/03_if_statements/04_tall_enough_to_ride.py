MINIMUM_HEIGHT : int = 50 

def main():

    height = float(input("how tall are you?"))

    if height >= MINIMUM_HEIGHT:
        print("You are tall enough to ride.")
    else:
        print("You are not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()