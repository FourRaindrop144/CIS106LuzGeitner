#input phase
mealTotal = float(input("Enter the total for the meal: "))
#process phase
tip15 = mealTotal * 0.15
tip18 = mealTotal * 0.18
tip20 = mealTotal * 0.20
total15 = mealTotal + tip15
total18 = mealTotal + tip18
total20 = mealTotal + tip20
#output phase
print("The total for a 15% tip is: ", total15)
print("The total for a 18% tip is: ", total18)
print("The total for a 20% tip is: ", total20)
