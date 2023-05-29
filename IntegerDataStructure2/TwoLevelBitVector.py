"""
Predecessor problem: Maintain a set S, which is a subset of U supporting:
(1) predecessor(x): return the largest element in S that is <= x
(2) successor(x): return the smallest element in S that is >= x
(3) insert(x): add x into S
(4) delete(x): remove x from S

"""

"""
Solution 2: Two Level Bitvector

Data Structure: Top bitvector + sqrt(u) bottom bitvectors

Predecessor(x): walk left in bottom + walk left in top + walk left in bottom
Index in top is hi(x) and index in bottom is lo(x)
To find indices in top and bottom, we have x = hi(x)* sqrt(u) + lo(x)

Time O(sqrt(u))
Space O(u)
"""
import math

class TwoLevelBitvector(object):
    def __init__(self,u):
        self.u = u
        self.sqrt_u = int(math.sqrt(u))
        self.top_bits = [0]*(u//self.sqrt_u)
        self.bottom_bits = [[0]*self.sqrt_u for _ in range(u//self.sqrt_u)]
    
    # Top bit vector
    def print_top_bits(self):
        print(self.top_bits)
    
    # Bottom bit vector
    def print_bottom_bits(self):
        print(self.bottom_bits)
    
    # add elements into this data structure
    def set_bits(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u
        self.top_bits[hi_x] = 1
        self.bottom_bits[hi_x][lo_x] = 1
        
    # Remove elements from this data structure
    def clear_bits(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u
        self.top_bits[hi_x] = 0
        self.bottom_bits[hi_x][lo_x] = 0
    

    def predecessor(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u
        # print("pre_hi_x", hi_x)   For testing
        # print("pre_lo_x", lo_x)

        # walk left in the bottom bitvector
        for i in range(lo_x, -1, -1):
            if self.bottom_bits[hi_x][i] == 1:
                return hi_x*self.sqrt_u + i


        # walk left in the top bitvector
        for i in range(hi_x-1, -1, -1):
            if self.top_bits[i] == 1:
                # walk left in the bottom bitvector from the last element of this bottom bitvector
                for j in range(self.sqrt_u-1, -1, -1):
                    if self.bottom_bits[i][j] == 1:
                        return i*self.sqrt_u + j
        
        return False
    
    def successor(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u
        # print("suc_hi_x", hi_x)       the three lines for testing
        # print("suc_lo_x", lo_x)
        # print("sqrt_u", self.sqrt_u)

        # walk right in the bottom bitvector
        for i in range(lo_x, self.sqrt_u, 1):
            if self.bottom_bits[hi_x][i] == 1:
                return hi_x*self.sqrt_u + i


        # walk right in the top bitvector
        for i in range(hi_x + 1, self.sqrt_u, 1):
            if self.top_bits[i] == 1:
                # walk right in the bottom bitvector from the first element of this bottom bitvector
                for j in range(0, self.sqrt_u, 1):
                    if self.bottom_bits[i][j] == 1:
                        return i*self.sqrt_u + j
        return False




if __name__ == "__main__":
    # Initializes the size of the array
    bitvector = TwoLevelBitvector(36)

    # Initializes the array
    elements = [1,3,5,8,6,13,24,27]
    for element in elements:
        bitvector.set_bits(element)
    
    # return the predecessor of element 25
    pre = bitvector.predecessor(25)

    # return the successor of element 14
    suc = bitvector.successor(14)

    print("pre:", pre)
    print("suc:", suc)

    # output the two level bitvector
    bitvector.print_top_bits()
    bitvector.print_bottom_bits()




   