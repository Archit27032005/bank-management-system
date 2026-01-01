import random
import re

class Bank:
    dic={}
    def __init__(self,name,ph_no,bal,acc_no):
        self.name = name
        self.ph_no = ph_no
        self.bal = bal
        self.acc_no = acc_no

    def main(self):
        print("------Bank Account Management System------")
        # selecting a option for below
        i=int(input("\n1.Account Creation\n2.Withdrawal\n3.Deposit\n4.Balance Inquiry\n5.Transaction History\n6.Account Details Display\n7.Exit\nEnter a proper option:"))
        if i==1:
            a=input("b.Savings Account Creation \nc.Current Account Creation\npress option")
            if a=='b':
                savings_acc()
            elif a=='c':
                current()
            else:
                print("wrong value")
                exit()
        elif i==2:
            withdrawal()
        elif i==3:
            deposit()
        elif i==4:
            balance_inquiry()
        elif i==5:
            transaction_his()
        elif i==6:
            account_display()
        else:
            exit()
                    
    def savings_acc(self):
           self.name=input("Enter your name:")
           self.ph_no=int(input("Enter your phone nunber:"))
           #creating 10 digit number in string
           # 0 to 9 digit to selected and it done more 9 time in for loop
           star=("".join([str(random.randint(0,9)for _ in range(0,10))]))
           # converting string into intger
           self.acc_no=int(star)
           print("\nthe minmum amount is 100")
           self.bal=int(input("Enter a amount:"))
           if self.bal<100:
               print("less than 100 ")
               exit()
               
           else:
                  print("Account created")
                  print(f"name:{self.name}")
                  print(f"Account number:{self.acc_no}")
                  print(f"phone number{self.ph_no}")
                  print(f"Balance{self.bal}")
                  
           return None

           