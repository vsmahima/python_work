#ATM withdrawal and balance checking

total=100000
minimum=1000
amount = int(input("Enter the amount to withdraw:"))
if(amount>total):
    print("Insufficient amount in your account,Please check your balance")
elif(amount==total):
    print(f"Cant withdraw full amount,please maintain minimum balance rs {minimum}")
elif(amount<total):
    print(f"{amount} withrawn successfully\n Balance is {total-amount}")
else:
        print("Please try agian after some time")

