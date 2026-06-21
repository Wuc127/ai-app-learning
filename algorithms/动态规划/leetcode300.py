# lc300 最长递增子序列
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 1

        dp = [1] * len(nums)  #这里不能初始化0

        for i in range(1, len(nums)):
            for j in range(0, i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1) 
        res=0
        for i in range(0, len(nums)):
            res = max(res, dp[i])

        return res