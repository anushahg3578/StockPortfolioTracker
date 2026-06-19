dic = {"AAPL":180,"TSLA":250,"GOOG":200,"MSFT":240,"AMZN":185} 
total_investment = 0   # to store overall total

while True:
    stock_name = input("Enter Stock name: ").upper()
    stock_quantity = int(input("Enter the quantity of the stock: "))
    if stock_name in dic:
        value = dic[stock_name] * stock_quantity
        print("Investment for", stock_name, "is:", value)
        total_investment = total_investment + value   # adding to total
    else:
        print("Stock not found")

    choice = input("Do you want to add another stock? (yes/no): ").lower()
    
    if choice != "yes":
        break   # stop loop

print("Total Investment:", total_investment)
       
 