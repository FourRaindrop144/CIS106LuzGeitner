#input phase
sharePrice = float(input("Enter the share price: "))
stockPrice = float(input("Enter the stock price: "))
stockQuantity = float(input("Enter the stock quantity: "))
#process phase
newStockPrice = stockPrice - sharePrice
stockValue = newStockPrice * stockQuantity
#output phase
print("The new stock price is: ", newStockPrice)
print("The stock value is: ", stockValue)
