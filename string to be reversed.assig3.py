#Write a Python program to reverse a string.
def reverse(string):
    string = string[::-1]
    return string
str = input("Enter a string to be reverse")
print(reverse(str))