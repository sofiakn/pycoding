
mathScore = int(input("What is your math's score? "))

if mathScore > 90:
    print("Excellent")
elif mathScore > 70:
    print("Good")
elif mathScore > 50:
    print("Need improvement")
else:
    print("What the heck")

# Logical Error (or a bug in the code)
if mathScore > 50:
    print("Need improvement")
elif mathScore > 70:
    print("Good")
elif mathScore > 90:
    print("Excellent")
else:
    print("What the heck")
