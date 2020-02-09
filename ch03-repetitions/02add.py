#ask for 2 numbers, show sum, repeat process till the first number entered is 0, then stop execution.
from _ast import If

firstNumber = int(input("Enter first number (0 to stop): "))


while firstNumber != 0:
    secondNumber = int(input("Enter second number: "))
    result = (firstNumber + secondNumber)
    print(f"The sum of {firstNumber} and {secondNumber} is {result}")
    print()
    firstNumber = int(input("Enter first number (0 to stop): "))
print("byebye")