
# *********** This program is a game that we played in our chilhood (snake-water-gun game ) *******



import random

def game(compu, you):
    if compu == you:
        return None
    elif compu == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif compu == 'w':
        if you == 's' :
            return True
        elif you == 'g':
            return False
    elif compu == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True      

print("Computer turn : snake(s) or water(w) or gun(g) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    compu = 's'
elif randNo == 2:
    compu = 'w'
elif randNo == 3:
    compu = 'g'

you = input("Your turn : snake(s) or water(w) or gun(g) : ")
a = game(compu, you)

print(f"Computer choose {compu}")
print(f"You choose {you}")

if a == None:
    print("GAME TIE !")
elif a:
    print("YOU WIN!")
else :
    print("YOU LOSE!")
