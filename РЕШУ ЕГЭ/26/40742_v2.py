file = open('26.txt')
n = int(file.readline())
start_time = 1633305600
end_time = start_time + 604800
count = 0
time_process = [0] * 604800
for _ in range(n):
    start_process, end_process = [int(x) for x in file.readline().split()]
    if (start_process < start_time) and ((end_process > start_time) or (end_process == 0)):
        count += 1
    if (start_process >= start_time) and (start_process <= end_time):
        time_process[start_process - start_time] += 1
    if (end_process >= start_time) and (end_process <= end_time):
        time_process[end_process - start_time] -= 1

sum_time = 0
max_process = 0
for i in range(604800):
    count = count + time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time += 1
print(max_process, sum_time)


