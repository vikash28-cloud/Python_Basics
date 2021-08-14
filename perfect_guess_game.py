import random
randNumber = random.randint(1,100)

userguess = None
guesses = 0

while(userguess !=randNumber):
    userguess = int(input("enter your guess: "))
    guesses+=1
    if (userguess == randNumber):
        print("you win")
    elif userguess>randNumber:
        print("too high")
    elif userguess<randNumber:
        print("too low")
        
    
print(f"you guessed in {guesses} guesses")
   