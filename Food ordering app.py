import json
from tkinter import *
import pprint
root = Tk()
root.geometry("500x300")
Label(root, text="User Registration form", font = 'ar 15 bold').grid(rows=1, column=3)

Name = Label(root, text="Name") 
Phone_number = Label(root, text="Phone Number") 
Email = Label(root, text="Email") 
Address = Label(root, text="Address ") 
Password = Label(root, text="Password") 

Name.grid(row=2, column=2)
Email.grid(row=3, column=2)
Phone_number.grid(row=4, column=2)
Address.grid(row=5, column=2)
Password.grid(row=6, column=2)

root.mainloop()

with open('D:\Edyoda\menu.json', 'r') as f:
    data = json.load(f)
    print(data)
items = data.get('items', []) 
while True:
    print('-'*40)
    print('Indian cusine Restaurant')
    print('-'*40)
    print("1. Show Menu")
    print("2. Order items")
    print("3. Update cart")
    print("4. Add review")
    print("5. Exit")
    print('-'*40)
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        print('-'*40)
        print("ID \t Name\t\t price")
        print('-'*40)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
    elif choice == 2:     
        order_items = list(map(int, input('What item you want to try').split(',')))
        print('-'*40)
        print("ID \t Name\t\t price")
        print('-'*40)
        total_bill = 0
        for order_item in order_items:
            for item in items:
                if item["id"] == order_item:
                    print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
                    total_bill = total_bill + int(items.get('price', 10))
                    break
        print('-'*40)
        print('Total amount:', items.get("price"))
        print('-'*40)
        break
id_no = list(map(int, input("Enter the id to be changed: ").split(',')))
print(id_no)
for item in items:
    for i in id_no:
        if i ==item["id"]:
             items_details= {    
            "id": input("enter food id:"),
            "name": input ("Enter the 1item"),
            "price": input("Enter the price of the item"),
            "Quantity": input("Enter the quantity of the item"),
            "discount": input("Enter the dicount percentage"),
            "available_stock": input("Enter the available stock")
        }
        with open('D:\Edyoda\menu.json', 'w') as file_object:
                json.dump(items_details, items)
                f= open('D:\Edyoda\menu.json')
                data = json.load(f)
print(data)
   
  



