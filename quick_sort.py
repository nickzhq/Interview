# coding=utf-8
import random


def quick_sort(int_list, idx_left, idx_right):
    if idx_left >= idx_right:
        return
    pivot = partition(int_list, idx_left, idx_right)
    quick_sort(int_list, idx_left, pivot - 1)
    quick_sort(int_list, pivot + 1, idx_right)

    return int_list


def partition(int_list, idx_left, idx_right):
    pivot = int_list[idx_right]
    low = idx_left
    high = idx_right - 1
    while low <= high:
        if int_list[low] < pivot:
            low += 1
        elif int_list[high] >= pivot:
            high -= 1
        else:
            int_list[low], int_list[high] = int_list[high], int_list[low]
            low += 1
            high -= 1

    # 将基准添加回list
    int_list[low], int_list[idx_right] = int_list[idx_right], int_list[low]
    return low


if __name__ == '__main__':
    li = [1, 3, 2, -1, 0, 199, 65, -90, 100, 602, -87, 0, 1, 1, 77, 34]
    # res = quick_sort(li, 0, len(li) - 1)
    # print res
    num1 = random.randrange(0, len(li))  # randrange范围 [start, stop)
    print num1
