#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
x = lambda a: a + 25
num = int(input("Enter a number to be added: "))
print(x(num))