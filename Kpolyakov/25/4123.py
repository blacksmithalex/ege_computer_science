def gcd(a, b):
    if a % b == 0 or b % a == 0:
        return min(a, b)
    elif a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)

count, Smax, cmax = 0, 0, 0
for n in range(1, 71):
    for m in range(n + 1, 71):
        if n ** 2 + m ** 2 > 5000:
            continue
        if gcd(m, n) == 1 and (m - n) % 2 != 0:
            a, b, c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
            factor = 5000 // c
            count += factor
            a, b, c = a * factor, b * factor, c * factor
            if a + b + c > Smax:
                Smax, cmax = a + b + c, c
print(count, cmax)

