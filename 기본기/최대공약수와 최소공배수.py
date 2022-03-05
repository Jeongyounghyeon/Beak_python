from __future__ import division


a, b= map(int, input().split())

small=min(a,b)
big=max(a,b)

for i in range(small, 0, -1):
    if(small%i==0 and big%i==0):
        division=i
        break

i, j=1, 1

while True:
    if(small*i==big*j):
        product=small*i
        break
    elif(small*i>big*j):
        j+=1
    elif(small*i<big*j):
        i+=1

print(division)
print(product)