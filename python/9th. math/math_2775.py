arr = [[0] * 15 for i in range(15)]
def find_person(floor, room_num):
    if floor == 0:
        return room_num
    elif arr[floor][room_num] != 0:
        return arr[floor][room_num]
    else:
        for i in range(1,room_num+1):
            arr[floor][room_num] += find_person(floor - 1,int(i))
        return arr[floor][room_num]

a = input()
for i in range(int(a)):
    floor = int(input())
    room = int(input())
    find_person(floor, room)
    print(arr[floor][room])