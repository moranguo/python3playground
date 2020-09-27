# 统计一段字符串中字符出现的次数


def count_str(str_data):
    """定义一个字符出现次数的函数"""
    dict_str = {}
    for i in str_data:
        dict_str[i] = dict_str.get(i, 0)+1
    return dict_str


dict_str = count_str("AAABBCCACabc")
str_count_data = ""
for k, v in dict_str.items():
    str_count_data += k + str(v)
print(str_count_data)
