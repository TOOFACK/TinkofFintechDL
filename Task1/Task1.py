val = int(input())  # капитал
temp = int(input())  # длина "массива" акций
time = []  # массив времени каждой акции
income = 0
mas = []
time_buy = []
time_sold = []
incomes = []
for i in range(temp):
    mas.append(int(input()))
for i in range(temp):
    time.append(int(input()))
# Идея жадного алгоритма для 1 задчи, как только цена возрастает покупаем акцию, если капитал позволяет и фиксируем
# время покупки до тех пор пока цена возрастает не продаем, как только упала продеам, фиксируем прибыл,
# учитывая капитал, и фиксируем время продажи, затем пробегаемся по массиву и выбираем максимальное

k = 0
for i in range(temp - 1):
    if mas[i] < mas[i - 1] and val >= mas[i]:
        k = i
        time_buy.append(time[i])
        while k < temp - 1:
            if mas[k] < mas[k + 1]:
                income = mas[k + 1] - mas[i]
                k += 1
            else:
                i = k
                break
        incomes.append(val - mas[i] + income)
        income = 0
        time_sold.append(time[i])

_max = 0
index = 0
for i in range(len(incomes)):
    if _max < incomes[i]:
        index = i
        _max = incomes[i]

print(incomes[index])
print(time_buy[index])
print(time_sold[index])