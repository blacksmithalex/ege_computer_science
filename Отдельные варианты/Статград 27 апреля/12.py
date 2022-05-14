def f(a):
  while '00' not in a:
    a = a.replace('02', '20', 1)
    a = a.replace('03','30', 1)
    a = a.replace('011', '1031', 1)
    a = a.replace('01','102', 1)
  return a

a = '0' + '1' * 5 + '21' * 12 + '0'
res = f(a)
print(res.count('1'), res.count('2'), res.count('3'))

#Ответ: 12