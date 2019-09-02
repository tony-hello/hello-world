#列表也叫数组。
#1.翻转列表[0,1,2,3,4,5,6,7,8,9]
origin_list = [0,1,2,3,4,5,6,7,8,9]
reverse_list = origin_list[::-1]
print('翻转的数组是==>',reverse_list)

#2.翻转后的列表拼接成字符串
s1 = ''.join([str(i) for i in reverse_list])
print('拼接后的字符串是==>',s1)

#3.用切片方式取第3到第8个字符。

sliced_str = s1[2:8]
print('第三个到第八个字符是==>',sliced_str)

#4.对获得的字符串翻转
reversed_str = sliced_str[::-1]
print('翻转后的字符串是==>',reversed_str)

#5.转换为int类型
int_value = int(reversed_str)
print('转换为整型后的字符串是==>',int_value)

#6.转换为二进制，八进制，16进制
print('转换为二进制==>',bin(int_value))
print('转换为八进制==>',oct(int_value))
print('转换为16进制==>',hex(int_value))