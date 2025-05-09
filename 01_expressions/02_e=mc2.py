def main():
    # Define mass in kilograms
    m = 100.0  # mass in kg

    # Define the speed of light in meters per second
    C = 299792458  # speed of light in m/s

    # Calculate energy using E = mc^2
    e = m * C**2

    # Print the result
    print(f"\033[1;3m {e} joules of energy! \033[0m ")

if __name__ == "__main__":
    main()