file = open('26_8482.txt')
N = int(file.readline())
K = int(file.readline())
a = []
for _ in range(N):
    start, end = [int(x) for x in file.readline().split()]
    a.append([start, end])
file.close()
a = sorted(a)

ends = [-20] * K
count, lastind = 0, 0
for start, end in a:
    flag = False
    for i in range(K):
        if ends[i] < start:
            flag = True
            ends[i] = end + 5
            count += 1
            lastind = i
            break
    if not flag:
        m_ends = min(ends)
        m_time = m_ends - start + 1
        if m_time <= 10:
            m_ind = ends.index(m_ends)
            T = end - start
            if ends[m_ind]  + T + 1 <= 70 * 23:
                ends[m_ind] = T + 5 + 1
                count += 1
                lastind = m_ind
print(count, lastind + 1)