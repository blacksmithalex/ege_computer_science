count = 0
cur = [[42]]
while len(cur) != 0:
    newcur = []
    for path in cur:
        for diff in [1, 3, -1, -3]:
            if (40 <= path[-1] + diff <= 49) and not ((path[-1] + diff in path) and (path[-1] + diff != 42)):
                if path[-1] + diff == 42:
                    count += 1
                else:
                    newcur.append(path + [path[-1] + diff])
    cur = newcur
print(count)
