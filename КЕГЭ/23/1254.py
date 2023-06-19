uniq = {1}
for _ in range(9):
    new_uniq = set()
    for x in uniq:
        new_uniq.add(x * 2)
        new_uniq.add(x * 2 + 1)
    uniq = new_uniq
print(len(uniq))
