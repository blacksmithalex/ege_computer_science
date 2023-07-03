file = open('26.txt')
times = []
N = int(file.readline())
for line in file:
    ts, te, type = line.split()
    times.append([int(ts), int(te), type])
file.close()
times = sorted(times)

auto_in, auto_out = 0, 0
auto_ends = [-1] * 80
micro_ends = [-1] * 20
for a in times:
    ts, te, type = a
    if type == 'A':
        flag = False
        for i in range(80):
            if auto_ends[i] <= ts:
                auto_in += 1
                auto_ends[i] = ts + te
                flag = True
                break
        if not flag:
            for i in range(20):
                if micro_ends[i] <= ts:
                    auto_in += 1
                    micro_ends[i] = ts + te
                    flag = True
                    break
        if not flag:
            auto_out += 1
    else:
        flag = False
        for i in range(20):
            if micro_ends[i] <= ts:
                micro_ends[i] = ts + te
                flag = True
                break
        if not flag:
            auto_out += 1
print(auto_in, auto_out)


