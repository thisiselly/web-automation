def chufa(mm, nn):
    result = mm
    count = 0
    while result >= nn:
        result = mm - nn
        count+=1
        mm = result
    return count

if __name__ == '__main__':
    print(chufa(1000000000,1))
    # print(100000000000//10)