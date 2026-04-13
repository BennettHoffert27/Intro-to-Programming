speed = float(input("Speed? "))

if speed < 74:
    print("Tropical Storm")
elif speed >= 74 and speed < 96:
    print("Category 1")
elif speed >= 96 and speed < 111:
    print("Category 2")
elif speed >=111 and speed < 130:
    print("Category 3")
elif speed >= 130 and speed < 157:
    print("Category 4")
else:
    print("Category 5")

