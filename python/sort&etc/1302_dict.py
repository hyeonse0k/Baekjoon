n = int(input())
books = {}
for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
max = max(books.values())
array = []
for book, number in books.items():
    if number == max:
        array.append(book)
print(books)