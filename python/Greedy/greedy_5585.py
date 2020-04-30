n = int(input())
pay = 1000 - n
coin = [500,100,50,10,5,1]
sum_value , count = 0,0
while sum_value < pay:
    for i in coin:
        sum_value += i
        if sum_value > pay:
            sum_value -= i
        else:
            count += 1
            break
print(count)