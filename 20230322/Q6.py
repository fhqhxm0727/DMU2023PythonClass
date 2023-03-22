n = int(input('어디까지 짝수를 합할까요? : '))
i = 1
sum = 0


while i <= n :
    if i % 2 == 0 : sum = sum + i 
    i = i + 1

print('1부터 %d까지의 짝수 합은 %d\n' % (n, sum))

i = 0
sum = 0
for i in range(1, n+1) :
    if i % 2 == 0 : sum = sum + i
     
print('1부터 %d까지의 짝수 합은 %d\n' % (n, sum))
