# coding=utf-8
# @Time     : 22th November, 2019  17:54
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : integer_break_II.py
# @Software : PyCharm 
# =======================================================

"""
设n是一个正整数。现在要求将n分解为若干个自然数之积，使得自然数的和最小。输出这个最小的和。
要求:
*****暂不考虑:（1）要求这些自然数互不相同******
（2）要求这些自然数可以是相同的
"""

# 解题方法来自integer_break.py文件中动态规划公式的推导过程，和这道题属于"同根生"
def integer_break_II(n):
    res = 0
    dp = [n for i in xrange(n + 1)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 4
    for i in xrange(4, n + 1):
        for j in xrange(1, i):
            if i % j == 0:
                # 因为dp[i]保存了每次的结果，同时由于涉及到了同一个位置多次比较，所以dp[i]被写在了min()中
                dp[i] = min(dp[i], dp[i / j] + j, i / j + j)

    return dp[-1]


if __name__ == '__main__':
    for i in xrange(4, 140):
        print str(i) + " : " + str(integer_break_II(i))
