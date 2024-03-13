#input phase
examOne = int(input("Enter score for exam one: "))
examTwo = int(input("Enter score for exam two: "))
weightExamOne = int(input("Enter weight for exam one: "))
weightExamTwo = int(input("Enter weight for exam two: "))
#processing phase
examOneWeighted = examOne * weightExamOne
examTwoWeighted = examTwo * weightExamTwo
totalWeighted = examOneWeighted + examTwoWeighted
#output phase
print("The total weighted score is: ", totalWeighted)