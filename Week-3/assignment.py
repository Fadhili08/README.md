favourite_musicians =[ ]
#using a for loop add 7 new musicians 
#copy the list to a new list clled musicians 
#sort the list 
#Pop out 2 celebrities from the list 
#Count the remaining celebrities in the list 

fav_musicians = []

#using for loop add five new musicians
print("Enter five names of your favourite musicians:")
for musician in range(0,5):
    the_musicians = input("Enter name:")
    fav_musicians.append(the_musicians)
print(fav_musicians)

#copy the list to a new list called celebs 
celebs = fav_musicians.copy()
print(celebs)

#sort the list
celebs.sort()
print(celebs)

#pop out two celebrities
celebs.pop()
celebs.pop()
print(celebs)

#count the remaining celebrities in the list
print(len(celebs))