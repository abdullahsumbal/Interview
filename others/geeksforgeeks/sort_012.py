

a = [1,0,1,0,2,2,2,1,0]
arr_size =len(a)



lo = 0
hi = arr_size - 1
mid = 0
while mid <= hi:
    if a[mid] == 0:
        a[lo],a[mid] = a[mid],a[lo]
        lo = lo + 1
        mid = mid + 1
    elif a[mid] == 1:
        mid = mid + 1
    else:
        a[mid],a[hi] = a[hi],a[mid]
        hi = hi - 1
    print (a)
    print("low: ", lo, "| mid: ", mid, "| hi: ", hi)
    print("")
