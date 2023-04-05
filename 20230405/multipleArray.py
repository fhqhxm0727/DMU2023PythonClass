list1 = []
list2 = []
value = 0
for i in range(0, 3) :
    for k in range(0, 4) :
        list1.append(value)
        value += 5
    list2.append(list1) # list2에 append되는 list1은 일차원 리스트므로, 이차원 리스트 형식으로 사용됨.
    list1 = []

for i in range(0, 3) :
    for k in range(0, 4) :
        print("%3d" % list2[i][k], end= " ")
    print("")


for i in range(0, 4) : # 이차원 리스트 접근 방식 : 전치 - transpose
    for k in range(0, 3) :
        print("%3d" % list2[k][i], end= " ")
    print("")