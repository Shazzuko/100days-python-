

print("Are you tall enough to ride the rollercoaster ")
height = input("how tall are you in Cm? ")
if int(height) >= 120: 
    age =input("how old are you? ")
    if int(age) < 18:
        print("sorry you to yonug to ride!")
    else:
        print("enjoy the ride!")
else: 
    print("sorry maybe next time!")