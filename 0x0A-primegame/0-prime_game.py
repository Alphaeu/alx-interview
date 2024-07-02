#!/usr/bin/python3

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes, is_prime

def simulate_game(n, primes, is_prime):
    set_size = n
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        # Find the first prime that hasn't been removed
        move_made = False
        for p in primes:
            if p > set_size:
                break
            if is_prime[p]:
                move_made = True
                # Remove this prime and its multiples
                for multiple in range(p, set_size + 1, p):
                    is_prime[multiple] = False
                break
        if not move_made:
            break
        turn = 1 - turn  # Switch turns
    return turn

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes, is_prime = sieve(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # Reset the primes status for the current game
        current_is_prime = is_prime[:]
        winner = simulate_game(n, primes, current_is_prime)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

