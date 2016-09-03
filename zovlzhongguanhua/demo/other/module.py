#!/usr/bin/python3
# Filename: using_sys.py

# import sys
# for i in sys.argv:
#     print(i)
# print(sys.path)
# print(sys.api_version)
# print(sys.version)
# print(sys.hexversion)
# print(sys.hash_info)
# Fibonacci numbers module

# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     print()
# def fib2(n): # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result


# if __name__ == '__main__':
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')

import sys
a = dir(sys)
print(a)