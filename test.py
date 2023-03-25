

from time import time
from time import gmtime
from time import localtime
from time import sleep


print("입력한 시간까지 몇시간 몇분 몇초 남았는지 알려주고, 해당 시간에 종료되는 프로그램입니다!")
wantHour = int(input("원하는 시 입력 : "))
wantMinute = int(input("원하는 분 입력 : "))


tm = localtime(time())
print("%d시 %d분" % (tm.tm_hour, tm.tm_min))
sleep(1)