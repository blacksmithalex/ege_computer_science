uniq = {333}
for _ in range(13):
    new_uniq = set()
    for x in uniq:
        new_uniq.add(x - 3)
        new_uniq.add(x * (-3))
    uniq = new_uniq
neg = 0
for x in uniq:
    if x < 0:
        neg += 1
print(neg)
