list = ("abc", 123)

print(list)
for x in list:
    print(x)
    
books = [
    ("Learn Java", 12.94),
    ("Python Made Easy", 17.99)
    ]

print(books)
print()
for book in books:
    for data in book:
        print(data)
