class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        dp = [[None for _ in range(r)] for _ in range(c)]  # Swap rows and columns
        
        for i in range(r):
            for j in range(c):
                dp[j][i] = matrix[i][j]  # Reversed indices for correct assignment
                
        return dp
