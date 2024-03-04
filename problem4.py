#input phase
carMake = input("Enter the make of the car: ")
carModel = input("Enter the model of the car: ")
msrp = float(input("Enter the MSRP of the car: "))
discountPercent = float(input("Enter the discount percent: "))
#process phase
amountOff = msrp * discountPercent
discountPrice = msrp - amountOff
#output phase
print("Make: ", carMake)
print("Model: ", carModel)
print("MSRP: $", format(msrp, ',.2f'))
print("Discount Percent: ", format(discountPercent, '.0%'))
print("Amount Off: $", format(amountOff, ',.2f'))
print("Discount Price: $", format(discountPrice, ',.2f'))
