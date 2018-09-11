import os

if __name__ == '__main__':
    str = 'I am %s,i\'m %d years old'
    print(str % ('libeibei', 18))
    str1='I am {}'
    print(str1.format('libeibei'))
    a = 9/4
    b = 9//4
    print(a,b)

    c =100
    print(c==100 or false)
    ## 成员运算符
    a = [1,2,4,5,3,6,7]
    print (c in a)

    a = 100
    b = 100
    print (a is b)
