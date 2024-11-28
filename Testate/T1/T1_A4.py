import random
roll = [0,0]
while sum(roll) != 7:
    roll = [random.randint(1,6) for _ in range(2)]
    print(f"Es wurde {roll[0]} und {roll[1]} gewürfelt.")