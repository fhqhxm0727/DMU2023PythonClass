import random

com = random.randrange(1, 21)

print("무작위로 정해진 1부터 20까지의 수 중 하나를 맞추는 스무고개 게임입니다.")
while True : 
    user = int(input("1 ~ 20 사이 수 입력 : "))
    if com == user :     
        print("맞췄습니다")
        break
    elif com > user :
        print("더 큰 수 입니다.")
    else :
        print('더 작은 수입니다')
    