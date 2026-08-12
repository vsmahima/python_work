#loan eligibility

min_credit_score=700
min_salary=25000
min_age=21
age = int(input("Enter your age:"))
credit_score = int(input("Enter your credit score:"))
salary =int(input("Enter your net salary:"))
if(age>=min_age and salary>=min_salary and credit_score>=min_credit_score):
    print("You are eligible for applying loans")
else:
    print("You are not eligible, please check the eligibilty criteria")