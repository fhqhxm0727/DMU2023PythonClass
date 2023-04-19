x, y = map(int, input("사용할 x값과 y값을 입력해주세요 : ").split())


for i in range(1,x) :
    print(i, "단 출력 : ", end="\n")
    for k in range(1,y) :
        if(k == 2) : continue
        print(i, " * ", k, " = ", i*k)
        if(k > 4) : break