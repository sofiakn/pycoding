
year = int(input("What is your birth year? "))
age = 2020 - year

print(f"You will be {age} years old by Dec 31.")

if age > 17:
    print("You are an adult.")
else:
    print("You are a minor.")
