import random as r

random = r.randint(1, 100)
print("GUESS A NUMBER BETWEEN 1 AND 100: ")
while True:
    guess = int(input())
    if guess > random:
        print("TOO HIGH")
    elif guess < random:
        print("TOO LOW")
    else:
        print("YOU WIN")
        break
