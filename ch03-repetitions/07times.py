# Ask for a number and show times table from 1 to 10

num = int(input("Enter a number (0 to stop): "))
while num != 0:
    for number in range(1, 11):
        print(f"{num} x {number} = {num*number}")
    
    print()
    num = int(input("Enter a number (0 to stop): "))
print("Thanks")