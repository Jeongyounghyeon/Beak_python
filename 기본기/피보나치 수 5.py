fibonaccy=[]

fibonaccy.insert(0, 0)
fibonaccy.insert(1, 1)

n=int(input())

for i in range(2, n+1, 1):
    fibonaccy.insert(i, fibonaccy[i-2]+fibonaccy[i-1])
    
print(fibonaccy[n])