#Keep asking user input until they exit
cart = {}
#print(type(cart))

while True:
    item_name=input("Enter the item:")
    item_price=float(input("Enter the price:"))
   # print(item,price)
    cart.update({item_name:item_price})
    ch=input("Do you like to continue(y|n)")
    if(ch.lower()=="n"):
        break
print(cart)