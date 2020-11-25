import numpy as np


def RhoAlgorithmFloyd(n, hare, c, tortoise, factor = 1):
    start = hare
    while factor == 1:
        tortoise = ((tortoise * tortoise) % n + c) % n
        hare = ((hare * hare) % n + c) % n
        hare = ((hare * hare) % n + c) % n
        factor = np.gcd(abs(tortoise-hare), n)
        if factor == n or tortoise == hare:
            print("either n is a prime or your x^2 + c combination doesn't work for this problem")
            hare, tortoise = start, start
            while factor == 1:
                tortoise = ((tortoise * tortoise * tortoise) % n + c) % n
                hare = ((hare * hare * hare) % n + c) % n
                hare = ((hare * hare * hare) % n + c) % n
                factor = np.gcd(abs(tortoise - hare), n)
                if factor == n or tortoise == hare:
                    print("n might be a prime number")
    return factor
