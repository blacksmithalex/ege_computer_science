a = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
a = oct(a)[2:] #два символа, которые не относятся к числу
print(a.count('7'))


