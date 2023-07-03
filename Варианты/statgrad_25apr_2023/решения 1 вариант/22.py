proc = {}
file = open('22.txt')
count = 0
for line in file:
    id, t, addicts = line.split()
    id, t = int(id), int(t)
    if addicts[0] == '"':
        addicts = [int(x) for x in addicts[1:-1].split(';')]
    else:
        addicts = [int(addicts)]
    if len(addicts) == 1 and addicts[0] == 0:
        proc[id] = t
    else:
        for p in addicts:
            proc[id] = max(proc.get(id, 0), proc[p])
        if proc[id] >= 80:
            count += 1
        proc[id] += t

print(count)
