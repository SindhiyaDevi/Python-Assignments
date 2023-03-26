#Write a Python program to triple all numbers of a given list of integers. Use Python map.
a = input("Enter a list of numbers: ").split(',')
print(a)
result = map(lambda n: int(n)*3, a)
print(list(result))