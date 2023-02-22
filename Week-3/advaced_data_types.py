#advanced data types

#Mutable VSimmutable

#Mutable are data types that can change during progrom life cycle 
#add/ remove elements 
#Immutable--> data types that can't be edited 

#1 list (mutable)

friends = ["Jeff","Norm" , "Anita" , "Jesse" , "Nicole"]
#or friends 
#add --> append(), extend()
#remove--> pop()

Students = ["Victor", "Dave", "Mike"]

friends.extend(Students)
friends.append("victor")
friends.reverse()
# 2) Tuples (immutable)
#types of list that are immutable 

stationaries = ("pens", "ink","sharpener",)

#replace the whole tuple
stationaries = ("ruler", "clip board", "eraser")


for stationary in  stationaries:
    print(stationary)

numbers = (1,2,3,4,5,6,7,76,89,)

#3) Dictionaries aka dict 

#uses a key and a value pair to store data 

Student = {"Name": "Alvin", "age":18 , "gender": "Male", "height" :"is_tall "}
print(Student["Name"])
print(Student["age"])
print(Student["gender"])
print(Student["height"])

Friend = {"Fav_color": "Yellow", "hobbies": "dancing , singing", "course": "driving" , "weight":70 , "height":190}
print(Friend["Fav_color"])
print(Friend["hobbies"])
print(Friend["course"])
print(Friend["weight"])
print(Friend["height"])
print(Student.values())
print (Student.keys())