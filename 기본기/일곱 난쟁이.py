height=[]
cnt=0

for i in range(0, 9, 1):
    height.append(int(input()))
    cnt+=height[i]

for i in range(0, 9, 1):
    for j in range(i+1, 9, 1):
        if cnt-(height[i]+height[j])==100:
            spy1, spy2=height[i], height[j]

height.remove(spy1)
height.remove(spy2)
height.sort()

for i in range(0, 7, 1):
    print(height[i])