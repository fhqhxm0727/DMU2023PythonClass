select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if(select == 1) :
	evalWhat = input("수식을 입력해주세요 : ")
	answer = eval(evalWhat)
	print("%s 결과는 %5.1f입니다." % (evalWhat, answer))

elif(select == 2) :
	print("두 수 사이의 합계를 계산합니다.")
	a = int(input("수 a : ")) 
	b = int(input("수 b : ")) 
	i = 0
	sum = 0
	for i in range(a, b+1) :
		sum = sum + i
	print("%d + ... %d + %d까지의 값은 %d 입니다." % (a, b, b+1, sum))


else : print('시행할 수 없는 명령입니다')