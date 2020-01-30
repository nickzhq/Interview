# coding=utf-8
# 输入任何正整数，返回有多少种组合方式(仅用 1，2，5数字组成)


def triple_loop_v1(int_target):
    res = 0
    for c in xrange(0, int_target + 1, 5):
        for b in xrange(0, int_target + 1, 2):
            for a in xrange(0, int_target + 1):
                if a + b + c == int_target:
                    res += 1

    return res


def triple_loop_v2(int_target):
    res = 0
    for c in xrange(0, int_target + 1, 5):
        for b in xrange(0, int_target + 1 - c, 2):
            for a in xrange(0, int_target + 1 - c - b):
                if a + b + c == int_target:
                    res += 1

    return res


def triple_loop_v3(int_target):
    res = 0
    for c in xrange(0, int_target + 1, 5):
        for b in xrange(0, int_target + 1 - c, 2):
            res += 1

    return res


def triple_loop_v4(int_target):
    res = 0
    for c in xrange(0, int_target + 1, 5):
        res += (int_target - c) / 2 + 1

    return res


'''
x + 5z = 100 - 2y
推论出: x+5z <= 100 且 x+5z且一定为偶数
基于上两个推论，接下来枚举数值解
z=0, x可为 100, 98，96。。。。。0
z=1, x可为 95, 93, 91.........1
....
....
....
z=19, x可为 5, 3, 1
z=20, x可为 0
偶数M包含的偶数( 0也要包含 )一共有 M/2 + 1
基数M包含的基数一共有: (M+2) / 2
两个公式都可以变成 (M+2)/2
'''
def triple_loop_math(int_target):
    res = 0
    for m in xrange(0, int_target + 1, 5):
        res += (m+2)/2
    return res


if __name__ == '__main__':
    print (triple_loop_v1(100))
    print (triple_loop_v2(100))
    print (triple_loop_v3(100))
    print (triple_loop_v4(100))
    print (triple_loop_math(100))
