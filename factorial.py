def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example
number = 10
print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")
