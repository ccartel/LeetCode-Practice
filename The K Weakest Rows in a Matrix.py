The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = sorted([(index, sum(row)) for index, row in enumerate(mat)], key=lambda x: (x[1], x[0]))[:k]
        return [index for index,_ in n]
