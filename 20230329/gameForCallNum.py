num = int(input("몇으로 나누는 놀이를 할까요?"))
print("%d로 나누어지는 가장 가까운 수로 답해드릴게요" % num)

for k in range(5) :
    callNumber = int(input("call Number : "))

    percent = callNumber % num # num으로 나눈 나머지 제공
    # 두 가지 경우 : 1. 큰 쪽의 값이 정답인 경우, 2. 작은 쪽의 값이 정답인 경우
    if num - percent < percent : # 나누는 값 - 나머지 < 나머지 == 큰 쪽의 값
        answer = callNumber + (num-percent)
    else : # 작은 쪽의 값
        answer = callNumber - percent
    
    callNumber - percent # 가장 가까운 경우 1

    print("정답은 : %d" % answer)
     # 가장 가까운 경우 2
    