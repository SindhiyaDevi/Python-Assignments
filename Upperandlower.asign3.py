#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def upperlower(str):
    upper_count = 0
    lower_count = 0
    for u in str:
        if u.isupper():
            upper_count= upper_count+1
        elif u.islower():
            lower_count= lower_count+1
        else:
            print("Interger")
    print("Count of upper case ", upper_count)
    print("Count of lower case ", lower_count)
a = input("Enter a string: ")
upperlower(a)