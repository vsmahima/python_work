#type of triangle

first = int(input("Enter the measurement of first side:"))
second = int(input("Enter the measurement of second side:"))
third = int(input("Enter the measurement of second side:"))
if(first==second and second==third):
    print(f"{first},{second},{third} sides of the tringles are same and is equilateral traingle")
elif(first!=second and first!=third and second!=third):
    print(f"{first},{second},{third} sides of the tringles are different and is scalene traingle")
else:
    print(f"{first},{second},{third} two sides of the tringles are equal and is isosceless traingle")
    



