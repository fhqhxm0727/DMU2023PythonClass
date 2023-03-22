
for x in range(2, 10) :
    print("\n%d단 : " % x, end="\n")
    for y in range(1, 10) :
        print("%d * %d = %d" % (x, y, x*y), end=" ")
        if y == 4 : break