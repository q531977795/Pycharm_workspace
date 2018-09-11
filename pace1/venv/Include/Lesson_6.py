# 问题1：
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
# 各是多少？

# if __name__ == '__main__':
#     count = 0
#     for a in range(1, 5):
#         for b in range(1, 5):
#             for c in range(1, 5):
#                 if (a != b and a != c and b != c):
#                     count += 1
#                     print(a * 100 + b * 10 + c)
#
#     print('一共有%d个数'%count)

# 问题2：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 高于100万元时，超过100万元的部分按1%提成;
# 从键盘输入当月利润I，求应发放奖金总数？

# def getAnswer(number=0):
#     arr = [100, 60, 40, 20, 10, 0]
#     rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
#     bonus = 0
#     for i in range(6):
#         if (number > arr[i]):
#             bonu = (number - arr[i]) * rat[i] * 10000
#             bonus += bonu
#             print("利润高于{0}万的部分获得的奖金 = {1}".format(arr[i], bonu))
#             number = arr[i];
#
#     print("获得总奖金%d元" % bonus)


# if __name__ == '__main__':
#     I = int(input('请输入当月利润(万)'))
#     getAnswer(I)

# 问题3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# if __name__ == '__main__':
#     for a in range(10000):
#         for b in range(10000):
#             if a + 100 == b ** 2:
#                 for c in range(10000):
#                     if a + 268 == c ** 2:
#                         print(a, b, c)

# import sys
#
#
# def getThings(**str):
#     print(type(str))
#     for index, msg in str.items():
#         print(index, '---', msg)
#
#
# def showSomething(name, age, gender, hobby="没有", *args, **kwargs):
#     'showSomething()函数说明：混合参数函数测试'
#     print("大家好！\r\n我的名字叫%s,今年%d岁，性别%s" % (name, age, gender))
#     print("我爱好{}".format(hobby))
#     for item in args:
#         print(item)
#     for k, v in kwargs.items():
#         print(k, " -- ", v)
#
#
# if __name__ == '__main__':
#     getThings(name="libeibei", age=None, gender="femal", career="Android")
#
#     showSomething('李贝贝', 26, '男', '足球', '篮球', '跑步', 职业='Andorid 工程师', 其他='涨薪')
#     print(showSomething.__doc__)
#     help(showSomething)
#
# 问题 4 ，汉诺塔请编写move(n, a, b, c)函数
# 它接收参数n：表示3个柱子A、B、C中第1个柱子A上的圆盘数量
# 然后打印出把所有盘子从A借助B移动到C的方法；
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '---->', c)
#         return None
#     move(n - 1, a, c, b)
#     move(1, a, b, c)
#     move(n - 1, b, a, c)
#
#
# if __name__ == '__main__':
#     move(3, 'a', 'b', 'c')


# 递归函数的层数限制验证
# import sys
#
# a = 1
#
#
# def fun():
#     global a
#     print('递归：第{0}次调用fun()函数'.format(a))
#     a += 1
#     fun()
#
#
# if __name__ == '__main__':
#     sys.setrecursionlimit(10000)
#     fun()

# 方法一：直接用递归求斐波那契数列第n个数值
# 该种求法，n越大效率越低，因为每次求值，都会重新把前面的数算一遍
# def feibona(n):
#     if n < 2:
#         return n
#     return feibona(n - 1) + feibona(n - 2)
#
#
# # 方法二：使用尾递归求斐波那契数列第n个数值
# # 该种求法，效率较高
# def feibona_tial(n, a, b):
#     if n == 0:
#         return a
#     return feibona_tial(n - 1, b, a + b)
#
#
# # 方法三：循环求斐波那契数列第n个数值
# # 该种求法，效率最高
# def feibona_while(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return a
#     if n == 1:
#         return b
#     for i in range(1, n):
#         c = a + b
#         a = b
#         b = c
#     return c
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         print(feibona_while(i))  # 循环
#
#     for i in range(999):
#         print(feibona_tial(i, 0, 1))  # 尾递归
#
#     for i in range(10):
#         print(feibona(i))  # 递归


#############  ############ 2018/09/07  ############ ###################

# 9x9 打印乘法表
def print9x9():
    for i in range(1, 10):

        for j in range(1, i + 1):
            print('{}x{}={}'.format(i, j, i * j), end='a')

        print()


# 阶乘
def factorial(num):
    if num <= 0:
        pass
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    print('{}的阶乘={}'.format(num, factorial))


def isAmusitelang(num):
    '''
    # 判断一个数字是不是阿姆斯特朗数
    # 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
    # 例如1^3 + 5^3 + 3^3 = 153。
    # 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
    # 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
    :param num:
    :return:
    '''
    a = num
    nums = list()
    while (True):
        b = a % 10
        nums.append(b)
        a = a // 10
        if a < 10:
            nums.append(a)
            break
    c = 0
    for i in range(len(nums)):
        d = 1
        for j in range(len(nums)):
            d *= nums[i]
        c += d

    if c == num:
        print('{}是阿姆斯特朗数,其各位数字的{}次方之和={}'.format(num, len(nums), c))
    else:
        print('{}不是阿姆斯特朗数,其各位数字的{}次方之和={}'.format(num, len(nums), c))


step = 0


def HannoTower(n, a, b, c):
    '''
    汉诺塔
    :param n:汉诺塔中的圆盘个数
    :param a:第一个塔
    :param b:第二个塔
    :param c:第三个塔
    :return:
    '''
    global step
    if n == 1:
        step += 1
        print('第{}步：'.format(step), end='')
        print('{} ----> {}'.format(a, c))
        return
    HannoTower(n - 1, a, c, b)
    HannoTower(1, a, b, c)
    HannoTower(n - 1, b, a, c)


def test():
    a = [1, 2, 3, 4]
    b = [10, 100, 1000, 10000]
    c = [m * n for m in a for n in b]
    d = list(range(10))


    print(c)
    print(len(c), max(c))
    print(d)


if __name__ == '__main__':
    test()
    pass

    #############  ############ 2018/09/08  ############ ###################
