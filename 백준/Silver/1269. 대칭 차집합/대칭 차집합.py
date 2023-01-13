import sys

n,m = map(int, input().split())

N = set()
M = set()

N = set(list(map(int, input().split())))
M = set(list(map(int, input().split())))

print(len(M-N)+len(N-M))