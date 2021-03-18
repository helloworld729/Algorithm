from typing import List
class Solution:
    def maxValue1(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        if not m * n: return 0

        cans = list()
        res = 0
        cans.append([(0, 0), grid[0][0]])

        while cans:
            (i, j), value = cans.pop()
            res = max(res, value)
            for (ii, jj) in [(i + 1, j), (i, j + 1)]:
                if 0 <= ii <= m - 1 and 0 <= jj <= n - 1:
                    cans.append([(ii, jj), value + grid[ii][jj]])
        return res

    def maxValue2(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * (1 + n) for i in range(m + 1)]  # 哨兵

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = grid[i][j] + max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

grid = [
            [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
            [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
            [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
            [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
            [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
            [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
            [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
            [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
            [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
            [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
            [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
            [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9] ]

print(Solution().maxValue2(grid)) # m*n
print(Solution().maxValue1(grid)) # 超时



