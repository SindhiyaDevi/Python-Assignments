#Write a Python program to count the number of even and odd numbers from a series of numbers.
odd  =0
even =0
for i in range(1,10):
    if(i%2==0):
        n1 = even +1
        even = n1
    elif(i%2!=0):
        n2 = odd+1
        odd = n2
print("number of even number", even)
print("number of odd number", odd)

    