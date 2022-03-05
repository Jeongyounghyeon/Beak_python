cnt=0
max=0

for i in range(0, 10, 1):
    person_out, person_in=map(int, input().split())
    cnt=cnt-person_out+person_in
    if cnt>max:
        max=cnt

print(max)