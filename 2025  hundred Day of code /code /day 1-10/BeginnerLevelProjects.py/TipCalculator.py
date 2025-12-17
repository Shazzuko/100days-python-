print("Welcome to the tip Calculator")
tMoney = input("How much was the bill?")
precentTip = input("How much would you like to tip 10, 12, 15? ")
NumPeople = input("How many people will split the bill? ")

finalTip = int(precentTip) / 100 

finalBill = int(tMoney) + finalTip
moneyPerPerson = finalBill / int(NumPeople)
print(moneyPerPerson)