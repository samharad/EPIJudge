from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_price, max_profit = 0.0, 0.0
    for price in reversed(prices):
        max_price = max(max_price, price)
        profit = max_price - price
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
