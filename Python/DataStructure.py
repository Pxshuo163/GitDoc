# encoding: utf-8
# 数据结构

# list
print ("》**** 以下为list列表 ****《")
list_name = ["val1", "val2", "val3"]
# 获取
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print (weekday[0])

"""
多行注释
"""
all_in_list = [
    1,                                  # 整数
    1.0,                                # 浮点数
    "a word",                           # 字符串
   #  print(1),                         # 函数
    True,                               # 布尔值
    [1, 2],                             # 列表中嵌套列表
    (1, 2),                             # 元组
    {"key": "value"}                    # 字典
]
# 添加
all_in_list.insert(1, "insert")
print ("插入:", all_in_list[1])
# 删除
all_in_list.remove("insert")
all_in_list.remove(1)
print ("移除:", all_in_list[1])
# 修改
all_in_list[1] = "fix"
print ("修改：", all_in_list[1])
# 删除多个
del all_in_list[1:-1]
print ("数组长度", len(all_in_list), all_in_list[-1])
# 添加多个
all_in_list.extend(["hello", "world", "oh", "no"])
print ("添加后数组长度", len(all_in_list), all_in_list[-1])


# 字典
print ("》**** 以下为dict字典 ****《")
dict_name = {"key1": "val1", "key2": "val2", "key3": "val3"}
# 动态初始化key
dict_key = "key"
dict_key2 = "key"
dict_test = {dict_key: "hi", dict_key2: "world"}
dict_key2 = "key"
print (dict_test[dict_key2])
# 添加
dict_test["hello"] = "you"
print ("添加：", dict_test["hello"])
"""
# 添加多个
dict_key.update({"hi": "good"})
print ("添加多个：" + dict_test["hi"])
"""
# 删除
del dict_test["hello"]
print ("删除：", "hello" in dict_test.keys())

# 元组
print ("》**** 以下为tuple元组 ****《")
print ("元组不可以被修改")
tuple_name = ("val1", "val2", "val3")
print (tuple_name[0])

# 集合
print ("》**** 以下为set集合 ****《")
set_name = {"val1", "val2", "val3", "val4"}
print ("元组无序且不重复")
set_name.add("val2")
set_name.remove("val2")
print (set_name)

# 排序
num_list = [6, 2, 7, 4, 1, 3, 5]
print (sorted(num_list), num_list[0], sorted(num_list, reverse=True))

# 合并
num_list_r = sorted(num_list)
num_list_l = sorted(num_list, reverse=True)
for a, b in zip(num_list_l, num_list_r):
    print (b, "is", a)
print (zip(num_list_l, num_list_r))

# 推导式
print ("》**** 以下为推导式 ****《")
a = []
for i in range(1, 11):
    a.append(i)
print (a)
print ([i for i in range(1, 11)])
a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
d = {i: i+1 for i in range(4)}
g = {i: j for i, j in zip(range(1, 6), 'abcde')}
g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}

# x^y
print 3**4

# 遍历数组
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(letters):
    print(letter, 'is', num + 1)
print (str(enumerate(letters)))



