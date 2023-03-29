

import random

count = 5
score = 0

# 3번 시도 후 맞추지 못할 경우 답을 출력

for Q in range(5) :
    correct = False
    tnum = 0
    x = random.randint(10, 99) # 10 to 99
    y = random.randrange(10, 100) # 같은 수 반복
    

    while tnum < 3 and not correct :
        print("%d + %d의 답은 ? : " %(x,y))
        answer = int(input())

        if answer == x + y : 
            print("Correct!! %d번만에 성공!" % tnum + 1)
            correct = True
            score += (20-tnum*3)
        else :
            tnum += 1
            print('Try Again~~~, 남은 횟수 %d' % round(3 - tnum))
            

    
    count -= 1
    if tnum == 3 : print("정답은", x+y, "였습니다...")

print("score : %d" %score)


    



tnum = 3