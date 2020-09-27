# 55.请按alist中元素的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):
    return sorted(list1, key=lambda x:x['age'], reverse=True)


if __name__ == "__main__":
    print(sort_by_age(alist))