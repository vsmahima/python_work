#Stone,paper,Scissor
import random
print("Welcome to Stone, Paper, Scissor Game")
print("Game Rules")
print("""
        Scissor->Stone,Stone win
        Scissor->paper, Scissor win
        Stone->paper, paper win
        """)
user_point=0
sys_point=0
option=["stone","paper","scissor"]
while True:
    user_choice=input("Enter user choice: ")
    sys_choice=random.choice(option)
    print(f"System choice: {sys_choice}")
    if(user_choice==sys_choice):
        print("It's a tie")
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="scissor" and sys_choice=="stone"):
        sys_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="stone" and sys_choice=="scissor"):
        user_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="paper" and sys_choice=="scissor"):
        sys_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="scissor" and sys_choice=="paper"):
        user_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="stone" and sys_choice=="paper"):
        sys_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    elif(user_choice=="paper" and sys_choice=="stone"):
        user_point+=5
        print(f"User Score: {user_point},System Score: {sys_point}")
    else:
        print("please check the choice")
    if(user_point==25 or sys_point==25):
        break
if(user_point==25):
    print("You won the game")
else:
    print("System won the game")
print("Final Score")
print(f"User score={user_point},System score={sys_point}")    