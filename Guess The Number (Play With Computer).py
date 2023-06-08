import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number that is between 1 and {x}: "))
        if guess > random_number:
            print("Too high, try Again!")
        elif guess < random_number:
            print("Too low, try again!")   
        
    print(f"You got it right it's {random_number}")
i = int(input("Enter the highest range you want to play within. You wanna play between 1 and :  "))
guess(i)
