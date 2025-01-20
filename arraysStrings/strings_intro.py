# 🌟 Introduction to Strings in Python 🌟

# 👨‍💻 Hey friends! Today we’re learning about strings (text) in Python. Strings are simply text, like 'Hola Mundo'. Let’s look at some fun and easy examples. 🚀

# 🌐 Defining a String
my_string = "Hola Mundo"  # 👋 Defining a string
define_string = f"My string is: {my_string}"  # Using f-strings to make it dynamic
print(define_string)

# 🌿 Joining Strings
part1 = "Hola"
part2 = "Mundo"
hola_mundo = part1 + " " + part2  # Concatenating strings with +
print(f"Joined: {hola_mundo}")

# 🔎 Accessing Specific Characters
print(f"First character: {my_string[0]} 📝")  # Accessing the first character
print(f"Last character: {my_string[-1]} 🔄")  # Accessing the last character using -1

# 💨 Reversing a String
reversed_string = my_string[::-1]  # Using slicing to reverse the string
print(f"Reversed: {reversed_string} 🔁")

# 🤔 Checking if a Word is a Palindrome
# A palindrome is a word that reads the same forwards and backwards (like "radar")
def is_palindrome(word):
    return word == word[::-1]

word = "radar"
palindrome_result = is_palindrome(word)
print(f"Is '{word}' a palindrome? {'Yes 👍' if palindrome_result else 'No 👎'}")
