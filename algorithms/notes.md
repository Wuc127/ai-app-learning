# 算法学习笔记与做题记录

## 数组

### 滑动窗口

leetcode76 题最小覆盖子串笔记：

get 是 Python 字典（dict）的一个方法，用来安全地获取字典中某个键的值，如果键不存在则返回一个默认值。基本语法
```python
字典.get(键, 默认值)
```
```py
if c in need:
    need[c] = need[c] + 1  
else:
    need[c] = 0 + 1       
```
等价于
```py
need[c] = need.get(c, 0) + 1
```
---

[start:start + length] 是 Python 的切片语法，用来从字符串中截取一段子串。基本格式
```python
字符串[起始索引:结束索引]
# 注意：包含起始，不包含结束
```
s[start:start + length] 的含义
```python
s[start:start + length]
# 从 start 开始，取 length 个字符
```

具体例子
```python
s = "ADOBECODEBANC"
start = 9
length = 4

s[9:9+4] = s[9:13]
#          索引: 9, 10, 11, 12
#          字符: B,  A,  N,  C
#          结果: "BANC"
```

### 前缀和
```py
self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
```
等价
```py
self.preSum = []                        # 创建一个空列表
for _ in range(m + 1):                  # 循环 m+1 次
    row = [0] * (n + 1)                 # 每次创建一个长度为 n+1 的行（一维列表）
    self.preSum.append(row)             # 把这行添加到 self.preSum 里
```
[0] * (n + 1)：创建一个长度为 n+1 的一维列表，里面全是 0。

例如 n=3，则 [0, 0, 0, 0]。

for _ in range(m + 1)：把“创建一行”这个动作重复 m+1 次。

把每次创建的行收集到一个外层列表里，就得到了一个二维列表（即矩阵）。

## 二叉树 & 递归思想

### leetcode543. 二叉树的直径

实例变量在哪个方法里创建都行，一旦创建，同一个实例的所有方法都能访问和修改。但必须在使用之前创建，否则报错！无论嵌套函数还是实例方法，只要通过 self.diameter 访问，就是同一个实例变量，所有方法共享！

```py
class Solution:
    def methodA(self):
        self.diameter = 100  # 在 methodA 中创建
        print(f"methodA 创建: {self.diameter}")
    
    def methodB(self):
        print(f"methodB 访问: {self.diameter}")  # 可以访问！
    
    def methodC(self):
        self.diameter = 200  # 甚至可以修改
        print(f"methodC 修改: {self.diameter}")

# 使用
sol = Solution()
sol.methodA()   # 输出: methodA 创建: 100
sol.methodB()   # 输出: methodB 访问: 100  ✅ 能访问到
sol.methodC()   # 输出: methodC 修改: 200
sol.methodB()   # 输出: methodB 访问: 200  ✅ 被修改了
```

实例变量的生命周期:
```py
创建实例 → 实例变量诞生 → 所有方法共享 → 实例销毁 → 变量消失

sol = Solution()  # 创建实例
                ↓
     (此时还没有 diameter)
                ↓
sol.methodA()    # self.diameter = 100  ← 变量诞生
                ↓
sol.methodB()    # 可以读取 100
                ↓
sol.methodC()    # 可以修改成 200
                ↓
del sol          # 实例销毁，diameter 消失
```


使用实例变量前必须先初始化,错误示例：
```py
class Solution:
    def maxDepth(self, node):
        # 这里试图读取 self.diameter
        self.diameter = max(self.diameter, left + right)  # ❌ 问题在这里
        # 当 self.diameter 还不存在时，max() 无法读取它
    
    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)  # 直接调用 maxDepth，但此时 self.diameter 还不存在
```

```
调用 diameterOfBinaryTree
    ↓
直接调用 self.maxDepth()
    ↓
maxDepth 里读取 self.diameter
    ↓
❌ 报错！self.diameter 还不存在
```
---

正确做法:
```py
class Solution:
    def maxDepth(self, node):
        # 此时 self.diameter 已经存在了（在调用前就被创建了）
        self.diameter = max(self.diameter, left + right)  # ✅ 没问题
    
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # ← 关键：先创建并初始化
        self.maxDepth(root)  # 然后再调用 maxDepth
        return self.diameter
```

```
调用 diameterOfBinaryTree
    ↓
self.diameter = 0  ← 先创建
    ↓
调用 self.maxDepth()
    ↓
maxDepth 里读取 self.diameter
    ↓
✅ 成功！值是 0
```
self.diameter 在 diameterOfBinaryTree 中被创建，然后在 maxDepth 中被反复读取和覆盖，所有方法共享同一个实例变量！
例子：
```py
class Solution:
    def maxDepth(self, node):
        # 左侧换了个名字
        self.result = max(self.diameter, left + right)
        #               ↑ 读取这个     ↑ 赋值给这个（新建）
        print(f"diameter 还是: {self.diameter}")  # 没变
        print(f"result 是: {self.result}")        # 新变量
    
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.maxDepth(root)
        print(f"最终 diameter: {self.diameter}")  # 还是 0？不对...
        return self.diameter  # 会返回 0，错误！
```

```py
# ❌ 错误：换名字后，直径没有被记录
self.result = max(self.diameter, left + right)
# 最后 return self.diameter 还是 0

# ✅ 正确：同名才能覆盖更新
self.diameter = max(self.diameter, left + right)
# 最后 return self.diameter 才是正确答案
```
左侧换名字就等于新建一个实例变量，不会覆盖原来的 self.diameter。要覆盖更新，必须用同名变量！

---

max(self.diameter, ...) 需要先读取旧值才能计算新值，所以 self.diameter 必须在执行这行代码之前就已经存在。不能在读取的同时创建！
```py
self.diameter = max(self.diameter, left + right)
#                ↑                ↑
#            要读取旧值        要写入新值
```
执行顺序：
```
1.先计算右边的 max(self.diameter, ...)
2.计算时需要读取 self.diameter 的当前值
3.如果 self.diameter 还不存在 → ❌ 报错
4.然后才把计算结果赋值给 self.diameter
```

