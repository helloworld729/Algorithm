import copy
b = [1, 2, 3, [4, 5]]
c = copy.deepcopy(b)  # 深拷贝
c[0] = 0
c[-1][-1] = 6
print("深拷贝 完全独立")
print(b)
print(c)
# 拷贝后，bc两个变量的id相同，改变元素内容后，
# 改哪个，哪个的id变化

# # ##################### 直接赋值，完全相同 ###############################
list_11 = [1, 2, 3, [4, 5]]
list_22 = list_11  # 别名,二维列表相同
list_22[-1][-1] += 1
print("直接赋值 完全相同")
print(list_11)
print(list_22)

# ############### 工厂函数=浅拷贝 ##########################
list_1 = [1, 2, 3, [4, 5]]
list_2 = list(list_1)  # 等价于：list_2 = copy.copy(list_1)
list_2[-1][-1] += 1
list_2[0] -= 1
print("浅拷贝 局部(简单元素)独立")
print(list_1)
print(list_2)

# # ############### 切片操作=浅拷贝 ##########################
a = [1, 2, 3, [4, 5]]
b = a[1:]
a[3][0] += 1
print(b)
b[2][0] -= 1
print(a)

# 1、关于地址：经勘察发现 简单元素的地址是连续的，
# 但是复杂子对象[4, 5]不在连续存储区
# 2、copy操作后,由于是可变对象(list可以原地改变)，
# 所以list_1、list_2两变量的地址不同，但是内部对应
# 元素的地址都是一样的
# 3、简单元素改变：浅拷贝前后的变量值会发生冲突，
# 故list1变量的所有id都保持改变，list2相应位置地址改变。
# 4、复杂元素改变：浅拷贝在复杂子对象的改变上，
# 两变量没有冲突，故直接原地操作，id均未改变。

# 小结，何谓深浅？关于深浅拷贝，有点反常识，浅拷贝并
# 不是在浅层相同，而是浅层具有独立性。深拷贝不是全部
# 拷贝，而是完全独立。所以深浅是指可以独立的程度，浅拷贝
# 就是浅层独立，深拷贝就是完全独立，如果元素都是简单元素
# 例如以为list那么深浅都是表现的相同。

# 浅拷贝方法：copy函数，切片操作，工厂函数

