# leetcode304 二维区域和检索 - 矩阵不可变
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) # 矩阵有几行
        n = len(matrix[0]) # 矩阵有几列
        if m == 0 or n == 0:
            return
        # 构造前缀和矩阵
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)] #加哨兵方便处理
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                     matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 目标矩阵之和由四个相邻矩阵运算获得
        return (self.preSum[row2 + 1][col2 + 1] - self.preSum[row1][col2 + 1] -
                self.preSum[row2 + 1][col1] + self.preSum[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)