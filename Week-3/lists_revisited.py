#!/usr/bin/env python3

myFavouriteFruits = ["grapes","apple","mango","oranges","guava"]

for fruit in myFavouriteFruits:
    print(fruit)

print(len(myFavouriteFruits))

friends = ["Fred","Mark","Ted","Racheal","Ben"]
print(friends)
friends[0] = "Jim"
print(friends)
print("-----------------------------------------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)