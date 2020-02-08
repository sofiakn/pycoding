'''
ask score of 3 subjects, add scores, calculate percentage based on max score = 100
if percentage is less than 50, show fail
if percentage is greater than 80, show pass with reward, otherwise show pass
'''

scoreOne = int(input("What is scoreOne?"))

if scoreOne < 50:
    print("Failed")
elif scoreOne > 80:
    print("Passed with reward")
else:
    print("Passed")
    
print()

scoreTwo = int(input("What is scoreTwo?"))

if scoreTwo < 50:
    print("Failed")
elif scoreTwo > 80:
    print("Passed with reward")
else:
    print("Passed")
    
print()
    
scoreThree = int(input("What is scoreThree?"))

if scoreThree < 50:
    print("Failed")
elif scoreThree > 80:
    print("Passed with reward")
else:
    print("Passed")    
    
