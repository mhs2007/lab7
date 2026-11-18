
def check_palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"


# Get input from user
word = input("Enter a string: ")

result = check_palindrome(word)
print(result)
