#!/usr/bin/env python3

print("Welcome to this script")

name= input("What is your name?") 


print("Hi", name, "all questions are yes or no...")
print("All questions require an answer")

sch= input("Do you like school?")


if sch == "yes":
    print("Good job", name, "!")

elif sch == "no":
    print("Hit the books,", name, " they don't hit back!")
#elif sch:
    print("The directions said to answer 'yes' or 'no'...")
    print(name, "You suck!")    
        
else:
    print("You don't read so good", name)
#   ss= input("Try again... Do you like School?")
#   if ss.lower == "yes":
#       print("Gold star for you!")
#   if ss.lower == "no":
#        print("Good for you!")
#    elif:
#        print("You failed the test")
#    else:
#        print("You failed the test")

