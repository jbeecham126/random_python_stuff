import random as r
import time

def dice():
    player = r.randint(1, 6)
    print("YOU ROLL...")
    time.sleep(2)
    print("YOU ROLLED " + str(player))

    ai = r.randint(1, 6)
    print("COMPUTER ROLLS...")
    time.sleep(2)
    print("COMPUTER ROLLED " + str(ai))

    if player > ai:
        print("YOU WIN")
    elif player == ai:
        print("TIE")
    else:
        print("COMPUTER WINS")

    print("QUIT? Y/N")
    reset = input()

    if reset == "Y" or reset == "y":
        exit()
    elif reset == "N" or reset == "n":
        pass
    else:
        print("I DID NOT UNDERSTAND THAT. PLAYING AGAIN.")

while True:
    print("PRESS ENTER TO ROLL YOUR DIE.")
    roll = input()
    dice()
