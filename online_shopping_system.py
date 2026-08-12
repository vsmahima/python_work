fruits={"Apple":100,
        "Orange":120,
        "Kiwi":150,
        "Grapes":175,
        "Strawberry":200,
        "Banana":80}
        
print("ITEMS AND ITS PRICE \n")
print(fruits)
cart={}
# import pandas as pd
# df = pd.DataFrame(fruits)
# print(df)
while True:
    item_name=str(input("Enter the item:"))
    item_name=item_name.title()
   # print(item_name)
    unit_price=fruits[item_name]
  #  print(unit_price)
    item_quantity=float(input("Enter the quantity:"))
    item_price=unit_price*item_quantity
    cart.update({item_name:item_price})
    ch=input("Do you like to continue shopping(y|n)")
    if(ch.lower()=="n"):
        break
print(cart)
total=0
del_option= input("Do you want home delivery(y|n):")
for i in cart:
   # print(cart[i])
    total+=cart[i]
if(total<500):
    disc=(5/100)*total
    net_total=total-disc
    print(f"Total= {net_total}")
else:
    disc=(10/100)*total
    net_total=total-disc
    print(f"Total= {net_total}")
if(del_option.lower()=="y"):
    print(f"Total amount to be paid including delivery charge {net_total+50}")
else:
    print(f"Total amount to be paid {net_total}")
