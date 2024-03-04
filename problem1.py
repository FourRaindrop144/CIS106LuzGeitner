#input phase
stockSymbol = input("Enter stock symbol")
shares = float(input("Enter number of shares"))
purchasePrice = float(input("Enter purchase price per share"))
#process phase
amountInvested = shares * purchasePrice
#output phase
print("Amount invested $", amountInvested)