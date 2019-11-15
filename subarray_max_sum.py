# coding = utf-8
def substring_max_sum(int_list):
    """
    f(x) = input[x] ,x = 0 or f(x-1) < 0;
           f(x-1) + input[x], x != 0 and f(x-1) > 0
    :param int_list:
    :return: int
    """
    res = [int_list[0]]
    begin_idx = 0
    count = 0
    for idx in xrange(1, len(int_list)):
        if res[idx-1] < 0:
            res.append(int_list[idx])
            begin_idx = idx
            count = 0
        elif res[idx-1] >= 0:
            res.append(res[idx-1] + int_list[idx])
            count += 1

    print "begin_idx: " + str(begin_idx) + "  count:" + str(count)
    print int_list[begin_idx:begin_idx+count]
    return max(res)


if __name__ == '__main__':
    print substring_max_sum([1, -2, 3, 10, -4, 7, 2, -5])

