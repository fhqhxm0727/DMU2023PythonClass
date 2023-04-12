myStr = input("문자열을 입력하세요 : ")
outStr = ""

count = len(myStr)

for k in range(count-1, -1, -1) :
    outStr += myStr[k]

print("내용을 거꾸로 출력 : %s" % outStr)




print("내용을 거꾸로 출력 --> ")

for k in range(len(myStr)-1, -1, -1) :
    print(myStr[k])

for i in range(0, len(myStr)) : # range(m, n) == m to n-1
                                # len(myStr) == '글자 수' 제공. 인덱스 사용위한 -1필요
    print(myStr[len(myStr)-1 -i], end='')