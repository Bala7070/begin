#variables
#age = 21
#print(f"you are {age} years old")
#print()

#loops
#for

#for x in range(1,11):
#    print(x)

#for x in reversed(range(1,11)):
#    print(x)

#credit_card= "1234-5678-9123-4567"
#for x in credit_card:
 #   print(x)

# break and continue

#for x in range(1,21):
   #     break
   # else:
    #    print(x)

#for x in range(1,21):
 #   if x==13:
  #      continue
   # else:
    #    print(x)

#While loop

# name=input("enter your name:")
# age=int(input("enter your age"))
# while name=="":
#     print("you didnt enter your name")
#     name=input("enter your name:")
#     print(f"hello {name}") 

# while age<0:
#     print("age cant be negative")
#     age=int(input("enter your age"))
#     print(f"your age is:{age}") 

#logical operators

# food = input("enter food you like(q to quit):")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("enter food you like(q to quit):")
#     print("bye")

# num = int(input("enter a number between 1-10"))
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("enter a number between 1-10"))
#     print(f"your num is {num}")

#Nested loop

# for x in range(3):
#     for y in range(1,10):
#         print(y, end=" ")
#     print()

#rectangele

# rows = int(input("enter no of rows"))
# coloumns = int(input("enter no of coloumns"))
# symbol = input("enter the symbol")

# for x in range(rows):
#     for y in range(coloumns):
#         print(symbol, end="")
#     print()

#Functions 

# def happy_birthday(name,age):
#     print(f"happy birthday to {name}")
#     print(f"your are {age} years old")
#     print("happy birthday to you")
#     print()

# happy_birthday("bala",32)
# happy_birthday("hani", 52)


# def display_invoice(username , amount, due_date):
#     print(f"hello {username}")
#     print(f"your amount is ${amount:.2f} is due:{due_date}")
    
# display_invoice("balabandaru", 2000, "25/10")
# display_invoice("krishna", 250.31, "15/10")

# def cerate_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name = cerate_name("bala", "bandaru")
# print(full_name)

#collection: list, set,tuple

#fruit = "apple"

#List

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

#fruits[1] = "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("apple"))
# print(fruits.count("apple"))
# print(fruits)

# for fruit in fruits:
#      print(fruit)



#dictionaries

capitals = {"india" : "new delhi", "usa" : "washington dc", 
            "russia":"moscow", "Japan" : "tokyo"}
#print(capitals.get("china"))

# if capitals.get("Japan"):
#     print("The capital exists")
# else:
#     print("that capital doesnt exist")

#capitals.update({"germany" : "berlin"})
#capitals.update({"usa" : "detroitte"})
#capitals.pop("Japan")
#capitals.popitem()
#capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():

#     print(key)

# values = capitals.values()
#  print(values)

# for value in capitals.values():
#     print(value)

items = capitals.items()
# print(items)

for key,value in capitals.items():

    print(f"{key} : {value}")

