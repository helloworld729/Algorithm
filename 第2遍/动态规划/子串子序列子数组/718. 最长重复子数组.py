"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
"""
class Solution:
    def findLength(self, A, B) -> int:
        res = 0
        la, lb = len(A), len(B)
        for i in range(la):
            for j in range(lb):
                if A[i] == B[j]:
                    count = 0
                    while la > i+count and lb > j+count and A[i+count] == B[j + count]:
                        count += 1
                        res = max(res, count)
        return res
    def findLength2(self, A, B) -> int:
        """空间二维动规 if same: dp[j][i] = dp[j+1][i+1]+1  25%"""
        la, lb = len(A), len(B)
        if not la*lb: return 0
        res = 0
        dp = [[0]*la  for j in range(lb)]
        for j in range(lb-1, -1, -1):  # up<--down
            for i in range(la):  # left-->right
                candy = dp[j+1][i+1] if (j+1 <= lb-1 and i+1 <= la-1) else 0
                dp[j][i] = candy + 1 if A[i] == B[j] else 0
                res = max(res, dp[j][i])
        return res
    def findLength2(self, A, B) -> int:
        """优化空间复杂度，降维  50%"""
        """处理边界问题，与其增加判断语句，不容对list扩充"""
        la, lb = len(A), len(B)
        if not la*lb: return 0
        res = 0
        dp = [0]*(la+1)
        for j in range(lb-1, -1, -1):  # up<--down
            for i in range(la):  # left-->right
                dp[i] = dp[i+1]+1 if A[i] == B[j] else 0
                res = max(res, dp[i])
        return res
