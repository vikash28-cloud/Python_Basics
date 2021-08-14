#   ---------    snake, water and gun game    ---------/
import random
print = (input("computer turn: snake(s) water(w) gun(g)"))
ai  = random.randint(1,3)
if ai==1:
    comp = "s"
elif ai==2:
    comp = "w"
elif ai==3:
    comp = 'g'

you = input("your turn: snake(s) water(w) gun(g)")
if comp==you:
    print(None)
elif comp=='s':
    if you=='w':
        a="no"
    elif you== "g":
        a="yes"
elif comp == 'w':
    if you== 'g':
        a="no"
    elif you == 's':
        a="yes"
elif comp =='g':
    if you == 'w':
        a="yes"
    elif you=='s':
        a="no"

if None:
    print("draw")
elif a=="yes":
    print("you  win")
else :
    print("lose")
    
    
