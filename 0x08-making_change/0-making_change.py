#!/usr/bin/python3
"""
Interview Question on fewest number of coins needed to
meet a given amount total
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    """ Initialize DP array with a value larger than any possible number of coins"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins needed to make 0 amount
    
    """ Process each amount from 1 to total"""
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    """If dp[total] is still infinity, it means we cannot make the amount with given coins"""
    return dp[total] if dp[total] != float('inf') else -1
