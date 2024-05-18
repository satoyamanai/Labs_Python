def find_min_divider_for(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i

def find_min_divider_while(number):
    i = 2
    while i <= number:
        if number % i == 0:
            return i
        i += 1


if __name__ == "__main__":
    number = int(input("Enter an integer (>= 2): "))
    print("Using for loop:", find_min_divider_for(number))
    print("Using while loop:", find_min_divider_while(number))
