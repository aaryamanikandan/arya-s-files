# Function to reverse a word
def reverse_word(word):
    return word[::-1]

# Input from the user
word = input("Enter a word: ")

# Reverse the word and display the result
reversed_word = reverse_word(word)
print(f"The reversed word is: {reversed_word}")
