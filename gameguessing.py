import random 
print("number guessing game")
number=random.randint(1,9)
chances=0
print("guess a number between 1 to 9")
# while loop to give 5 chance 
while chances < 5:
    guess = int(input("enter your guess:"))

    if guess == number :
         print("you won the number")

    elif guess <number :
        print ("your guess is to low")

    else :
        print ("your guess is to high")
    chances+=1   

if not chnaces < 5 :
    print ("that you lose the game")        