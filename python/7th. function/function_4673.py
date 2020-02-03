def self_num():
    num_list = list(range(1,10000))
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    try:
                        del(num_list[num_list.index((i*1001 + j * 101 + k * 11 + l * 2))])
                    except:
                        continue
    for p in num_list:
        print(p)

self_num()