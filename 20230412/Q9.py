upp, low, dig, pct = 0,0,0,0

pswd = input('암호입력 : ')

#아래 메소드들은 True 또는 False만을 반환한다.

if pswd.isalnum() == False :
    # pswd 문자열은 특수문자 없이 문자와 숫자로만 이루어져있는가?
    pct = 1
    # 특수 문자가 있으면 pct = 1

for k in pswd :
    if k.isupper() : upp = 1 # 대문자 존재시
    elif k.islower() : low = 1 # 소문자 존재시
    elif k.isdigit() : digit = 1 # 숫자 존재 시

if low + upp + dig + pct >= 3 :
    print('사용 가능')
else : print('사용 불가능한 암호')