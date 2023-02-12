def f(n):
    nums = sorted([int(x) for x in str(n)])
    ma = nums[2] * 10 + nums[1]
    if nums.count(0) == 0:
        mi = nums[0] * 10 + nums[1]
    elif nums.count(0) == 1:
        mi = nums[1] * 10 + nums[0]
    else:
        mi = ma
    return ma - mi

count = 0
for n in range(500, 600 + 1):
    if f(n) == 10:
        count += 1
print(count)