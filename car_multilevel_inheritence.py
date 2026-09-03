#Create a multilevel inheritence vehicle system, where 
#vehicle contain brand details,
#car adds model information and Electriccar adds battery capacity details.4
class Vehicles:
    def __init__(self,brand_name,nation,estd_year):
        self.brand_name=brand_name
        self.nation=nation
        self.estd_year=estd_year
    def display(self):
        print(f"Brand Name: {self.brand_name}")
        print(f"Nation of origin: {self.nation}")
        print(f"Established Year: {self.estd_year}")
class Car(Vehicles):
    def __init__(self, brand_name, nation, estd_year,model_name,variant_name,color):
        super().__init__(brand_name, nation, estd_year)
        self.model_name=model_name
        self.variant_name=variant_name
        self.color=color
    def display(self):
        super().display()
        print(f"Model Name: {self.model_name}")
        print(f"Varainat Name: {self.variant_name}")
        print(f"Color: {self.color}")
class ElectricCar(Car):
    def __init__(self,brand_name, nation, estd_year,model_name,variant_name,color,battery_capacity,price):
        super().__init__(brand_name, nation, estd_year,model_name,variant_name,color)
        self.battery_capacity=battery_capacity
        self.price=price    
    def display(self):
        super().display()
        print(f"Battery Capacity: {self.battery_capacity}")
        print(f"Price: {self.price}")
obj = ElectricCar('Tata','India','1945','punch','smart','Red','30kwh',1000000)
obj.display()
        
        

        