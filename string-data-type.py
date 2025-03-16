#Exercicio 1
mystring = "This is a string"
print(mystring)
print(type(mystring))
print(mystring + " is of the data type " + str(type(mystring)))
#Exercicio 2
firststring = "water"
secondstring = "fall"
trirdstring = firststring + secondstring
print(trirdstring)
#Exercicio 3
name = input("What is yout name?: ")
print(name)
#Exercicio 4
color = input("Whats is your favorite color?: ")
animal = input("Whats is your favorite animal: ")
print("seu animal preferido é " + animal + ", sua cor preferida é " + color)
print("{}, you like a {} {}!".format(name, color, animal))