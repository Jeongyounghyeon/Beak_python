k = int(input())

for i in range(0, k, 1):
    A, B = input().split()

    A = int(A)
    B = int(B)

    print("Case #%d: %d + %d = %d" % (i+1, A, B, A+B))