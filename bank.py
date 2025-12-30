import random
import re

class Bank:
    def __init__(self,name,ph_no,bal,acc_no):
        self.name = name
        self.ph_no = ph_no
        self.bal = bal
        self.acc_no = acc_no

    def main():
        dic={}
        print("------Bank Account Management System------")
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
                                    
                    


        