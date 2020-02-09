number = int( input("Enter a number for times table (0 to stop): "))
while number != 0 :
    print(f"{number} x 1 = {number*1}")
    print(f"{number} x 2 = {number*2}")
    print(f"{number} x 3 = {number*3}")
    print()
    number = int( input("Enter a number for times table (0 to stop): "))
print("Thank you for using this program.")