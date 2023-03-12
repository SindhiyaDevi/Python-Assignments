my_dict = {}
a = input("Enter a list of alaphabet to get its ASCII values")
b = a.split(',')
print(b)
p = len(b)
i=0
while (i<p):
     c =(b[i])
     my_dict[c] = ord(c)
     i+=1
print(my_dict)