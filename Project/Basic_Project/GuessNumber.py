import random

limitNumber = int(input("Set your limit number: "))

def guessNumber(x):
    randomNumber = random.randint(1,x)
    guess = 0

    print("Guessing Number: {}".format(randomNumber))

    while(guess != randomNumber):
        guess = int(input("Guess the number between 1 and {}: ".format(x)))
        if(guess < randomNumber):
            print("Its Too Low")
        elif(guess > randomNumber):
            print("Its Too High")

    print("Yeay Congrats, u deserve it!")

def guessNumberRobot(x):
    low = 0
    high = x
    randomNumber = random.randint(1,x)
    guess = 0

    print("Guessing Number: {}\n".format(randomNumber))

    while(guess != randomNumber):
        guess = random.randint(low,high)
        print("Robot Guess: {}".format(guess))
        if(guess < randomNumber):
            print("Its Too Low")
            low = guess+1
        elif(guess > randomNumber):
            print("Its Too High")
            high = guess-1

    print("Yeay Congrats, u deserve it!")


guessNumberRobot(limitNumber)