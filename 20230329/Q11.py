# 한 줄에 여러개의 입력을 받고 싶은 경우 예제

input("입력할 여러 개의 수를 공백으로 구분하여 입력 : ")
numbers = list(map(int, input.split()))
# input으로 입력받은 문자열을 split()으로 공백기준 분할하여 int 형변환.
# 이후 map활용하여 list의 각 데이터 값으로 매핑 시행.
# numbers 리스트 생성 완료