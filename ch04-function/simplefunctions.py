# Draws a line
def line():
    print("-------------")
    
def readNonEmptyString(messageString):
    result = input(messageString)
    while result == "":
        result = input(messageString)
    return result
