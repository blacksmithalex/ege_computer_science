from math import sqrt
def num_of_div(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return len(div)

prev = set()
for n in range(1, 700000):
    prev.add(num_of_div(n))

count = 1
num_div_prev = num_of_div(700000)
n = 700000 + 1
print(700000, num_div_prev)
prev.add(num_div_prev)
while count != 5:
    num_div = num_of_div(n)
    if num_div > num_div_prev and num_div not in prev:
        num_div_prev = num_div
        print(n, num_div)
        count += 1
    prev.add(num_div)
    n += 1

#Нужно дофиксить баги