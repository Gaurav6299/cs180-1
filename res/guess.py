# Practice 6
# Guess the number
import random
a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
x=random.randrange(a,b)
i=1
n=6
while i<=n:
    guess=int(input("Enter guess the number for player1\n"))
    if(x<guess):
        print("Wrong choice! Please enter smaller number")
        print(f"you have remaining {n-i} chance out of {n} chances\n")
        i +=1

    elif(x>guess):
        print("Wrong choice!Please enter greater number")
        print(f"you have remaining { n - i} chance out of {n} chances\n")

        i +=1

    elif(x==guess):
        print("correct guess")
        player1=i
        print(f"you  guess the number in {player1} chances out of {n} chances\n")
        break
x=random.randrange(a,b)
j=0
while j<=n:
    guess2=int(input("Enter guess the number for player2\n"))
    if(x<guess2):
        print("Wrong choice! Please enter smaller number")
        print(f"you have remaining {n-j} chances out of {n} chances\n")
        j +=1
    elif(x>guess2):
        print("Wrong choice! Please enter greater number ")
        print(f"you have remaining {n-j} chances out of {n} chances\n")
        j +=1

    elif(x==guess2):
        print("correct choice")
        player2=j
        print(f"you took {j} chances to guess the number out of {n} chances\n")
        break

if player1>player2:
    print("Player2 is won the match")

if player2>player1:
    print("player1 is won the match")

if player1==player2:
    print("Both player games becomes tie")



