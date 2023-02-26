from fnmatch import fnmatch

for n in range(2023, 10**10, 2023):
    if fnmatch(str(n), '1?2139*4'):
        print(n, n // 2023)

