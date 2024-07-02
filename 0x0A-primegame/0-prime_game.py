#!/usr/bin/python3
""" Module for solving the prime game question """

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    x (int): Number of rounds.
    nums (list of int): List of the upper limits for each round.

    Returns:
    str: The name of the player who wins the most rounds ('Maria' or 'Ben').
         Returns None if there is a tie or invalid input.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max(max_num + 1, 2))
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Cumulative count of primes up to each index
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    # Determine the number of rounds won by Maria
    maria_wins = sum(prime_count[num] % 2 == 1 for num in nums)

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"

