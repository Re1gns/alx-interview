#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    MAX_VALUE = float('inf')
    table = [MAX_VALUE for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != MAX_VALUE and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == MAX_VALUE:
        return -1
    return table[total]
