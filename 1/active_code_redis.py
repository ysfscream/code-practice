import active_code
import redis

"""
生成随机字符串 可以当激活码使用, 帮激活码保存到 redis 中
"""

rDB = redis.Redis(host='localhost', port=6379, decode_responses=True)


def redis_save():
    codes = active_code.gen_res_counts(200)
    for code in codes:
        print(code)
        rDB.lpush('codes', code)


if __name__ == '__main__':
    redis_save()
