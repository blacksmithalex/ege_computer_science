from math import sqrt
def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

n = 520000
count = 0
while count != 5:
    D = dividers(n)
    if sum(D) != 0 and isPalindrome(sum(D)):
        print(n, D[-1])
        count += 1
    n += 1
