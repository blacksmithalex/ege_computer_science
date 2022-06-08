def f(n):
    div = []
    for d in range(1, n + 1):
        if n % d == 0:
            div.append(d)
    return div

for n in range(201455, 201470 + 1):
    div = f(n)
    if len(div) == 4:
        print(*div)

