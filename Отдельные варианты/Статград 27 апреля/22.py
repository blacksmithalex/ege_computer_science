for i in range(9): #кол-во девяток
    for j in range(9 - i): #кол-во шестерок
        for k in range(9 - i - j): #кол-во троек
            for t in range(9 - i - j - k): #кол-во нулей
                if i + j + k + t != 8:
                    continue
                if 9 * i + 6 * j + 3 * k == 66:
                    print(i, j, k, t)

#Таким образом получаем две комбинации: 6 девяток и 2 шестерки или 7 девяток и 1 тройка