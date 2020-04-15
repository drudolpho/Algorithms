#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530,
prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    biggest_difference = -9999

    for i in range(len(prices) - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            diff = prices[i] - prices[j]
            if diff > biggest_difference:
                biggest_difference = diff

    return biggest_difference


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
