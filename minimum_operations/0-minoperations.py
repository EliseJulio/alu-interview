#!/usr/bin/python3
"""Interview Questions."""


def minOperations(n):
    """Minimum operations to reach n."""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
