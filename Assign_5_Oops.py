#Challenge 1:Square Numbers and Return Their Sum
# class Point:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def sqSum(self):
#        sum = self.x**2+self.y**2+self.z**2
#        return sum
# s1 = int(input("Enter the first number: "))
# s2 = int(input("Enter the second number: "))
# s3 = int(input("Enter the third number: "))
# a = Point(s1,s2,s3)
# print(a.sqSum())


#Challenge 2: Impement a calculator class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        addition = self.num1+self.num2
        return addition
    def subtract(self):
        Subtraction = self.num2 - self.num1
        return Subtraction
    def multiply(self):
        multi = self.num1*self.num2
        return multi
    def divide(self):
        division = self.num2/self.num1
        return division
s1 = int(input("Enter the first number: "))
s2 = int(input("Enter the second number: "))

obj  = Calculator(s1,s2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())


#challenge 3: Implement the complete Student Class

class Student:
    def __init__(self):
        self.__name = "Sindhiya"
        self.__rollno = 19
    def get_name(self):
        print("Student name:", self.__name)    
    def get_rollno(self):
        print ("Roll no: {}".format(self.__rollno))
    def set_name(self, name):
        self.__name = name 
    def set_rollno(self, rollno):
        self.__rollno = rollno
a = Student()
a.get_name()
a.get_rollno()
a.set_name("Ajeesh")
a.get_name()
a.set_rollno(23)
a.get_rollno()


#Implement a Banking account using the concept of inheritance:

class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance
    def Account_holder(self):
        print("Account holer name: {},   Balance: {}".format(self.title, self.balance))
class SavingsAccount(Account):
    def __init__(self,title, balance=0, rate = 0):
        Account.__init__(self, title, balance)
        self.rate = rate
    def Savings_account_detail(self):
        print("Account holder name: {},    Balance: {},    interest rate {}". format(self.title, self.balance, self.rate))
a = Account("Anish", 5000)
a.Account_holder()
a = SavingsAccount("Anish", 5000, 5)
a.Savings_account_detail()


#Challege 5: Handling Banking account using inheritance

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
    def getbalance(self):
        print("Balance= ", self.balance)
    def deposit(self, depo_amount):
        self.depo_amount = depo_amount
        self.balance+=self.depo_amount
        print("Current Balance after deposit = ",self.balance)
    def withdrawl(self, withd_amount):
        self.withd_amount = withd_amount
        self.balance-=self.withd_amount
        print("Current Balance after withdrawl = ", self.balance)

class SavingsAccount(Account):
    def __init__(self, balance=0, rate = 0):
        Account.__init__(self, balance)
        self.rate = rate
    def interest_amount(self):
        result = (self.balance*self.rate)/100
        print("Interest amount received= ", result)
    
    
a = Account(5000)
a.getbalance()
a.deposit(500)
a.withdrawl(500)
obj = SavingsAccount(2000, 5)
obj.interest_amount()