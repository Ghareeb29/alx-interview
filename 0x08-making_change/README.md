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

1. We first check if the total is 0 or less, in which case we return 0.
2. We sort the coins in descending order to start with the largest denominations.
3. We iterate through each coin denomination:
   - For each coin, we use as many of that coin as possible (using integer division).
   - We keep track of the total number of coins used and the remaining amount.
4. If at any point the remaining amount becomes 0, we return the total number of coins used.
5. If we've gone through all coins and still haven't reached the total, we return -1.

The time complexity of this solution is O(n log n) due to the sorting step, where n is the number of coin denominations. However, the actual coin selection process is O(n), which is very fast even for large totals.

The space complexity is O(1) as we only use a constant amount of extra space.

This greedy approach works correctly for standard coin systems (like US coins: 1, 5, 10, 25 cents) where the greedy choice always leads to the optimal solution. However, it's worth noting that for some non-standard coin systems, this greedy approach might not always give the optimal solution. In those rare cases, the dynamic programming approach would be more accurate.
