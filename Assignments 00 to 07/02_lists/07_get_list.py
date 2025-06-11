
def main():
    lst = [] 

    val = input("Enter a value: ") 
    while val: 
        lst.append(val)
        val = input("Enter a value or press enter to stop: ") 

    print("Here's the list:", lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

