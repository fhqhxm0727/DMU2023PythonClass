file_path = "C:\class_colon.txt"

data_dict = {}

# 읽어온 파일은 다음과 같은 형식을 지닌다
# 과목코드:교수명:수강인원:강의실번호

with open(file_path, "r") as f :
    for line in f : 
        id, *data = line.strip().split(':')
        # 첫번째 값을 id, ':' 이후 나머지 모든 값(*data) 총 두가지 값으로 저장
        # 나머지 모든 값도 ':'로 데이터 분할이 이루어진다는 점 잊지 않기
        data_dict[id] = tuple(data)
        #data_dict 딕셔너리의 id 값. 즉, key 값에 대한 value로 tuple 형의 data를 부여

# print(data_dict) -> dictionary

for k in data_dict :
        print(k, data_dict[k]) # key값 k와 내부 튜플값 출력
smax = 0
max_idx = 0

for k in data_dict : 
    if int(data_dict[k][1]) > smax :
        smax = int(data_dict[k][1])
        max_idx = k

print("최대 수강 인원인 강좌의 정보 : ", max_idx, ':', data_dict[max_idx])


snumList = []
for k in data_dict :
     idata = int(data_dict[k][1])
     snumList.append(idata)

print('리스트 함수이용 : 최대 수강인원은 = ', max(snumList))


