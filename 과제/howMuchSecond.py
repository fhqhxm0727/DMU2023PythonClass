from time import time
from time import localtime
from time import sleep

launch_time = localtime(time())
# launch_time은 localtime으로 생성된 객체값 지님
# launch_time
print("현재 시각은 %d시 %d분 %d초 입니다." % (launch_time.tm_hour, launch_time.tm_min, launch_time.tm_sec))
sleep(int(input("몇 초 동안 대기할까요? : ")))

afterSleep_time = localtime(time())
print("현재 시각은 %d시 %d분 %d초 입니다." % (afterSleep_time.tm_hour, afterSleep_time.tm_min, afterSleep_time.tm_sec))

# 실행 시간 저장
# 입력한 초 만큼 sleep으로 대기
# 대기 이후 시간 출력