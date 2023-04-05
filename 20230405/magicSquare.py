# 이차원 리스트 연습시 필히 진행하는 코스

# 정방 행렬 ? : 행과 열의 개수가 동일한 배열.
# 마방진 : n*n 정방ㄹ 행렬에서 각 행, 열, 대각선의 합이 같도록 1부터 n^2까지의 값을 지님
# 3*3 행렬인 경우, 1부터 9까지의 수로 대입
# 스도쿠의 규칙을 생각해보기



print('참조 : 입력값은 홀수여야 함')
sdoku = int(input("제작할 정방행렬이 몇*몇인지 입력해주세요 : "))

count = 2 # 1이 이미 기입되어있음 + 앞으로 기입할 숫자로 사용


magicSquare = [[0]*sdoku for k in range(sdoku)]
# sdoku 만큼의 길이를 지닌 1차원 리스트를
# sdoku 개의 행만큼 생성

# magicSquare = [sdoku][sdoku]

#for i in range(0, sdoku) :
#   for j in range(0, sdoku) :
#        magicSquare[i][j] = 0 # 정방행렬 0 초기화

i = 0
j = sdoku//2
magicSquare[i][j] = 1 # 첫번째 행 가운데에 1로 제작

while count <= sdoku*sdoku :
    row = i-1; col = j-1
    if row < 0 : row = sdoku-1
    if col < 0 : col = sdoku-1
    if magicSquare[row][col] != 0 :
        i += 1
    else : i = row; j = col
    magicSquare[i][j] = count
    count += 1

print('magicNumber = %d', sum(magicSquare[0]))
print(magicSquare)

print('-------------------')
for m in magicSquare :
    print(m)
print('-------------------')



for row in range(sdoku) :
    for col in range(sdoku) :
        print('%4d' % magicSquare[row][col], end='')
    print()