# Dictionary problem: maintain a dynamic set of integers S, which is a subset of U, following operations:
# 1. Lookup(x): return true if x is in S; otherwise return false
# 2. Insert(x): add x in S
# 3. Delete(x): delete x from S

# Goal: a compact data structure with fast operations

"""
data structure of the universal Hashing:
(1) H is a family of functions mapping U to {0,...,m-1}.
(2) For any x != y in U and h chosen uniformly at random in H, we have Pr(h(x) = h(y)) <= 1/m

the definition of hash function defined as follow: (Universal hashing)
Given a prime m and a = (a_1 a_2 a_3 ... a_r)_m, we define 

"""

# Time: O(1) expected time per operation(lookup, insert, delete)
# Space: O(n) n elements in the dictionary
def base_m_representation(x, m):
        if m < 2 or not isinstance(m, int):
            raise ValueError("m must be a prime number greater than or equal to 2.")
        if x == 0:
            return [0]
        result = []
        while x > 0:
            remainder = x % m
            result.append(remainder)
            x = x // m # floor division operator
        return result[::-1] # return the result list in reverse order

class UniversalHashing(object):
    def __init__(self, bucket, a, m):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]
        self.__a = a
        self.__m = m

    # define hash function: h
    """
    m is a prime
    we use base-m representation to rewrite x and a  (x written in base m; same for a)
    """
    def hashFunction(self, key, a, m):
        aBaseM = base_m_representation(a, m)
        keyBaseM = base_m_representation(key, m)
        result = 0
        for index1,index2 in zip(aBaseM,keyBaseM):
            result += index1*index2
        return result % m


    # compute h(x); scan through list for h(x). Return true if x is in list and false otherwise
    def LookupItem(self, key, a, m):
        index = self.hashFunction(key, a, m)
        if key not in self.__table[index]:
            return False
        else:
            return True
    
    def InsertItem(self, key, a, m):
        index = self.hashFunction(key, a, m)

        # using append function, this element gonna be add at the end of the list
        # self.__table[index].append(key)
        # add this element in the front of this list
        self.__table[index].insert(0, key)
    
    def DeleteItem(self, key, a, m):
        # compute h(x)
        index = self.hashFunction(key, a, m)

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
    a = 107
    m = 7 # prime
    h = UniversalHashing(bucket_size,a,m) 
   
    print(a_before)

    # insert all elements
    for x in a_before:
        h.InsertItem(x, a, m)

    h.DisplayHash()
    h.InsertItem(3, a, m)
    h.DisplayHash()
    # h.InsertItem(4, a, m)
    # h.DisplayHash()
    # h.DeleteItem(4, a, m)
    # h.DisplayHash()