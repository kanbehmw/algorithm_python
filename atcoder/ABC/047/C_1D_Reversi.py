S = input()
prev = S[0]
ans = 0
for i in range(1, len(S)):
    if prev != S[i]:
        ans += 1
    prev = S[i]
print(ans)