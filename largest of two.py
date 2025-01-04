# Function to find the largest of two numbers
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

# Input two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Find and display the largest number
largest = find_largest(number1, number2)
print(f"The largest number is: {largest}")
