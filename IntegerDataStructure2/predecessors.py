"""
Predecessor problem: Maintain a set S, which is a subset of U supporting:
(1) predecessor(x): return the largest element in S that is <= x
(2) successor(x): return the smallest element in S that is >= x
(3) insert(x): add x into S
(4) delete(x): remove x from S

"""

"""
Solution 1: Bitvector
Just walk left
Time O(u)
Space O(u)
"""
from array import array

class Bitvector(object):
    def __init__(self,size):
        self.my_array = [0]*size
        # print(self.my_array)
    
    def add_element(self, element):
        for x in element:
            self.my_array[x] = 1
    
    def print_array(self):
        print(self.my_array)
    
    def BVpredecessor(self, value):
        while value >= 0:
            if self.my_array[value] == 1:
                return value
            else:
                value= value - 1
        return False

    def BVsuccessor(self, value):
        while value < len(self.my_array):
            if self.my_array[value] == 1:
                return value
            else:
                value= value + 1
        return False


if __name__ == "__main__":
    # Initializes the size of the array
    BitVector = Bitvector(40)

    # Initializes the array
    BitVector.add_element([1,3,5,8,6,13,24,27])

    # Output the array
    BitVector.print_array()

    # return the predecessor of element 7
    pre = BitVector.BVpredecessor(0)

    # return the successor of element 10
    suc = BitVector.BVsuccessor(27)

    print("pre:", pre)
    print("suc:", suc)




