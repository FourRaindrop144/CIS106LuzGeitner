#input phase
firstName = input("Enter your first name: ")
stepsWalked = input("Enter the number of steps you walked today: ")
#process phase
caloriesBurned = int(stepsWalked) * 0.25
#output phase
print(firstName + ", you have burned " + str(caloriesBurned) + " calories today." )  