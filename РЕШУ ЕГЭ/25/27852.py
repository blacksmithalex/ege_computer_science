def Searchdividers(number):
    alldividers = []
    for divider in range(1, int(number**0.5) + 1):
        if number % divider == 0:
            alldividers.append(divider)
            alldividers.append(number // divider)
    alldividers = sorted(alldividers)
    return alldividers

for number in range(185311, 185331):
    if len(Searchdividers(number)) == 4:
        print(Searchdividers(number))