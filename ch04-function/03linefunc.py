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

def heading(s):
    print("+-", ("-" * len(s)), "-+", sep='')
    print("|", (s), "|")
    print("+-" + ("-" * len(s)) + "-+")



heading("Introduction")
print("This is the introduction.")
print()
heading("Summary")
print("This is summary.")
print()
