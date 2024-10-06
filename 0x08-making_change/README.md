# 0x08-making_change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: def makeChange(coins, total)
- Return: fewest number of coins needed to meet total
  - If total is 0 or less, return 0
  - If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

## example

```bash
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py

# !/usr/bin/python3

"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```

This implementation uses dynamic programming to solve the coin change problem efficiently. Here's a breakdown of the solution:

1. We first check if the total is 0 or less, in which case we return 0.
2. We create a dynamic programming array `dp` where `dp[i]` represents the minimum number of coins needed to make change for amount `i`.
3. We initialize all values in `dp` to infinity, except `dp[0]` which is set to 0 (it takes 0 coins to make a total of 0).
4. We then iterate through all amounts from 1 to `total`.
5. For each amount, we try all coin denominations and update `dp[i]` with the minimum number of coins needed.
6. Finally, we return `dp[total]` if a solution was found, or -1 if it's impossible to make change for the given total.

This solution has a time complexity of O(total * len(coins)) and a space complexity of O(total), which is efficient for most practical cases.
