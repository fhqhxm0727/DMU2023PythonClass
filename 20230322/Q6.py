n = int(input('어디까지 짝수를 합할까요? : '))
i = 2
sum = 0


while i <= n :
    sum = sum + i 
    i = i + 2

print('1부터 %d까지의 짝수 합은 %d\n' % (n, sum))

i = 2
sum = 0
for i in range(2, n+1, 2) :
    sum = sum + i
     
print('1부터 %d까지의 짝수 합은 %d\n' % (n, sum))
