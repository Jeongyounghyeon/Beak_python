import sys
input = sys.stdin.readline

high, wide = map(int, input().split())
world = list(map(int, input().split()))

result = 0

for i in range(1, wide-1, 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        result += compare - world[i]

print(result)