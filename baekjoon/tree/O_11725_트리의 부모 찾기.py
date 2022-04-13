# First Trial referred to other's solution
# Solved (메모리 156188 KB, 시간 452 ms)

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N + 1)]
Parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def dfs(idx, tree, parents):
    for child in tree[idx]:
        if not parents[child]:
            parents[child] = idx
            dfs(child, tree, parents)

dfs(1, Tree, Parents)
print(Tree)
print(Parents)

for i in range(2, len(Parents)):
    print(Parents[i])