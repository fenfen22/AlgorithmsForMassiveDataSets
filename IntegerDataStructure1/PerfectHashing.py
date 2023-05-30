# Static Dictionary problem: given a set of integers S, which is a subset of U, following operations:
# 1. Lookup(x): return true if x is in S; otherwise return false


# Goal: perfect hashing in linear space and constant worst-case time
"""
data structure:
FKS scheme (two level solution):
1. at level 1 use colution with lots of collisions and linear space
2. resolve collisions at level 1 with collision-free solution at level 2
3. lookup(x): look-up in level 1 to find the correct level 2 dictionary. Lookup in level 2 dictionary

Collision-free but with too much space: use a universal hash function to map into an array of size n^2;
so we gonna get the expected total number of collisions in the array is 1/2.
    So this mean with probability 1/2 we get perfect hashing function, if not we could try again;
    Expected number of trials before we get a perfect hash function is O(1)
    For a static set S, we can support lokups in O(1) worst-case time using O(n^2) space.

Many collisions but linear space: with array of size n, so the expected total number of collisions in the array is (1/2)n
"""

class PerfectHashing(object):
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]
        # self.__p = p


        # TODO

if __name__ == "__main__":
    S=[1,16,41,54,66,96]