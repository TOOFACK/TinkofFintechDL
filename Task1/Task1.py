import pandas as pd

df = pd.read_csv("new.csv")

price = df['price'].values
time = df['time'].values
date = df['date'].values
val = int(input())
date_of_buy = 0
date_of_selling = 0
backpack = []
# Идея жадного алгоритма для 1 задчи, как только цена возрастает покупаем акцию, если капитал позволяет и фиксируем
# время покупки, до тех пор пока цена возрастает не продаем, как только упала продеам и сравниваем с значением max,
# в которой хранится максимальная прибыль,если больше фиксируем прибыль и время продажи, а также записываем изменения
# цен в каждый момент времени, между date_of_buy и date_of_selling затем пробегаемся по массиву и выбираем максимальное

max = 0
income = 0
index = 0
k = 0
for i in range(len(price) - 1):
    if price[i] < price[i + 1] and val >= price[i]:
        k = i
        index = i
        date_of_buy = date[i]
        while k < len(price) - 1:
            if price[k] < price[k + 1]:
                income = price[k + 1] - price[i]
                k += 1
            else:
                i = k
                break
        if income > max:
            max = income
            date_of_selling = date[i]
            backpack = price[index:i+1]
        income = 0
print(date_of_buy)
print(date_of_selling)
print(backpack)
print(max)
