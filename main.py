import random

computer = random.choice([-1,1,0])
youstr = input("Enter your choice : ")
youDict ={"s" :1 , "w" : -1, "g" : 0 }
reversDict = {1: "Snake", -1: "Water" , 0 : "Gun"}
you = youDict[youstr]


print (f"Your Choice {reversDict[you]}\n Computer Choice {reversDict[computer]}")

if computer == you :
    print("Game is Tai!..")

else:
    if computer == -1 and you == 1:
        print("You Win ! ")

    elif computer == 1 and you == -1:
        print("You Lost . ")

    elif computer == 0 and you == 1:
        print("You Lost . ")

    elif computer == -1 and you == 0:
        print("You Lost . ")

    elif computer == 1 and you == 0:
        print("You Win . ")

    elif computer == 0 and you == -1:
        print("You Win . ")

    else:
        print("Something was wrong !..")