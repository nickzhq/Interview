# coding = utf-8
import sys

def func(list_input):
    # rec = float('inf')
    rec = sys.maxsize
    idx_rear = - 1
    size = len(list_input)
    idx_front = 0
    count = 0
    while idx_front - idx_rear != size:

        if rec == rec ^ list_input[idx_front]:
            idx_front += 1
        else:
            temp = list_input[idx_front]
            del(list_input[idx_front])
            list_input.append(temp)
            idx_rear -= 1

    return list_input


if __name__ == '__main__':
    print( func([1, 6, 5, 3,5, 3, 6, 2, 100,   1, 1, 0, 3]) )
