from datetime import datetime
class Bank:
    def __init__(self,name,age,gender,city,Acc_Type,pin):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city 
        self.Account_Type=Acc_Type
        self.balance=0 
        self.count=0
        self.pin=pin
        self.transaction=[]
        print("\nWELCOME!\n")
        self.operations()
        
    def operations(self):
        print("Operations Are ")
        print("1 for Show Details ")
        print("2 for Deposit ")
        print("3 for Withdraw ")
        print("4 for Mini Statement ")
        sel=int(input())
        while sel!=0:
            match sel:
                case 1:
                    self.show_details()
                case 2:
                    self.deposit()
                case 3:
                    self.withdraw()
                case 4:
                    self.mini_statement()
                case default:
                    print("Enter Valid! ")
            sel=int(input("Do you want continue if NO, press 0 \nor To continue with Above Operations "))
    
    def show_details(self):
        print("Personal Details ")
        print("Name    : ",self.name)
        print("Age     : ",self.age)
        print("Gender  : ",self.gender)
        print("City    : ",self.city)
        print("Balance : ",self.balance)
    
    def deposit(self):
        print("Deposit you Amount")
        temp_acc_type=input("Please Select Your Account Type :")
        if self.Account_Type==temp_acc_type:
            amount=int(input("Enter Amount to be Deposit : Rs."))
            self.balance+=amount
            print("Balance has been updated : Rs.",self.balance)
            self.transaction.append(f"Your a/c XX34 is credited for Rs.{amount} on {datetime.now()}  , Avl Balance : Rs. {self.balance}")
        else:
            print("You chose Wrong Account Type!")
    
    def withdraw(self):
        print("\nWithdraw your Amount")
        self.count+=1
        if self.count>=5:
            self.balance-=12 
            
        temp_acc_type=input("Please Select Your Account Type : ")
        temp_pin=int(input("Enter you secret PIN to withdraw amount : "))
        if self.Account_Type==temp_acc_type and self.pin==temp_pin:
            amount=int(input("Enter Amount to be Withdraw : Rs."))
            if amount%100!=0:
                print("Please Choose Amount as Multiple of 100 ")
                return
            if self.balance<amount:
                if self.count>=5:
                    print("Rs.12 Charge Deduction!")
                print("Insufficient Amount ! Your Balance : Rs.",self.balance)
                
            else:
                self.balance-=amount
                if self.count>=5:
                    print("Rs.12 Charge Deduction!")
                print("Balance has been updated : Rs.",self.balance)
                self.transaction.append(f"Your a/c XX34 debited Rs.{amount} on {datetime.now()}  , Avl Balance : Rs. {self.balance}")
            
        else:
            print("You entered Wrong details !")
    def mini_statement(self):
        i=0
        length=len(self.transaction)
        if length==0:
            print("No Transaction !")
        while i<5 and i<length:
            print(self.transaction[i])
            i+=1
def main():
    print("Please fill you details ")
    print("Like this : username=Bank(<full_name>,<age>,<gender>,<city>,<accountType>, <Secret PIN> \n")
    
if __name__ == "__main__":
    main()
    
