F = [0] * (2023 + 1)
F[1] = 1
for n in range(2, 2023 + 1):
    F[n] = F[n - 1] * n

print(F[2023] / F[2020])

