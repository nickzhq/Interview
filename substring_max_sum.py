# coding=utf-8


def substring_max_sum(int_list):
    """
    该方法只能处理当前数组仅有一个和最大的连续连续子序列
    f(x) = input[x] ,x = 0 or f(x-1) < 0;
           f(x-1) + input[x], x != 0 and f(x-1) > 0
    :param int_list:
    :return: int
    """
    res = [int_list[0]]
    begin_idx = 0
    count = 1
    for idx in xrange(1, len(int_list)):
        if res[idx - 1] < 0:
            res.append(int_list[idx])
            begin_idx = idx
            count = 1
        elif res[idx - 1] >= 0:
            res.append(res[idx - 1] + int_list[idx])
            count += 1

    # print "begin_idx: " + str(begin_idx) + "  count:" + str(count)
    print int_list[begin_idx:begin_idx + count]
    print res
    return max(res)


def substring_max_sum_v2(int_list):
    """
    该方法只能处理数组中有多个和最大的连续连续子序列
    f(x) = input[x] ,x = 0 or f(x-1) < 0;
           f(x-1) + input[x], x != 0 and f(x-1) > 0
    :param int_list:
    :return: int
    """
    dp = [int_list[0]]
    dict = {dp[0]: [[int_list[0]]]}
    begin_idx = 0
    count = 1
    for idx in xrange(1, len(int_list)):
        if dp[idx - 1] < 0:
            dp.append(int_list[idx])
            begin_idx = idx
            count = 1
        elif dp[idx - 1] >= 0:
            dp.append(dp[idx - 1] + int_list[idx])
            count += 1

        # 每次记录计算结果
        if dp[idx] in dict:
            dict[dp[idx]].append(int_list[begin_idx:begin_idx + count])
        else:
            dict[dp[idx]] = [int_list[begin_idx:begin_idx + count]]

    # print "begin_idx: " + str(begin_idx) + "  count:" + str(count)
    # print int_list[begin_idx:begin_idx+count]
    print dict
    print dp
    return dict[max(dict.keys())]


if __name__ == '__main__':
    print substring_max_sum_v2([1, -2, 3, 10, -4, 7, 2, -500, 18, -4, 2])
    """
    s = "ADSFrew"
    s.lower()
    with open("unittest_test.py", "r") as f:
        for line in f.readlines():
            print line
    """
    # s = "abcdef"
    # print s[2:1]
    # for idx, ele in enumerate(s):
    #     print str(idx) + "    " + ele
