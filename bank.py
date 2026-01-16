import random
import re


class Bank:
    def __init__(self, name, ph_no, bal, acc_no):
        self.name = name
        self.ph_no = ph_no
        self.bal = bal
        self.acc_no = acc_no

    def main(self):         
        print("------Bank Account Management System------")
        # selecting a option for below
        i = int(input("\n1.Account Creation\n2.Withdrawal\n3.Deposit\n4.Balance Inquiry\n5.Transaction History\n6.Account Details Display\n7.Exit\nEnter a proper option:"))
        if i == 1:
            a = input("b.Savings Account Creation \nc.Current Account Creation\npress option")
            if a == 'b':
                dic, data_list = savings_acc(self)
            elif a == 'c':
                dic, data_list = current_acc(self)
            else:
                print("wrong value")
                exit()
        elif i == 2:
            withdrawal(self,dic,data_list)
        elif i == 3:
            deposit(self,dic,data_list)
        elif i == 4:
            balance_inquiry(self,dic,data_list)
        elif i == 5:
            transaction_his(self,dic,data_list)
        elif i == 6:
            account_display(self,dic,data_list)
        else:
            exit()

    def savings_acc(self):
            self.name = input("Enter your name:")
            self.ph_no = int(input("Enter your phone nunber:"))
           #creating 10 digit number in string
           # 0 to 9 digit to selected and it done more 10 time in for loop
            star = ("".join([str(random.randint(0,9))for _ in range(0,10)]))
           # converting string into intger
            self.acc_no = int(star)
            print("\nthe minmum amount is 100")
            self.bal = int(input("Enter a amount:"))
            if self.bal < 100:
                print("less than 100 ")
                exit()
            else:
                   print("Account created")
                   print(f"name:{self.name}")
                   print(f"Account number:{self.acc_no}")
                   print(f"phone number{self.ph_no}")
                   print(f"Balance{self.bal}")
                   
                  
             return {self.acc_no: [self.name,self.bal,self.ph_no]}, self.acc_no
    

    def current_acc(self):
         self.name = input("Enter your name:")
         self.ph_no = int(input("Enter your phone number:"))
         #creating 10 digit number in string
         #0 to 9 digit to selected and it done more 10 time in for loop
         arc = ("".join([str(random.randint(0,9))for _ in range(0,10)]))
        #string to intger
         self.acc_no = int(arc)
         print("\n the minmum amount is 100")
         self.bal = int(input("Enter a anount:"))
         if self.bal < 100:
             print("less than 100")
             exit()
        
         else:
             print("Account Created")
             print(f"name:{self.name}")
             print(f"Account number:{self.acc_no}")
             print(f"Phone number{self.ph_no}")
             print(f"Balance{self.bal}")

             return {self.acc_no:[self.name,self.bal,self.ph_no]},self.acc_no
    
    def withdrawal(self,dic,data_list):
         #take an input value to check the account is there
         o = int(input("enter the account number"))
         if o in dic.self.acc_no:
             c = int(input("enter the amount want:"))
             #in list 1 the value is bal that will be updated
             data_list[1] -= c
             print(data_list[1])
             print("amount is updates")
         else:
            Exit()
            
        return dic, data_list

    def deposit(self,dic,data_list):
        o = int(input("enter the account number"))
         if o in dic.self.acc_no:
            c=int(input("enter the amount to deposit"))
            data_list[1]+=c
            print(data_list[1])
            print("amount is updates")
         else:
            exit()

        return dic, data_list
               
        


           