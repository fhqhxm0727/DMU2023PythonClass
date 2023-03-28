from time import strftime
from time import strptime

import calendar


whatTime = strptime(input("확인할연도-확인할월-확인할일 형식으로 입력해주세요 : "), "%Y-%m-%d")
print(calendar.month(whatTime.tm_year, whatTime.tm_mon))
print(strftime("확인해보니, %d일은 %A입니다.", whatTime))