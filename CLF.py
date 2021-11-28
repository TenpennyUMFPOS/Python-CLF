import random

n=int(input("1 : Single Player \n 2 : MultiPlayer \n"))


if n==1:
    pun=input("1=Pair or 2=unpair \n")
    playerChoice=int(input("chose a number between 0 and 10 \n"))
    print("Your choice",playerChoice)
    ComputerChoice=random.randint(0,10)
    print(ComputerChoice)
    if ((playerChoice+int(ComputerChoice))%2==0)and(int(pun)==1):
        print("Winner")
    else:
        print("Loser")

elif n==2:
    Player1pun=input("1=Pair or 2 Unpair \n")

    Player1Choice=int(input(" PLayer 1 Chose a number between 0 and 10 \n"))
    Plyaer2Choice=int(input(" PLayer 2 Chose a number between 0 and 10 \n"))
    print(Player1Choice)
    print(Plyaer2Choice)

    if ((Player1Choice+Plyaer2Choice)%2==0)and (int(Player1pun)==1):
        print("Player 1 has won")
    else : 
        print("Player 2 has won")    
    
    
    

