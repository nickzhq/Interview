# coding=utf-8
# 四则运算器
def get_value(num1, num2, opt):
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    else:
        return num1 / num2


def process_data(data, opt):
    opt_top = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(get_value(num1, num2, opt_top))


def priority_compare(opt1, opt2):
    """
    :param opt1:
    :param opt2:
    :return: 若opt1优先级高于opt2, 返回true， 否则返回false。四则运算中，乘除为高，加减为低。所以目前想到一种比对方法opt1是乘除,opt2是加减
    """
    return opt1 in ["*", "/"] and opt2 in ["+", "-"]


def calculate(str_input):
    data = []  # 数字栈
    opt = []  # 操作符栈, 这个栈维持操作符优先级从低到高，保持这个秩序，若出现有低优先级进栈时，要先把栈之前的数据清空，然后再入栈，依旧是维持优先级从低到高的顺序
    idx = 0
    while len(str_input) > idx:
        if str_input[idx].isdigit():  # 数字，入栈data
            start = idx
            while idx + 1 < len(str_input) and str_input[idx + 1].isdigit():
                idx += 1
            data.append(int(str_input[start:idx + 1]))
        elif not opt or opt[-1] == "(":  # 若opt为空或者栈顶为(, 不问理由直接入栈
            opt.append(str_input[idx])
        elif str_input[idx] == "(" or priority_compare(str_input[idx], opt[-1]):  # 当前操作符为( 或者 比栈顶操作符优先级高，操作符直接入栈opt
            opt.append(str_input[idx])
        elif str_input[idx] == ")":
            while opt[-1] != "(":
                process_data(data, opt)
            opt.pop()
        else:  # 优先级不比栈顶操作符高时，opt出栈同时data出栈并计算，计算结果如栈data
            while opt is not None and not priority_compare(str_input[idx], opt[-1]):
                if opt[-1] == "(":
                    break
                process_data(data, opt)
            opt.append(str_input[idx])
        idx += 1

    while opt:
        process_data(data, opt)

    return data[-1]


if __name__ == '__main__':
    exp = "(9+((3-1)*3+10/2))*2"
    # print calculate(exp)
    print 5/2
    9223372036854775807
