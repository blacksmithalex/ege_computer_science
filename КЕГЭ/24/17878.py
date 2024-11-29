def solution_linear(a):
    flag_operator = False
    flag_leading_zero = False
    flag_prev_zero = False

    count, countm = 0, 0
    for x in a:
        if x == '0':
            if flag_operator or count == 0:
                flag_leading_zero = True
            if not flag_leading_zero or flag_operator:
                count += 1
                countm = max(count, countm)
            else:
                count = 1
            flag_prev_zero = True
            flag_operator = False
        elif x in '6789':
            if flag_leading_zero:
                count = 1
            else:
                count += 1
                countm = max(count, countm)
            flag_leading_zero = False
            flag_operator = False
            flag_prev_zero = False
        else:
            if not flag_operator and count != 0:
                count += 1
                flag_operator = True
            else:
                count = 0
            flag_leading_zero = False
            flag_prev_zero = False
    return countm

file = open('24_17878.txt')
a = file.readline()
file.close()

print(solution_linear(a))