
import random
import string
import database as db
from MinimumBalance import MinimumBalanceError
print("------------------Welcome  to DT Bank------------------")
while True:
        print(''' Choose the desire option given below:-
                        1. Create New account
                        2.Perform transactions for an account
                        3.Show transcation table of all accounts
                        4.Delete Account of Account holder
                        5.Exit''')
        Choice=int(input("Enter the choice from above:-"))
        if Choice==1:
                 number = string.digits
                 num=list(number)
                 random.shuffle(num)
                 accno="".join(num)
                 name = input ('Enter Account Holder Name:- ')
                 city = input('Enter the city  in which you live currently:-  ')
                 contact = int (input('Enter the contact:- '))
                 adhaar=int(input("Enter the valid Adhaar card Number:- "))
                 pin=int(input("Enter the secret pin to access the account:- "))
                 balance=int(input("Enter the amount You want to deposit first:- "))                 
                 try:
                    if balance<5000:
                        raise MinimumBalanceError("Amount should be greater than 5000 ")
                 except MinimumBalanceError as e:  #User defined Exception
                    print(e)
                    continue
                 try:
                    db.Create(accno,name,city,contact,adhaar,pin,balance)
                    print('Account Created Successfully')
                 except:
                       print('Adding Operation Failed')
                        
        elif Choice==2:
            print('''Select the action you want to perform on your account given below:-
                     1.Deposist  money in  the account
                     2.Withdraw money from the account
                     3.Change the name of the account holder
                     4.Exit from this menu''')
            Action=int(input("Enter the action:- "))
            if Action==1: #Deposit function
             pin=int(input("Enter the secret pin to access the account:- "))
             data= db.showcustomer()
             for i in  data:
              i=list(i)     
              if i[6]==pin: 
                amount=int(input("Enter the Amount you want to Deposit:- "))
                i[5]+=amount
                try:
                    type='deposit'
                    db.Deposist(pin,amount,i[0],type)
                    print("Amount Deposisted sucessfully")
                    print("Your current balance is:-",i[5])
                    print("Thankyou")
                    break
                except Exception as e:
                    print(e)
                    print("Enter correct pin!")
            
            elif Action==2: #Withdrawn function
             pin=int(input("Enter the secret pin to access the account:- "))
             data=db.showcustomer()
             for i in data:
                i=list(i)
                if i[6]==pin:
                 print("Note:- Account should have minimum Rs5000")
                 amount=int(input("Enter the amount to withdrawn:- "))
                 try:
                     if i[5]-amount<5000:    #User defined Exception
                      raise MinimumBalanceError("Account Should have minimum 5000 Balance ")
                      break      
                 except MinimumBalanceError as e:
                    print(e)
                 try:   
                    if i[5]-amount>=5000:
                     i[5]-=amount
                     type='withdrawn'
                     db.Withdrawn(pin,amount,i[0],type)
                     print("Money Withdrawn Successfully")
                     print("Your current balance is:-", i[5])
                     print("Thankyou")
                 except:
                    print("Money Cannot Withdrwan") 
            elif Action==3: #Update Customer Name
                pin=int(input("Enter the secret pin to access the account:- "))
                newname = input('Enter New Name: ')                     
                data = db.showcustomer()
                for i in data:
                    if i[6] == pin:                      
                     db.updatename(pin,newname)
                     print("Name of Account Holder Updated Successfully")
                     break
                else:
                    print('Invalid pin')

            elif Action==4:
                continue
            
        
        elif Choice==3:
            data = db.showtransaction()
            for i in data:
             print(f'Accno: {i[0]} Amount: {i[1]} Type: {i[2]}')

        elif Choice==4:
            pin=int(input("Enter the secret pin to access the account:- "))
            data=db.showcustomer()
            for i in data:
              if i[6] == pin:
               db.deleteaccount(pin)
               print("Account Deleted Successfully")
               break
            else:
              print ('Invalid pin')   

        elif Choice==5:
            break
        else:
            print(" Invalid choice")
