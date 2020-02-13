# line() displays a line followed by message.
def line(message):
    print("-------------", message)
    
def read():
    return int(input("Enter a number for table (0 to exit): "))

name = input("Enter your name: ")
print("Welcome", name)
line("Welcome message displayed.")

number = read()
while number != 0:
    line(f"{number} read as keyboard input.")
    for count in range(1,11):
        #print(f"{number} x {count} = {count * number}")
        print("%d x %d = %d"%(number, count, count * number))
    line("table displayed.")
    number = read()

line("A ZERO was enterred to end this program")
print("Thank you")
