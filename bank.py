import random
 
class Bank:
    def __init__(self):
        self.dic_id={}

    def main(self):
        while True:
            print("-----Bank mangment system-----")
            print("1.Created Account\n2.Deposit Money\n3.Withdrawal Money\n4.Balance Inquiry\n5.Account Details\n6.Exit")
            try:
                op=int(input("Enter Your Option:"))
            except ValueError:
                print("enter a number")
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
            elif op==6:
                print("thank you for using Bank System. Goodbye!")
                exit()
            else:
                print("Invaild option picked")
        

    def saving_account(self):
        name=input("enter your name:")
        try:
            ph_no=int(input("enter the phone number"))
        except ValueError:
            print("enter a number")
            return
         
        #creating 10 digit number in string
        # 0 to 9 digit to selected and it done more 10 time in for loop
        star = ("".join([str(random.randint(0,9))for _ in range(0,10)]))
        # converting string into intger
        acc_no = int(star)
        bal = int(input("Enter a amount:"))
        if bal < 100:
            print("less than 100 ")
            return
        else:
                print("Account created")
                print(f"name:{name}")
                print(f"Account number:{acc_no}")
                print(f"phone number{ph_no}")
                print(f"Balance{bal}")
        
        self.Bank.dic_id[acc_no]={"name":name,"ph_no":ph_no,"bal":bal, "type":"saving account"}