fruits = ["apple", "banana", "orange", "blueberry", "strawberry"]
print(fruits)
print(fruits[0])
print(fruits[4])
add_to_fruits = input("Add another fruit.")
fruits.append(add_to_fruits)
print(fruits)
remove_from_fruits = input("Remove a fruit.")
if remove_from_fruits == "apple":
    fruits.remove("apple")
elif remove_from_fruits == "banana":
    fruits.remove("banana")
elif remove_from_fruits == "orange":
    fruits.remove("orange")
elif remove_from_fruits == "blueberry":
    fruits.remove("blueberry")
elif remove_from_fruits == "strawberry":
    fruits.remove("strawberry")
print(fruits)


fruits.sort()
print(fruits)



fruits_two=["banana", "apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)