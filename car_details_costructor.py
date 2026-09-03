#Create a car details using constructor and print the car information
class Car:
    def __init__(self,name,manufacturer,mode,fueltype):
        self.name=name
        self.manufacturer=manufacturer
        self.model=mode
        self.fueltype=fueltype
        pass
    def car_details(self):
        print(f"Car Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Mode: {self.model}")
        print(f"Fuel Type: {self.fueltype}")
cname= input("Enter car name: ")
cmanufacturer=input("Enter Manufacturer: ")
cmode=input("Enter model: ")
cfuel=input("Enter fuel type: ")
car_obj=Car(cname,cmanufacturer,cmode,cfuel)
car_obj.car_details()