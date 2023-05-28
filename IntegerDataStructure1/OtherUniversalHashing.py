# Dictionary problem: maintain a dynamic set of integers S, which is a subset of U, following operations:
# 1. Lookup(x): return true if x is in S; otherwise return false
# 2. Insert(x): add x in S
# 3. Delete(x): delete x from S

# Goal: a compact data structure with fast operations

"""
data structure of this universal Hashing:
For prime p > 0, 1 < a < p-1; 0 < b < p - 1, we define: TODO

"""

# Time: O(1) expected time per operation(lookup, insert, delete)
# Space: O(n) n elements in the dictionary


import random

class UniversalHashing(object):
    # p is a prime
    def __init__(self, bucket, p):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]
        self.__p = p

    # define other universal hashing function: h
    def hashFunction(self, key, p):
        a = random.randint(1, p-1)
        b = random.randint(0, p-1)
        index = (a*key + b)%p
        return index


    # compute h(x); scan through list for h(x). Return true if x is in list and false otherwise
    def LookupItem(self, key, p):
        index = self.hashFunction(key, p)
        if key not in self.__table[index]:
            return False
        else:
            return True
    
    def InsertItem(self, key, p):
        index = self.hashFunction(key, p)

        # using append function, this element gonna be add at the end of the list
        # self.__table[index].append(key)
        # add this element in the front of this list
        self.__table[index].insert(0, key)
    
    def DeleteItem(self, key, p):
        # compute h(x)
        index = self.hashFunction(key, p)

        # scan through lish for h(x). If x is in list remove it. Otherwise, do nothing
        if key not in self.__table[index]:
            return
            # print("couldnot find the element that you wanna delete")
        else:
            self.__table[index].remove(key)
    
    def DisplayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end=' ')
            for x in self.__table[i]:
                print(" --> %d" % x, end=' ')
            print()

if __name__ == "__main__":
    # elements that you wonna store in the dictionary
    # a_before = [1, 16, 41, 54, 66, 96, 214]
    a_before = [1,11,21,31,41,51,61] 
    bucket_size = 10
    # a = 107
    p = 7 # prime
    h = UniversalHashing(bucket_size,p) 
   
    print(a_before)

    # insert all elements
    for x in a_before:
        h.InsertItem(x, p)

    h.DisplayHash()
    h.InsertItem(3, p)
    h.DisplayHash()
    # h.InsertItem(4, a, m)
    # h.DisplayHash()
    # h.DeleteItem(4, a, m)
    # h.DisplayHash()