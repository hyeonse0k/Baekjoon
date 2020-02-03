while True:
    try:
        value = input()
        a , b = map(int,value.split())
        print(a + b)
    except:
        break