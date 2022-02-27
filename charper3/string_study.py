# 字符串

# 合法的字符串
# 'hello', 'he"llo'
# "python", "pyth'on"

#非法字符串
# 'Hell'o', "He"llo"

# a = 'let\'s go' # 对单引号进行转义得到单引号

# print(a)

# 多行字符串
# string = '''这是多行字符串的第一行
# 这是多行字符串的第二行
# 这是多行字符串的第三行'''
# print(string)

# format函数
# print("{}是人类进步的阶梯。" .format("书籍"))

# print("{}是一个大帅逼！" .format("xw"))

# print("{}:{}" .format("192.168.1.100", "8080"))   # 注意format中字符串分隔用逗号
# print("{1}:{0}" .format("192.168.1.100", "8080"))
#format函数格式控制符：
# 1.<填充>字段是一个字符，默认使用空格填充
# 2.<对齐>字段分别使用<>^三个字符表示左对齐，右对齐和居中对齐
# 3.<宽度>如果设定宽度比实际宽度要小，那么宽度就为实际宽度

# words = "design"
# print("{:*<10}" .format(words))  # 左对齐，填充*至10个字符
# print("{:@>10}" .format(words))  # 右对齐，填充@至10个字符
# print("{:$^10}" .format(words))  # 居中对齐，填充￥至10个字符

# <,> 用于显示千分位分隔符，就是银行显示钱的那个
# print("{:,}" .format(1238978354))

# <精度>字段以小数点开头。对于浮点数而言，精度表示小数点的有效位，对于字符串而言，精度表示字符串长度
# print("{:.5f}" .format(3.1415926))  #3.14159
# print("{:.5}" .format("python"))    #pytho


# a,b = int(input()), int(input())

# print("{} * {} = {:2d}" .format(a, b, a*b))


# 字符串操作符 + - 连接字符串    * - 复制字符串    in 和 not in - 检查字符串中是否存在某个字串

# a = "Hello"
# a = a + " world!"
# print(a)  # Hello world!

# a = "hello"
# print(a * 2)

# a = "Hello world!"
# b = "hello"
# c = "Hello"
#
# print(b in a)
# print(c in a)
# print(b not in a)


# len() - 返回字符串长度
# a = "Hello world!"
# print("a 的长度是：%d" %len(a))

# str() - 将对应类型转换为字符串类型
# a = int(100)
# print(type(str(a)))  # str类型

# ord() - 返回字符对应的Unicode编码
# a = 'A'
# print(ord(a))  # 'A'的ascii码为65

# 字符串逆序
# s = str(input())
#
# i = len(s) - 1
# while (i >= 0):
#     print(s[i], end = '')
#     i = i - 1

# 将一个数字分别以二进制八进制十进制十六进制输出
# a = 198
# print(bin(a), oct(a), a, hex(a))