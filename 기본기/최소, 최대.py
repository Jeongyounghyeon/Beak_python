N=int(input())

num_list=list(map(int,input().split()))

max=num_list[0]
min=num_list[0]

for i in num_list[1:]:
    if i>max:
        max=i
    elif i<min:
        min=i

print(min, max)