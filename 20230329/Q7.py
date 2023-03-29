# 리스트에 데이터를 읽어들여 
# 합과 평균, 최대값과 최소값을 구하여 출력하는 코드를 작성하시오

n = int(input("처리할 데이터의 개수를 입력해주세요 : "))
listex = [] # append사용 없이 하려면 list = 0*n

# sum = 0

print(n, '개의 데이터를 입력해주세요')
listex.append(int(input()))
# sum += listex[0]
# max, min = listex[0], listex[0]

for k in range(1, n) :
    listex.append(int(input())) # append사용 없이 하려면 listex[k] = int(input())
                                # input은 입력된 한 줄을 문자열로 읽어냄.
                                # 공백이 포함되어있는 경우, int로 바꿀수없다...
    # sum += listex[k]
    # if max < listex[k] : max = listex[k]
    # if min > listex[k] : min = listex[k]


avg = sum(listex) / len(listex)

msum = sum(listex)
print("입력된 리스트의 값 : ", listex)
print('리스트 데이터의 합 : %d' % msum)
print('리스트 데이터의 평균 : %d' % avg)
print('리스트 데이터의 최대값 : %d' % max(listex))
print('리스트 데이터의 최소값 : %d' % min(listex))