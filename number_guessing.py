import random

comp_guess = random.randint(1, 10)

limit = 0
score = 0

while limit < 3:
    try:
        user_guess = int(input("Enter a number between 1 to 10 : "))
        if(user_guess > 10 or user_guess < 0):
            print("Wrong input")
            limit = limit
    except:
        print("Please give correct input")

    if(comp_guess == user_guess):
        if(limit==0):
            score +=15
            break
        elif(limit==1):
            score +=10
            break
        elif(limit==2):
            score +=5
            break
        else:
            score = score
    elif(comp_guess > user_guess):
        print("Your Guess number is lower than my number")

    else:
        print("Your Guess number is greater than my number")

    limit +=1

if(limit>2):
    print("Your tried many times")
    print("My number was {}".format(comp_guess))
else:
    print("Congrulations!!! Your score is {}".format(score))



