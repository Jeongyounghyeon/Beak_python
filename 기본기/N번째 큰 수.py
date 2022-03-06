import heapq

graph=[]

N=int(input())

for i in range(N):
    graph.append(list(map(int, input().split())))

heap=[]
heapq.heapify(heap)
for i in range(N):
    for j in range(N):
        heapq.heappush(heap, graph[i][j])
        if len(heap)>N:
            heapq.heappop(heap)

print(heapq.heappop(heap))