import random

gnum = 0

while True :
    com= random.randrange(3)
    user= int(input('가위0 바위1 보2 선택: '))
    if not(user in [0, 1, 2]) :
        print('결과 user= %d, com= %d' % (user, com))

        if user == com :
            print('비겼습니다!')
        elif (user == 0 & com == 2) | (user == 1 & com == 0) | (user == 2 & com == 1) :
            print ("user가 이겼습니다!")
        else :
            print("com이 이겼습니다...")
        gnum = gnum + 1

        
    else : break

print('가위바위보를 %d회 플레이 하셨습니다!' % gnum)