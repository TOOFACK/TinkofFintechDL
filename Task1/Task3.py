import pandas as pd


def DP_utils(k, prices):
    if len(prices) < 2:
        return 0
    max_profit = 0

    if k >= len(prices) / 2:
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i - 1], 0)
        return max_profit

    max1 = [[0] * len(prices) for _ in range(k + 1)]
    max2 = [[0] * len(prices) for _ in range(k + 1)]

    for t in range(1, len(prices)):
        cur_profit = prices[t] - prices[t - 1]
        for j in range(1, k + 1):

            max2[j][t] = max(max1[j - 1][t - 1] + max(cur_profit, 0), max2[j][t - 1] + cur_profit)

            max1[j][t] = max(max1[j][t - 1], max2[j][t])

    return max1[k][-1]


df = pd.read_csv("new.csv")

price = df['price'].values
time = df['time'].values
date = df['date'].values
temp = int(input())

val = int(input())
k = int(input())  # транзакции
print(DP_utils(k, price))
