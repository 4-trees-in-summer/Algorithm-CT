import sys
import heapq

n = int(sys.stdin.readline())
num = []
answer = 0

for _ in range(n) :
    k = int(sys.stdin.readline())
    num.append(k)

heapq.heapify(num)

while len(num) != 1:
    n1 = heapq.heappop(num)
    n2 = heapq.heappop(num)
    n = n1+n2

    heapq.heappush(num, n)
    answer += n

print(answer)
    