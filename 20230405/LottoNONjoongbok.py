from random import randrange
from random import sample

#randrange() 함수와 집합을 이용, 중복을 제거
mylotto = set()

while True :
    num = randrange(1, 10)
    print(num, end=' ')
    mylotto.add(num)
    if len(mylotto) == 6 :
        break

print('\n 집합 : {}'.format(mylotto))
print('정렬리스트 : %s' % sorted(mylotto))

print('\nsample로 번호 리스트 만들기')
lotto = sample(range(1, 46), 6)
print('sample 함수 리스트 : {}'.format(lotto))
print('sample 함수 정렬 리스트 : %s' % sorted(lotto))

