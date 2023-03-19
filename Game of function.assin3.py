# Write a Python function to sum all the numbers in a list.
def add(num):
    total = 0
    for x in num:
        total = total + int(x)
    return total
#a = (1,2,3,4)
a = input("Enter a list of number")
b = a.split(',')
print(b)
print(add(b))



