def main():

    side1  = float(input("Enter the length of the first side of the triangle: "))
    side2  = float(input("Enter the length of the second side of the triangle: "))
    side3  = float(input("Enter the length of the third side of the triangle: "))

    perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is: {perimeter}")

if __name__ == "__main__":
    main()