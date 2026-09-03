#Create a mobile details storing using constructor and display mobile detials
class Mobile:
    def __init__(self,name,version,price):
        self.name=name
        self.version=version
        self.price=price
        pass
    def mobile_details(self):
        print(f"Mobile Name: {self.name}")
        print(f"Mobile Version: {self.version}")
        print(f"Price: {self.price}")
m_name=input(f"Enter mobile Name: ")
m_version=input("Enter mobile version: ")
m_price= int(input("Enter price: "))
mobj=Mobile(m_name,m_version,m_price)
mobj.mobile_details()