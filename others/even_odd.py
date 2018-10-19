








def eve_odd(l):
    lastEven = 0
    counter = 0
    for cur in range(len(l)):
        if(l[cur] % 2 == 0):
            l[lastEven], l[cur] = l[cur], l[lastEven]
            lastEven = lastEven + 1
            counter = counter + 1

    print(l)
    return counter;



if __name__ == '__main__':
    list = [1,2,3,4,5,6,2,2]
    eve_odd(list)
