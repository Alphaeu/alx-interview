# 0x08. Making Change

## Overview
This project focuses on solving the classic coin change problem using dynamic programming. The objective is to determine the minimum number of coins required to make up a given total amount from a list of coin denominations.

## Concepts Covered
- **Greedy Algorithms**: Understanding their applications and limitations in the context of the coin change problem.
- **Dynamic Programming**: Implementing an efficient solution to handle overlapping subproblems and optimal substructure.
- **Algorithmic Complexity**: Analyzing and striving for solutions with lower time and space complexity.
- **Problem-Solving Strategies**: Breaking down problems, iterative vs. recursive approaches.
- **Python Programming**: Efficient use of lists, list comprehensions, and control flow tools.

## Resources
- **Python Documentation**: [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- **GeeksforGeeks Articles**: 
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**: 
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic)

## Requirements
- **Editors**: vi, vim, emacs
- **Python Version**: 3.4.3 on Ubuntu 20.04 LTS
- **PEP 8 Style**: Code must follow PEP 8 style guidelines (version 1.7.x)
- **Execution**: All files must be executable and end with a new line
- **README**: A `README.md` file at the root of the project directory is mandatory

## Task

### 0. Change Comes From Within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

#### Prototype
```python
def makeChange(coins, total):
```

#### Return
- Fewest number of coins needed to meet `total`.
- If `total` is 0 or less, return 0.
- If `total` cannot be met by any number of coins, return -1.

#### Constraints
- `coins` is a list of the values of the coins.
- The value of each coin is an integer greater than 0.
- Assume an infinite number of each denomination of coin.

### Example Usage
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Implementation

### File: `0-making_change.py`
```python
#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
```

## Author
**ALX Software Engineering Program**
