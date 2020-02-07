# Ask for the price and if price is dollar or more, there will be tax otherwise no tax is charged

price = float(input("What is the \"price\"? "))

if price >= 1.0 :
    print("You will be charged tax")
else :
    print("You will not be charged tax")

