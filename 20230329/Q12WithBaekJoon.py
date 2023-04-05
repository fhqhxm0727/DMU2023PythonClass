# 데이터개수 질의개수 입력받음
# 배열의 모든 값 입력받음
# 구할 범위의 인덱스 값 두개 입력받음

# 합 배열을 생성하여 작성하도록 한다
suNo = 0
quizNo = 0
suNo, quizNo = map(int, input().split())

numbers = list(map(int, input().split()))

pSum = [0]
temp = 0



for i in numbers :
    temp += i
    pSum.append(temp)

# 아래 반복문이 왜 오답인지 생각해보기
# for k in range(len(numbers)) :
#    pSum.append(pSum[k] + numbers[k])

print(pSum)

result = []

for i in range(quizNo) :
    s, e = map(int, input().split())
    result.append(pSum[e]-pSum[s-1])

print(result)
