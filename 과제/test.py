
from time import strftime
from time import strptime



import calendar


whatTime = strptime(input("확인할연도-확인할월-확인할일 형식으로 입력해주세요 : "), "%Y-%m-%d")
print(calendar.month(whatTime.tm_year, whatTime.tm_mon))
print(strftime("확인해보니, %d일은 %A입니다.", whatTime))


# nowHour = 0
# nowMin = 0
# nowSec = 0
# isTmEnded = False

# print("입력한 시간까지 몇시간 몇분 몇초 남았는지 알려주고, 해당 시간에 종료되는 프로그램입니다!")
# wantTime = int(input("오전을 원하면 0, 오후를 원하면 1 입력 : "))

# wantHour = int(input("원하는 시 입력 : "))
# if wantTime == 1 and wantHour >= 12 : 
#     wantHour = abs(24 - (wantHour + 12))
    
# wantMinute = int(input("원하는 분 입력 : "))

# # 마지막 남은시간에서 nowSec이 0이 되어야 함
# # 

# while not isTmEnded : 
#     tm = localtime(time())
#     nowHour = wantHour-tm.tm_hour
#     if(wantMinute < tm.tm_min) : 
#           nowMin = 60 - (tm.tm_min - wantMinute)
#     else :
#           nowMin = wantMinute - tm.tm_min
#     nowSec = 59 - tm.tm_sec
    
#     if nowHour == 0 and nowMin == 0 :
#         print("카운트 종료.")
#         isTmEnded = True
#         break
#     else:
#         print("남은시간 : %d시 %d분 %d초" % (nowHour, nowMin, nowSec))
    
    
#     sleep(1)