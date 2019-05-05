import random
import string

"""
生成随机字符串 可以当激活码使用
"""


def gen_rand_item():
    rand_str = string.ascii_letters + string.digits
    return ''.join(random.sample(rand_str, 4))


def gen_res_item(times):
    res = ''
    for i in range(0, times):
        res += gen_rand_item()
        if i + 1 != times:
            res += '-'
    return res


def gen_res_counts(times):
    res_arr = []
    for i in range(0, times):
        res_arr.append(gen_res_item(4))
    return res_arr
