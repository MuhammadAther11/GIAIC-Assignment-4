
def main():
    numbers = [1, 2, 3, 4, 5]
    

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2
    # numbers = [elem * 2 for elem in numbers]  

    print(numbers)


if __name__ == "__main__":
    main()