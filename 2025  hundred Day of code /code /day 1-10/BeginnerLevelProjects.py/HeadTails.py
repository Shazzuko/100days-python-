import random #  random.randint(a,b) give you a random number between a-b

headTails = random.random() *2
print(headTails)
if headTails >= 1:
    print("tails")
else:
    print("Heads")