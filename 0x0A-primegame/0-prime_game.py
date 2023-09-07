#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None
    maria, ben = 0, 0
    # generating prime number max nums
    num = max(nums)
    prime = [True for _ in range(1, num + 1, 1)]
    prime[0] = False
    for i, isPrime in enumerate(prime, 1):
        if i == 1 or not isPrime:
            continue
        for j in range(i + i, num + 1, i):
            prime[j - 1] = False
    # number of prime less than n in nums
    for _, num in zip(range(x), nums):
        count = len(list(filter(lambda x: x, prime[0: num])))
        ben += count % 2 == 0
        maria += count % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
