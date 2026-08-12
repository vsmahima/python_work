def fizz_buzz(num):
    if(num%3==0 and num%5==0):
        print("FIZZBUZZ...")
    elif(num%3==0):
        print("FIZZ....")
    elif(num%5==0):
        print("BUZZ.....")
    else:
        print("Wrong choice of number")

num=int(input("Enter the number:"))
#calling function to print Fizz bizz
fizz_buzz(num)