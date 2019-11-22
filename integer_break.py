# coding=utf-8
# @Time     : 22th November, 2019  12:19
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : integer_break.py
# @Software : PyCharm 
# =======================================================

"""
设n是一个正整数。现在要求将n分解为若干个自然数之和，使得自然数的成绩最大。输出这个最大的乘积。
要求:
（1）要求这些自然数互不相同
（2）要求这些自然数可以是相同的
"""


def integer_break_into_unique_number(n):
    res = 1
    record = []
    ele = 2
    while n >= ele:
        n -= ele
        record.append(ele)
        ele += 1

    """
    如果有多出来的，从后往前均匀分配到各个元素。
    考虑到一种特殊情况( 此时循环相减后剩余的n一定满足: N >= len(record) )，当多出来的数比前面已有元素的个数大1时（比如8的情况）:
        这个时候依旧先均匀分配到每个元素(即每个元素加1)，那么这个时候还剩个1，就直接给到已有元素的最大元素加1，
    """
    if n > 0:
        idx = len(record) - 1
        while n > 0 and idx >= 0:
            record[idx] += 1
            n -= 1
            idx -= 1

        record[-1] += n  # 此时的n要么是0，要么是1

    print record
    for idx in xrange(len(record)):
        res *= record[idx]

    return res


def integer_break_into_repeatable_number(n):
    """
    仍然是通过手写几个数查看一下规律：4=2+2，5=2+3，6=3+3，7=3+2+2，8=3+3+2，9=3+3+3。
    发现规律如下：
    （1）元素不会超过4，因为4=2+2，又可以转化为2的问题，而5=2+3，5<2*3，所以5总能分解成2和3。
    （2）尽可能多分解出3，然后分解出2，不要分出1。
    考虑任意一个数，除以3之后的结果有以下3种：
    （1）能被3除断，那么就分解为3+3+...+3的情况即可。例如9=3+3+3。
    （2）被3除余1，分解为3+3+...+3+2+2或者3+3+...+3+4的情况，例如10=3+3+2+2
    （3）被3除余2，分解为3+3+...+3+2的情况，例如11=3+3+3+2。

    :param n:
    :return:
    """
    record = []
    res = 1

    while n >= 3:
        n -= 3
        record.append(3)
    """
    if n != 0:
        if n == 1:
            n += record.pop()
        
        while n >= 2:
            record.append(2)
            n -= 2
    """
    # 将上述代码优化可得
    if n == 1:
        n += record.pop()
    while n >= 2:
        record.append(2)
        n -= 2

    print record
    for idx in xrange(len(record)):
        res *= record[idx]

    return res


def integer_break_by_dp(n):
    dp = [-1 for _ in xrange(n + 1)]
    dp[1] = 1
    dp[2] = 1
    """
    dp[i]=max{dp[i-1]*1,dp[i-2]*2,...,dp[i-(i-1)]*(i-1),(i-1) * 1,(i-2) * 2,(i-3)*3,.....(i) * (i-1)}
    观察上面这个公式，可发现：
        公式的后半段(i-1) * 1,(i-2) * 2,(i-3)*3,.....(i) * (i-1) 其实把数字N拆成了2个相乘
        还有情况是多个数字相乘，此时就要依靠动态规划帮忙，公式前半段作用发挥dp[i-1]*1,dp[i-2]*2,...,dp[i-(i-1)]*(i-1)
        数字越大，能被拆成的部分就越多；数字越小，能被拆分的部分就越少，所以任何一个数字肯定都是被从拆成两个部分开始的
    """
    for i in xrange(3, n + 1):
        for j in xrange(1, i):
            dp[i] = max(dp[i], j * dp[i - j], j * (i - j))

    return dp[-1]


if __name__ == '__main__':
    """
    print "n=15 :" + str(integer_break_into_unique_number(15))
    print "n=11 :" + str(integer_break_into_unique_number(11))
    print "n=10 :" + str(integer_break_into_unique_number(10))
    print "n=9 :" + str(integer_break_into_unique_number(9))
    print "n=8 :" + str(integer_break_into_unique_number(8))
    print "n=7 :" + str(integer_break_into_unique_number(7))
    print "n=6 :" + str(integer_break_into_unique_number(6))
    """
    """
    print "n=10 :" + str(integer_break_into_repeatable_number(10))
    print "n=9 :" + str(integer_break_into_repeatable_number(9))
    print "n=8 :" + str(integer_break_into_repeatable_number(8))
    print "n=7 :" + str(integer_break_into_repeatable_number(7))
    print "n=6 :" + str(integer_break_into_repeatable_number(6))
    """
    print integer_break_into_repeatable_number(6)
    print integer_break_by_dp(6)
    print "-----------------"
    print integer_break_into_repeatable_number(7)
    print integer_break_by_dp(7)
    print "-----------------"
    print integer_break_into_repeatable_number(8)
    print integer_break_by_dp(8)
    print "-----------------"
    print integer_break_into_repeatable_number(9)
    print integer_break_by_dp(9)
    print "-----------------"
