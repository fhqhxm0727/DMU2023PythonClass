import random as r
import time as t

howManyTime = int(input("슬롯머신을 몇 번 돌릴까요? : "))

slot = [0]*3

for i in range(howManyTime) :
    for k in range(3) :
        slot[k] = r.randrange(7,10) # 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(1)

    if sum(slot) == 21 :
        print("잭팟!")
        break
    else : print("아깝네요...")