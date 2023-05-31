import random

"""
# This file contains three class, which are HashFunction, SecondaryHT, PerfectHT.
# 
# HashFunction: generate universal hashing function randomly based on the number of elements in a specific set
# 
# SecondaryHT: collision-free solution, goal of this is to resolve collisions at level 1.
# while NOW, we could not guarantee "collision-free". With probability 1/2, we could get perfect hashing function, TODO if not perfect try again.
# 
# PerfectHT: TODO isMember doesn't work now
# 
# The perfect hashing could work! While there are still some problems:
#
# 
# 
"""
class HashFunction:
    def __init__(self,n):
        self.m_tize = self.findPrime(n) # table size, must be a prime
        self.m_factor = random.randint(1, n-1)  # must have 0 < m_factor < m_tize
        self.m_shift = random.randint(0, n-1)   # must have 0 <= m_shift < m_tize
        self.m_multiplier = 33 # magic number from textbook # used in hashCode function
        # self.m_reboots = 0 # number of times reboot() was called TODO
        
    """ 
    Pass in requested hash table size via parameter n.
    The constructor picks the smallest prime, which is greater than or equal to n for the table size
    Initializes other hash function parameters randomly
    """
    """
    # TODO
    Function that maps string to int; return value can be much larger than table size; uses m-multiplier data member
    """

    def __call__(self, key):
        return (self.m_factor * key + self.m_shift) % self.m_tize

    def findPrime(self, m):
        # find smallest prime nuber greater than or equal to m
        if m < 2:
            return 2  # Smallest prime is 2

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        while True:
            if is_prime(m):
                return m
            m += 1

# Secondary hash table for PerfectHT class
class SecondaryHT(object):
    def __init__(self, input_array):
        self.s = len(input_array) * len(input_array) # double size
        self.h = HashFunction(self.s)
        self.m_tize = self.h.m_tize
        self.array = [None]*(self.s + 1) # index starts at 0, might out of the range, so we need + 1
        # print("len of the array", len(self.array))

        for ele in input_array:
            # print(self.h(ele))
            self.array[self.h(ele)] = ele
 
    def isMember(self, key):
        index = self.h(key)
        print("index:", index)

        if self.array[index] == key:
            return True
            # print("Find it!") # For testing
        else:
            return False
            # print("Could not Find it!")


class PerfectHT(object):
    def __init__(self,n):
        # create a perfect hashing table using n elements randomly generated
        self.random_integers = []
        for _ in range(n):
            random_int = random.randint(0, 100)
            self.random_integers.append(random_int)
        
        print("Integer randomly generated:", self.random_integers)
        
        self.h = HashFunction(n)
        self.result =[[] for _ in range(self.h.m_tize)]
        
        for ele in self.random_integers:
            self.result[self.h(ele)].append(ele)
        
        # print("result table:", self.result) # For testing the result table
        
        for index, arr in enumerate(self.result):
            # if the array is not empty
            if len(arr) > 1:
                self.secarry = self.SecondaryHT(arr)
                self.result[index] = self.secarry.array
                
    def isMember(self, key):
        FirstIndex = self.h(key)
        arry = self.result[FirstIndex]
        secindex = self.SecondaryHT(arry)
        if secindex.isMember(key):
            return True
    
    def printPerfecHT(self):
        for i in range(self.h.m_tize):
            print("[%d]" % i, end=' ')
            for x in self.result[i]:
                print(" --> %s" % x, end=' ') # output as a string
            print()
    


if __name__ == "__main__":
    # S=[1,16,41,54,66,96]
    # # stringsss=["apple","banana","red","black","pink"] # TODO
    # h = HashFunction(10)
    # print("tize",h.m_tize) 
    # print("factor",h.m_factor)
    # print("shift",h.m_shift)
    # print("multiplier",h.m_multiplier)

    # a = [1,2,3]
    # sec = SecondaryHT(a)
    # print(sec)
    # print("s:", sec.s)
    # print("array:", sec.array)
    # print("m_tize:", sec.m_tize)
    # sec.isMember(1)
    # sec.isMember(2)
    # sec.isMember(3)
    # sec.isMember(5)

    # for string in S:
    #     print(h(string))

    # # for perfect hashing
    per = PerfectHT(10)
    # print(per.random_integers)
    # print(per.result)
    per.printPerfecHT()





