N, M = list(map(int, input().split()))

L, R = [], []
for i in range(M):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

ans = min(R) - max(L) + 1
if ans >= 0:
    print(ans)
else:
    print(0)
