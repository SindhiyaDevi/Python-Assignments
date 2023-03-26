#Write a Python program to square the elements of a list using map() function.

a = input("Enter a sequence of number to create a list: ").split(',')
print(a)
result = map(lambda n:int(n)**2, a)
print(list(result))