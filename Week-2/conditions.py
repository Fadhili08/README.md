age  = 24 
gender = " male"

if (age < 16) :
    print("You are still young")
else: 
    print("You should get an id")

#compound /multiplle conditions 

if ((age > 30) & (gender == "male")):
    print("You might qualify for a loan ")
else:
    print("No loan for you")

fav_colour = "Blue"
age = 22 
if(fav_colour == "Blue") | (age <= 20):
    print("Happy birthday to you")
else:
    print(" No birthday for you")