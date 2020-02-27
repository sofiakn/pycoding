
# Draws a line
def line():
    print("-------------")
    
def readNonEmptyString(messageString):
    result = input(messageString)
    while result == "":
        result = input(messageString)
    return result

name = readNonEmptyString("Enter your name: ")
print("Welcome", name)
line()

number = int(input("Enter a number for table (0 to exit): "))
while number != 0:
    line()
    for count in range(1,11):
        print(f"{number} x {count} = {count * number}")
    line()
    number = int(input("Enter a number for table (0 to exit): "))

line()
print("Thank you")
