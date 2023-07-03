mn = 10000

def f(n):
    sm = 0
    for i in n:
        sm += int(i)
    for i in range(2, (sm+1)//2):
        if sm % i == 0:
            return False
    return True


for i in range(41, 100):
    st = '0' + (40 * '1')+ (i * '2')+ '0'
    st_nach = st
    while not '00' in st:
        st = st.replace('02', '101', 1)
        st = st.replace('11', '2', 1)
        st = st.replace('012', '30', 1)
        st = st.replace('010', '00', 1)
    if f(st):
        mn = min(mn, st_nach.count('2'))
print(mn)