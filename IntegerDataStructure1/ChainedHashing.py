# Dictionary problem: maintain a dynamic set of integers S, which is a subset of U, following operations:
# 1. Lookup(x): return true if x is in S; otherwise return false
# 2. Insert(x): add x in S
# 3. Delete(x): delete x from S

# Goal: a compact data structure with fast operations

# data structure of chained hash: 
# (1) Initialize an array A[0,..., m-1]
# (2) A[i] stores a linked list containing the keys in S whose hash value is i

""" There is a shortcoming of this data structre. To be more specific, For any fixed choice of h,
there is a set whose elements all map to the same slot. Finally, we end up with a single linked list

For example: we could set bucket_size = 10; a = [1,11,21,31,41,51,61] 
"""

# Time: O(1 + length of linked list for h(x))
# Space:O(n)

class ChainedHash(object):
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]

    # compute h(x)
    def hashFunction(self, key):
        return (key % self.__bucket)

    # compute h(x); scan through list for h(x). Return true if x is in list and false otherwise
    def LookupItem(self, key):
        index = self.hashFunction(key)
        if key not in self.__table[index]:
            return False
        else:
            return True
    
    def InsertItem(self, key):
        index = self.hashFunction(key)

        # using append function, this element gonna be add at the end of the list
        # self.__table[index].append(key)
        # add this element in the front of this list
        self.__table[index].insert(0, key)
    
    def DeleteItem(self, key):
        # compute h(x)
        index = self.hashFunction(key)

        # scan through lish for h(x). If x is in list remove it. Otherwise, do nothing
        if key not in self.__table[index]:
            return
            # print("couldnot find the element that you wanna delete")
        self.__table[index].remove(key)
    
    def DisplayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end=' ')
            for x in self.__table[i]:
                print(" --> %d" % x, end=' ')
            print()

if __name__ == "__main__":
    # elements that you wonna store in the dictionary
    a = [1, 16, 41, 54, 66, 96]
    # a = [1,11,21,31,41,51,61] #test the shortcoming of the chained hash
    bucket_size = 10
    h = ChainedHash(bucket_size)

    for x in a:
        h.InsertItem(x)

    h.DisplayHash()
    h.DeleteItem(1)
    h.DisplayHash()
    h.DeleteItem(96)
    h.DisplayHash()