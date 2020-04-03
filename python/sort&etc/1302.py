book_num = int(input())
book_list = []
no_list = []
best_list = []
for _ in range(book_num):
    book_list.append(input())
no_list = list(set(book_list))
for j in range(len(no_list)):
        best_list.append((book_list.count(no_list[j]),no_list[j]))
best_list = sorted(best_list, key= lambda x: (-x[0],x[1]))
print(best_list[0][1])