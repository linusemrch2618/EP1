import random

vmax=int(input("Maximum number: "))
number=random.randint(0,vmax)
guess=int(input("Guess a number: "))
diff=abs(guess-number)

for i in range(10):
    if guess<number:
        guess=int(input(f"Too low. Left trials: {9-i}\n    Try again: "))
        continue
    elif guess>number:
        guess=int(input(f"Too high. Left trials: {9-i}\n    Try again: "))
        continue
    elif guess==number:
        break
if guess==number:
    print("Correct!")
else:
    print("Game over!")