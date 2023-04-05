s1 = {0,1,3,5,7}
s2 = set() #비어있는 세트를 제작 시, set()를 이용한다.
            #그러나, 보통 비어있는 세트를 제작할 일은 없으므로 거의 사용하지 않음
s2.add(2), s2.add(4), s2.add(6), s2.add(8), s2.add(0)


print(s1|s2)
print(s1&s2)
print(s1-s2)

# format 메소드는 시험에 안나옴
# 그래도 문자열 관련 메소드니 한 번 써보기...
print('{0}과 {1}의 합집합 = {2}'.format(s1, s2, s1|s2))
print('{0}과 {1}의 교집합 = {2}'.format(s1, s2, s1&s2))
print('{0}과 {1}의 차집합 = {2}'.format(s1, s2, s1-s2))