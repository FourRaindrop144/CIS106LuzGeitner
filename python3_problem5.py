#input phase
fixedCost = float(input("Enter fixed cost: "))
pricePerUnit = float(input("Enter price per unit: "))
costPerUnit = float(input("Enter cost per unit: "))
#process phase
breakevenPoint = fixedCost / (pricePerUnit - costPerUnit)
#output phase
print("The breakeven point is: ", breakevenPoint)
