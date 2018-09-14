# 菜鸟教程
# Python 练习 100 例


def test_1():
    '''
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    :return:
    '''
    list_2 = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if k != i and k != j and i != j:
                    list_2.append(i * 100 + j * 10 + k)

    print(len(list_2), list_2)


def test_2():
    '''
    企业发放的奖金根据利润提成。
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%;
    高于100万元时，超过100万元的部分按1%提成;
    从键盘输入当月利润I，求应发放奖金总数？
    :return:
    '''
    I = int(input('请输入当月利润 = ？（元）'))
    J = 0
    index = 0
    list_1 = [1000000, 600000, 400000, 200000, 100000, 0]
    list_2 = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    for i in list_1:
        if I > i:
            J += (I - i) * list_2[index]
            I = i
        print(J, I, index)
        index += 1
    print(J)


def test_3():
    '''
    一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    :return:
    '''
    for i in range(1, 85):
        j = 168 / i
        if 168 % i == 0:
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x, n, m)


def test_4():
    '''
    输入某年某月某日，判断这一天是这一年的第几天？
    :return:
    '''
    year = int(input('请输入要查询的年？（例：2018）'))
    month = int(input('请输入要查询的月？（例：1）'))
    day = int(input('请输入要查询的日？（例：1）'))
    date = 0

    print('{}年{}月{}日是该年份的第{}天'.format(year, month, day, date))
    pass


def test_5():
    '''
    任意输入n个整数，把这n个数由小到大输出。
    :return:
    '''
    list_1 = []
    i = 0
    while (True):
        i += 1
        str = input("请输入第{}个数字 (按Y键结束输入)".format(i))
        if str == 'Y': break
        list_1.append(int(str))
    print(list_1)

    # 冒泡排序算法
    for i in range(len(list_1)):
        for j in range(len(list_1) - i - 1):
            print(i, j)
            if list_1[j] > list_1[j + 1]:
                a = list_1[j]
                list_1[j] = list_1[j + 1]
                list_1[j + 1] = a
    print(list_1)


def feibona(n, a, b):
    '''
    尾递归，算斐波那契数列
    :param n:第n个数
    :param a:第一个数值
    :param b:第二个数值
    :return:
    '''
    if n == 1:
        return a
    return feibona(n - 1, b, a + b)


def test_6():
    '''
    斐波那契数列。
    :return:
    '''
    str = input('输入字母(Y/y)打印前100位数列，输入数字n打印数列中的第n个数字')
    if str == 'Y' or str == 'y':
        for i in range(1, 101):
            print(feibona(i, 1, 1))
    else:
        n = int(str)
        print(feibona(n, 1, 1))


def test_7():
    '''
    将一个列表的数据复制到另一个列表中
    :return:
    '''
    list_1 = [100, 1, 3, 7]
    list_2 = list_1
    print(list_1, list_2, id(list_1), id(list_2))

    list_1[3] = 300
    print(list_1, list_2, id(list_1), id(list_2))

    list_3 = list_1[:]
    print(list_1, list_3, id(list_1), id(list_3))


def test_8():
    '''
    输出 9*9 乘法口诀表。
    :return:
    '''
    for i in range(1, 10):
        for j in range(1, 10):
            print('{}x{}={}'.format(i, j, i * j), end='\t')
            if i == j: break
        print(end='\n')


import time


def test_9():
    '''
    暂停一秒输出。
    :return:
    '''
    for i in range(1, 11):
        time.sleep(1)
        print('过了{}秒'.format(i))


def test_10():
    '''
    暂停一秒输出，并格式化当前时间。
    :return:
    '''
    for i in range(100):
        time.sleep(1)
        print('当前时间是=', time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))


def test_11():
    '''
    古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
    小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    1,1,2,3,5,8,13
    遵循斐波那契数列
    :return:
    '''
    a = 1
    b = 1
    for i in range(1, 1000):
        if i == 1:
            print(a)
            continue
        a, b = b, a + b
        print(a)
    pass


def test_12():
    '''
    判断101-200之间有多少个素数，并输出所有素数。
    素数(又称为质数)：
    只能被自身和1整除的大于1的自然数称为素数
    :return:
    '''
    list_1 = []
    isSu = False
    for i in range(101, 201):
        isSu = True
        for j in range(2, i):
            if i % j == 0:
                isSu = False
                break
        if isSu: list_1.append(i)

    print(list_1)


def getMinYinZi(num):
    list1 = [2, 3, 5, 7]
    for i in list1:
        if num % i == 0 and num / i == 1:
            print(num)
            exit(0)
    while (True):
        for i in list1:
            if num % i == 0:
                print('{}*'.format(i), end='')
                num = num // i
                getMinYinZi(num)
                break


def test_14():
    '''
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    :return:
    '''
    str = input('请输入一个正整数')
    num = int(str)
    print('{}='.format(num), end='')
    getMinYinZi(num)


def test_15():
    '''
    利用条件运算符的嵌套来完成此题：
    学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
    :return:
    '''
    str = input('请输入成绩（0-100）')
    points = int(str)
    print('A' if points >= 90 else ('B' if points >= 60 else 'C'))
    pass


import datetime as dt


def test_16():
    '''
    输出指定日期格式
    :return:
    '''
    print(dt.date.today().strftime('%Y%m%d'))

    myDay = dt.date(1992, 5, 9)
    print(myDay.strftime('%Y/%m/%d'))


def test_17():
    '''
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    :return:
    '''
    str = input('请输入任意字符串')
    letter = 0
    space = 0
    number = 0
    other = 0

    for i in range(len(str)):
        char = str[i]
        if char.isalpha():
            letter += 1
            continue
        if char.isspace():
            space += 1
            continue
        if char.isdigit():
            number += 1
            continue
        else:
            other += 1
    print('字母个数：{}，空格个数：{}，数字个数：{}，其他：{}'.format(letter, space, number, other))


# 递归
def getNa(n, a):
    if n == 1:
        return a

    return getNa(n - 1, a) + a * (10 ** (n - 1))


def test_18():
    '''
    求s=a+aa+aaa+aaaa+...+(n个a)的值，其中a和n都是正整数
    :return:
    '''
    print('求s=a+aa+aaa+aaaa+...+(n个a)的值')
    a = int(input('(0<a<10)请输入a='))
    n = int(input('n>0 请输入n='))
    print('s={}'.format(a), end='')
    sumNum = a
    for i in range(2, n + 1):
        sumNum += getNa(i, a)
        print('+{}'.format(getNa(i, a)), end='')
    if sumNum != a:
        print('={}'.format(sumNum))


def getYinZiList(num):
    return sum


def test_19():
    '''
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。
    例如6=1＋2＋3.
    编程找出1000以内的所有完数。
    :return:
    '''
    l3 = []
    for i in range(1, 1001):
        if i == getYinZiList(i):
            l3.append(i)
    print('1000以内的所有完数:', l3)


if __name__ == '__main__':
    test_19()
