import random

taro= ['자유', '시작', '갈등', '풍요', '성공', '자립', '연예', '전진',
        '극복', '회피', '선택', '안정', '희생', '불행', '인내', '유혹',
        '파괴', '균형', '불안', '행복', '결단', '성취']


print("타로 카드는 아래와 같은 종류가 있습니다.")
print(taro)

print("다섯 개의 무작위 타로 카드를 뽑습니다.")


for k in range(5) : 
    index = random.randrange(0,23)

    print("%s" % taro[index])