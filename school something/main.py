# #first_name = input("what is your first_name? ")
# #colour = input("What is your favorite color? ")
# #print(first_name + " like " + colour)
#
# #birth_year= input("Birth year: ")
# #print(type(birth_year))
# #age=2023- int(birth_year)
# #print(type(age))
# #print(age)
#
#
# # weight_pounds = input("what is your weight in punds? ")
# # weight_kilogram = int(weight_pounds) * 0.45
# # print(weight_kilogram)
# first = "John"
# last = "Smith"
# mesg= f"{first} [{last}] is a coder"
# print(mesg)

# course = "Python for begginers"
# print("Python" in course
# import math
# print()
# x=2.9
# print(abs(-2.9))
# house = 1000000
# A_credit= False
# if A_credit:
#     final_prize=int(house)*0.9
#
# else:
#     final_prize=int(house)*0.8
#
# print(f"Down payment: ${final_prize}")

# has_high_income= True
# has_good_credit= True
#
# if has_high_income and has_good_credit

# has_good_credit= True
# has_criminal_rcord= False
#
# if has_good_credit and not has_criminal_rcord:
#     print("oke")

# temperature=15
#
# if temperature>=29:
#     print("iT is a hot day")
# elif temperature <=10:
#     print("It is cold day")
# elif 11 < temperature<18:
#     print("It is relative temperature")
# else:
#     print("It is good temperature")

# username=input("what is your nickname: ")
#
# if len(username) > 50:
#         print("Maximum range is 50 characters ")
# elif 3 > len(username):
#         print("Minimum range of characters is 3")
# else:
#         print("Name looks good!")


# print("Hi")
# weight=input("Weight: ")
# mesurment=input("(L)bs or (K)g: ")
#
# if mesurment.upper() =="L":
#     finish=int(weight)*0.45
#     print(f"You are {finish} kg. ")
#
# elif mesurment.upper()=="K":
#     finish=int(weight)/0.45
#     print(f"You are {finish} lb. ")
# else:
#     print("Stupid")

# i =1
# while i<=5:
#     print("*"*i)
#     i=i+1
# print("Done")

# secret_number=9
# guess_count=0
# guess_limit=3
#
# while guess_count < guess_limit:
#     guess=int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#         print("You won")
#         break
# else:
#     print("Sorry you failed")
# command = ""
# started = False
#
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started=True
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "stop":
#         print("Car stopped")
#         if not started:
#             print("stupiid")
#         else:
#             print("Car has stopped ")
#     elif command == "quit":
#         break
#     else:
#         print("I dont understand.....type (help) for more.")

# prices= [10,20,30]
# total=0
# for price in prices:
#     total+=price
#print(f"Total:{total}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")


# numbers = [5,2,5,2,2]
# for i in numbers:
#     if i ==5:
#         print("xxxxx")
#     elif i == 2:
#         print("xx")
#     else:
#         break

# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# first_name = ["John", "Bob", "Mosh", "Sarah", "Mary"]
# first_name[0]= "Jon"
# print(first_name[2:])
# number = [3,6,2,8,4,10]
# max = number[0]
# for i in number:
#     if i > max:
#         max = i
#
# print(max)
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# numbers


# numbers= [5,2,1,7,4]
# number2 = numbers.copy()
# numbers.append(10)
# print(numbers)

# numbers = [10,21,25,26,25,20,30,20,2,35,53,696,62,52,589,596,6,10]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# coordinates = [1,2,3]
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]

# x,y,z = coordinates

# customer={
# "first_name": "John Smith",
# "age": 30,
# "is_verified": True
# }
# customer["first_name"] = "JAck Smith"
# print(customer.get("first_name"))


# numbers={
#     "1": "One ",
#     "2": "Two ",
#     "3": "Three "
# }
# phone = input("Phone: ")

# output = ""
# for ch in phone:
#     output += numbers.get(ch,"!") + " "
# print(output)
    
# message = input(">")
# words = message.split(" ")
# emojis={
#     ":)": "😀",
#     ":(" :"😞",

# }
# output= ""
# for word in words:
#    output+= emojis.get(word, word ) + " "

# print(output)


# def greet_user():
#     print("Hi there!")
#     print("Welcome aboard")


# print("start")
# greet_user()
# print("Finish")
# import tkinter, random
# c=tkinter.Canvas(width=500,height=500)
# c.pack()
# x,y=50,200

# for i in range(10):
#     posun_x=random.randint(10,40)
#     posun_y=random.randint(10,40)
#     c.create_rectangle(x,y,x+posun_x,y+posun_y)
#     x = x + posun_x
    
# def square(number):
#     return number*number
    

# print(square(3))

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis={
#         ":)": "😀",
#         ":(" :"😞",

#     }
#     output= ""
#     for word in words:
#         output+= emojis.get(word, word ) + " "
#     return output


# message=input(">")
# print(emoji_converter(message))


# try:
#     age= int(input("Age: "))
#     income=2000
#     risk=income/ age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannoct be 0")
# except ValueError:
#     print("Invalid value")

# class Point:
#     def __init__(self,x,y) -> None:
#         pass
#         self.x =x
#         self.y =y
#         pass
#     def move():
#         print("move")
    
#     def draw():
#         print("draw")


# point = Point(10,20)
# point.x  11
# print(point.x)


# class Person:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(f"{self.name} is talking")


# john = Person("John Smith")
# john.talk()
#prečo akože davam print john.name ked akože...ked len print(john) potrebujem ta na čo 
# vyuzijem toto druhe 
# print(john.name)
# john.talk()
# # tomu poslednemu chapem len toto self čo znamena nechapem


# # no to class to vytváraš objekt , máš napr. Person 
# # prvá funkcia v classe je __init__ to sa volá konštruktor.. tam sa definuje aké atribúty má daná classa ( konštruktorov môže byť viacero) 
# # a to že tam je to self. tak to znamená že sa jedná priamo o nejaký atribút tej classy, tam ako je že self.name tak upravuješ atribút name classy Person, 
# # keby si mal niekde v objekte Person funkciu napr. zmen meno(name)
# # tak vútri funkcie použiješ self.name = name na to aby si “updatol” atribút name classy Person

# # potom môžeš používať napr. v kóde že vytvoríš classu a chceš napr. len jej meno,adresu hocičo … tak dáš john.address a ono zoberie classu john , 
# # a vvytiahne z nej len atribút address
# john= Person("John Smith")
# #prečo akože davam print john.name ked akože...ked len print(john) potrebujem ta na čo 
# # vyuzijem toto druhe 
# print(john.name)
# john.talk()
# # tomu poslednemu chapem len toto self čo znamena nechapem

# class Person:
    # def __init__(self, name) -> None:
#         self.name = name
        
#     def talk (self):
#         print (f"Hi, I am {self.name}")


# john = Person ("John Smith")

# print(john.name)

# john.talk()


import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()


root.title("Unit Converter")
def start():
    greeting = tk. Label (text="Hello world",
                      fg="white",
                      bg="light blue",
                      width=50,
                      height=70)
    button = tk.Button(
        text="click on me! ",
        width=25,
        height=10,
        bg="yellow",
        fg="blue"
                        )
    
    entry = tk.Entry(fg="yellow", bg="blue", width=50)

    entry.pack()
    greeting.pack()
    button.pack()
start()
root.mainloop()
