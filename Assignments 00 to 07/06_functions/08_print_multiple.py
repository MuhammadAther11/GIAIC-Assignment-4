
def print_multiple(message : str, repeat : int) :
    """Prints a message multiple times.

    Args:
        message (str): The message to print.
        times (int): The number of times to print the message.
    """
    for _ in range(repeat):
        print(message)
    
def main():
    message = input("Enter a message: ")
    repeat = int(input("Enter the number of times to print the message: "))
    print_multiple(message, repeat)

if __name__ == "__main__":
    main()