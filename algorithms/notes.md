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

