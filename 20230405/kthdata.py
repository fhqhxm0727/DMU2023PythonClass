from random import randrange  # randrange를 따로 임포트했으므로, random 호출 필요 X
# 다음의 두가지 방법으로 k번 수를 선택
# 0 ~ 99 까지의 random number를 20개 리스트에 작성
# .sort 이용하여 오름차순 정렬 후 k번째 데이터 출력

# 0부터 50까지의 데이터를 중복없이 20개 만들어 min()으로 최소값을
# k번 구하고 마지막 값을 출력하기


#방법1
myList = [] 

for i in range(0, 20) :
    myList.append(randrange(0, 100))

# 오름차순 sort 실시
k = int(input("몇 번째로 작은 데이터를 구할까요? : "))
print(myList)
myList.sort() # 리스트 정렬
# myList.reverse() 큰 데이터 순서 구할때 오름차순 정렬 리스트 역순 전환
print(myList)
print(k, 'th data = ', myList[k-1])




#방법 2
# sort()를 이용한 정렬 대신, min() 함수를 이용하여 최소값을
# 차례차례 찾아나가는 방식.
count = 1
myList2 = []
while count < 20 : 
    num = randrange(0, 51)
    if num not in myList2: # 리스트 내에 있던 같은 값이 나온경우 실행되지 않음.
        myList2.append(num)
        count += 1 # 조건값인 카운트 증가가 if문 내에 있으므로, 값이 추가되지 않은 경우
        # 반복 조건 값이 증가.

print(myList2)
print(sorted(myList2))



# 최소값 구하고 k번만큼 삭제하기
for d in range(k) :
    mvalue = min(myList2)
    di = myList2.index(mvalue)
    del(myList2[di])
# 배열에서 최소값을 찾아 저장
# 최소값의 인덱스를 도출
# 해당 최소값의 인덱스를 이용해 del()로 삭제

myList2.sort()
print(myList2)
print(k, 'th data = ', mvalue)
