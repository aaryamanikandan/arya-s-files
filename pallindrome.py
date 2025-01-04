def is_palindrome(word):
    
    word = word.lower()
    
    return word == word[::-1]

# Input from the user
word = input("Enter a word: ")

# Check and display the result
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
