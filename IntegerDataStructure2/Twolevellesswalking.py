"""
Predecessor problem: Maintain a set S, which is a subset of U supporting:
(1) predecessor(x): return the largest element in S that is <= x
(2) successor(x): return the smallest element in S that is >= x
(3) insert(x): add x into S
(4) delete(x): remove x from S

"""

"""
Solution 3: Two Level Bitvector with Less Walking;

Data Structure: solution 2 with min and max for each bottom structure

Predecessor(x):
If hi(x) in top and lo(x) >= min in bottom[lo(x)] walk left in bottom.
If hi(x) in top and lo(x) < min or hi(x) not in top walk left in top. Return max at first non-empty position in top
So either walk left in bottom or in top;

Time O(sqrt(u))
Space O(u)

for each bottom bitvector, we use the first "position [0]" to store the mininal value of this bottom bitvector;
and use the second "position [1]" to store the maximal value of this bottom bitvector.
"""
import math

class TwoLevelBitvectorLessWalking(object):
    def __init__(self,u):
        self.u = u
        self.sqrt_u = int(math.sqrt(u))
        self.top_bits = [0] * ((u + self.sqrt_u - 1) // self.sqrt_u)  # Top-level bitvector
        self.bottom_bits = [[0] * (self.sqrt_u+2) for _ in range((u + self.sqrt_u - 1) // self.sqrt_u)]  # Bottom-level bitvectors
    
    # Top bit vector
    def print_top_bits(self):
        print(self.top_bits)
    
    # Bottom bit vector
    def print_bottom_bits(self):
        print(self.bottom_bits)
        # print(self.sqrt_u)
    
    # add elements into this data structure
    def set_bits(self,x):
        hi_x = x // self.sqrt_u
        lo_x = (x % self.sqrt_u) + 2

        self.top_bits[hi_x] = 1
        self.bottom_bits[hi_x][lo_x] = 1

        if self.bottom_bits[hi_x][0] == 0:
            self.bottom_bits[hi_x][0] = hi_x*self.sqrt_u + lo_x - 2
        else:
            self.bottom_bits[hi_x][0] = min(self.bottom_bits[hi_x][0], hi_x*self.sqrt_u + lo_x - 2)    # min value of this array
        

        if self.bottom_bits[hi_x][1] == 0:
            self.bottom_bits[hi_x][1] = hi_x*self.sqrt_u + lo_x - 2
        else:
            self.bottom_bits[hi_x][1] = max(self.bottom_bits[hi_x][1], hi_x*self.sqrt_u + lo_x - 2)    # min value of this array

        
    # Remove elements from this data structure
    def clear_bits(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u + 2
        self.top_bits[hi_x] = 0
        self.bottom_bits[hi_x][lo_x] = 0
    

    def predecessor(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u + 2
        # print("pre_hi_x", hi_x)  # For testing
        # print("pre_lo_x", lo_x)

        if hi_x*self.sqrt_u + lo_x - 2 >= self.bottom_bits[hi_x][0]:
            # If this value larger than or equla to the smallest one, then walk left in the bottom bitvector
            for i in range(lo_x, 1, -1):
                if self.bottom_bits[hi_x][i] == 1:
                    return hi_x*self.sqrt_u + i - 2
        else: #else, then walk left in the top bitvector
            for i in range(hi_x-1, -1, -1):
                if self.top_bits[i] == 1:
                    return self.bottom_bits[i][1]
        
        return False
    
    def successor(self,x):
        hi_x = x // self.sqrt_u
        lo_x = x % self.sqrt_u + 2
        # print("suc_hi_x", hi_x)       the three lines for testing
        # print("suc_lo_x", lo_x)
        # print("sqrt_u", self.sqrt_u)


        if hi_x*self.sqrt_u + lo_x - 2 <= self.bottom_bits[hi_x][1]:
            # If this value smaller than or equla to the largest one, then walk right in the bottom bitvector
            for i in range(lo_x, self.sqrt_u + 2, 1):
                if self.bottom_bits[hi_x][i] == 1:
                    return hi_x*self.sqrt_u + i - 2
        else: # else, then walk right in the top bitvector
            for i in range(hi_x+1, self.sqrt_u + 2, 1):
                if self.top_bits[i] == 1:
                    return self.bottom_bits[i][0]
        return False




if __name__ == "__main__":
    # Initializes the size of the array
    bitvector = TwoLevelBitvectorLessWalking(39)

    # Initializes the array
    elements = [1,3,5,8,6,13,24,27]
    for element in elements:
        bitvector.set_bits(element)
    
    # return the predecessor of element 12
    pre = bitvector.predecessor(12) # walk left in the top bitvector

    # return the successor of element 9
    suc = bitvector.successor(9) # walk right in the top bitvector

    print("pre:", pre)
    print("suc:", suc)

    bitvector.print_top_bits()
    bitvector.print_bottom_bits()