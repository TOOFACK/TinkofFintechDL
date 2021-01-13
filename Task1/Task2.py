import pandas as pd

df = pd.read_csv("new.csv")

price = df['price'].values
time = df['time'].values
date = df['date'].values

val = int(input())
max = 0
income = 0
index = 0
k = 0

date_of_buy = 0
date_of_selling = 0
backpack = []

date_of_buy2 = 0
date_of_selling2 = 0
backpack2 = []


def max_income(val, start, price, date):
    _income = 0
    _max = 0
    _date_of_selling = 0
    _backpack = 0
    _date_of_buy = 0
    _index = 0
    for i in range(start, len(price) - 1):
        if price[i] < price[i + 1] and val >= price[i]:
            k = i
            index = i
            _date_of_buy = date[i]
            while k < len(price) - 1:
                if price[k] < price[k + 1]:
                    _income = price[k + 1] + val - price[i]
                    k += 1
                else:
                    i = k
                    break
            if _income > _max:
                _max = _income
                _date_of_selling = date[i]
                _backpack = price[index:i + 1]
                _index = i
    return _max, _date_of_buy, _date_of_selling, _backpack, _index, index


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
        temp_max, temp_dateBuy, temp_dateSelling, tempBackpack, _index1, _index2 = max_income(val, i, price, date)
        if income + temp_max > max:
            max = income + temp_max
            date_of_selling = date[i]
            date_of_selling2 = temp_dateSelling
            date_of_buy2 = temp_dateBuy
            backpack2 = price[_index2:_index1 + 1]
            backpack = price[index:i + 1]
        income = 0
