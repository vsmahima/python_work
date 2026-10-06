#Menu driven program (repeat until user exit)
print("""MENU
    1.Add
    2.Subtract
    3.Exit
""")

while True:
    menu=input("choose your option:")
    if(menu=="1"):
        num1=int(input("Enter first number:"))
        num2= int(input("Enter second number:"))
        print(f"{num1}+{num2}={num1+num2}")
    elif(menu=="2"):
        num1=int(input("Enter first number:"))
        num2= int(input("Enter second number:"))
        print(f"{num1}-{num2}={num1-num2}")
    elif(menu=="3"):
        print("Temperory Exit...")
        break
    else:
        print("Wrong choice")
    ch=input("Do you like to continue (y|n:)")
    if(ch.lower()=="n"):
        print("Completely exited")
        exit()
print("Out of menu")