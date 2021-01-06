val = int(input())  # капитал
temp = int(input())  # длина "массива" акций
time = []  # массив времени каждой акции
income = 0
mas = []
time_buy = []
time_sold = []
for i in range(temp):
    mas.append(int(input()))
for i in range(temp):
    time.append(int(input()))
# Идея жадного алгоритма, будем идти по массиву и при возрастании цены, покупать акцию и искать момент,
# когда ее выгоднее всего продать, момент покупки будем записывать в массив buy, а продожи а sold

sum = 0
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
        sum += income
        val -= mas[i]
        time_sold.append(time[i])
        print(time_sold, time_buy, sum)
