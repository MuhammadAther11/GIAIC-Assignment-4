import math

def main():

    ab = float(input("Enter length of side AB: "))
    ac = float(input("Enter length of side AC: "))
    
    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length of the hypotenuse is: {bc}")

if __name__ == "__main__":
    main()