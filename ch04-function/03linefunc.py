'''
+--------------+
| Introduction |
+--------------+
This is the introduction.

+---------+
| Summary |
+---------+
This is summary.

'''

lineStyle = "="

def heading(s):
    
    def line():
        print("+", lineStyle * (len(s) + 2), "+", sep='')
    
    
    line()
    print("|", (s), "|")
    line()



heading("Introduction")
print("This is the introduction.")
print()
heading("Summary")
print("This is summary.")
print()