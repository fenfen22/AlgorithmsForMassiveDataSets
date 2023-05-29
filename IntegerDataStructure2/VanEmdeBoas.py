"""
Predecessor problem: Maintain a set S, which is a subset of U supporting:
(1) predecessor(x): return the largest element in S that is <= x
(2) successor(x): return the smallest element in S that is >= x
(3) insert(x): add x into S
(4) delete(x): remove x from S

Goal: static predecessor with O(log log u) query time

"""