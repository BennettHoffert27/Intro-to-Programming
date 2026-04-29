import random
x = random.randint(1, 100 )
y = 0
while x != y:
    y = int(input("Geuss the number!"))
    if y < x:
        print("too low.")
    elif y > x:
        print("too high.")

    elif y == x:
        break


print("You win! 67676767676767676767676767!!!")
    