import random


print("Welcome to the PYPassword Generator")
letter = int(input("How many letters would you like? "))
number = int(input("How many numbers would you like? "))
symbol = int(input("how man symbols would you like? "))



letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]   #!problem how do i get the chosen random passwords to be in a random place 
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*"]

password= []
for letter in range(0,letter):       # !cant append a string 
    password.append(random.choice(letters))
    
for number in range(0, number):
    password.append(random.choice(numbers))
    
    
for symbol in range(0, symbol ):
    password.append(random.choice(symbols))
print(password)

random.shuffle(password)

passwordString = ""
for char in password:
    passwordString += char
print(passwordString)