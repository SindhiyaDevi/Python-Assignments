#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
a = int(input("Enter a length of list"))
b = []
for i in range(a):
    c = int(input("enter the first element of tuple"))
    d = int(input("Enter the 2nd element of tuple"))
    b.append((c,d))
print(b)
n = len(b)
for i in range(n-1):
    for j in range(0,n-i-1):
        if b[j][1]>b[j+1][1]:
            b[j], b[j+1] = b[j+1],b[j]
print(b)