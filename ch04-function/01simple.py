name = input("Enter your name: ")
print("Welcome", name)
print("-------------")

number = int(input("Enter a number for table (0 to exit): "))
while number != 0:
    print("-------------")
    for count in range(1,11):
        print(f"{number} x {count} = {count * number}")
    print("-------------")
    number = int(input("Enter a number for table (0 to exit): "))

print("-------------")
print("Thank you")
