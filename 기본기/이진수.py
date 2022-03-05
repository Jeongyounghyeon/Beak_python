result=0

N=int(input())

for i in range(1, N+1, 1):
    if i==1:
        result=0
    elif i%2==0:
        result=2*result+1
    else:
        result=2*result-1

print(result)