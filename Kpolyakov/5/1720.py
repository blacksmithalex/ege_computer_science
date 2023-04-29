def f(N):
    digits = sorted([i for i in str(N)])
    if digits.count('0') == 0:
        ma2 = int(digits[2] + digits[1])
        mi2 = int(digits[0] + digits[1])
    elif digits.count('0') == 1:
        ma2 = int(digits[2] + digits[1])
        mi2 = int(digits[1] + digits[0])
    else:
        ma2 = mi2 = 0
    return ma2 - mi2

count = 0
for N in range(100, 200 + 1):
    if f(N) == 30:
        count += 1
print(count)

