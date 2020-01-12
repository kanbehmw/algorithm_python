def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r

    return x


x, y = tuple(map(int, input().split()))
print(gcd(x, y))