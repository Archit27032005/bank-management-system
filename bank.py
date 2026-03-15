import random
 
class Bank:
    def __init__(self):
        dic_id={}
    def main(self):
        print("-----Bank mangment system-----")
        print("1.Created Account\n2.Deposit Money\n3.Withdrawal Money\n4.Balance Inquiry\n5.Account Details\n6.Exit")
        op=int(input("Enter Your Option:"))
        if op==1:
            print("a.Savings Account or b.Current Account")
            op_2=input("Enter your option:").lower()
            if op_2 =='a':
                self.saving_account()
            else:
                self.current_account()
        elif op==2:
            self.deposit()
        elif op==3:
            self.withdrawal()
        elif op==4:
            self.balance_inq()
        elif op==5:
            self.account_display()
        else:
            exit()
