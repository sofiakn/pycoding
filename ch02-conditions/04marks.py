'''
ask score of 3 subjects (ln 7-9), add scores (ln 11), 
calculate percentage based on max score = 100 (ln 13)
if percentage is less than 50, show fail
if percentage is greater than 80, show pass with reward, otherwise show pass
'''

scoreOne = int(input("What is scoreOne? "))
scoreTwo = int(input("What is scoreTwo? "))
scoreThree = int(input("What is scoreThree? "))

totalScore = scoreOne + scoreTwo + scoreThree

percentage = totalScore / 300 * 100

if percentage < 50:
    print("Failed")
elif percentage > 80:
    print("Passed with reward")
else:
    print("Passed")

print(percentage)