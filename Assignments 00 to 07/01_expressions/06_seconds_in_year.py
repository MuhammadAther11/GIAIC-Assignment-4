Days_in_Years = 365
Hours_in_Day = 24
Minutes_per_Hour = 60
Seconds_per_Minute = 60

def main():
    

    total_seconds = Days_in_Years * Hours_in_Day * Minutes_per_Hour * Seconds_per_Minute

    print("There are", total_seconds, "seconds in a year.")

if __name__ == '__main__':
    main()