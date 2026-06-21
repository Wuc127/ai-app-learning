# lc509. 斐波那契数
# https://leetcode.cn/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


        # if n <= 1:
        #     return n
        
        # a, b = 0, 1
        
        # for _ in range(2, n + 1):
        #     a, b = b, a + b
        
        # return b


