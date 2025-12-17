print("Welcome to Treasure Island!")
print("Your Mission is to find the Treasure!")

Drec1= input("you enter a last mask and two doors appear before you the left door being made of steel and the right door made out of bamboo. left or right ? ")

if Drec1 == "right":
    print("Dead End!")
elif Drec1 == "left":
    Drec2 = input("entering the door you see a river with hungry alligators do you swim or wait? ")
    if Drec2 == "swim":
         print("Dead End")
    elif Drec2 == "wait":
        Drec3 = input("the building catches on fire you start seeing 4 different color yellow, red, blue, black? ")
        if Drec3 == "yellow":
            print("You have Excaped!")
        elif Drec3 == "red" or "blue" or "black":
            print("Game Over")
    


