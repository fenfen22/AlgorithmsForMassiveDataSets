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
"""