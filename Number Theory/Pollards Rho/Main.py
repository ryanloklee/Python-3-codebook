import RhoAlgorithm
from RhoAlgorithm import RhoAlgorithmFloyd

n = int(input())
hare = int(input())
c = int(input())
tortoise = hare
factor = RhoAlgorithmFloyd(n, hare, c, tortoise)
print(factor)
print(int(n/factor))