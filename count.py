def count_digits(number):
    # Convert the number to a positive integer
    number = abs(number)
    # Convert the number to a string and count its length
    return len(str(number))

# Input from the user
num = int(input("Enter a number: "))
print(f"The total number of digits in {num} is {count_digits(num)}.")
