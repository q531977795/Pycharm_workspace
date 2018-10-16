class A():
    name = 'a'
    age = 26

    def say(self, str):
        self.name = str
        print(self.name)
        print(A.name)
        pass


class B():
    name = ''
    age = 0
    __school = ''

    def __init__(self):
        self.name = 'bbb'
        self.age = 222
        self.__school = 'zhongyuan'

    def say(self):
        print(self.name)
        print(self.age)
        print(self.__school)

    def runtimeException(self):
        try:
            print(100 / 0)
        except ZeroDivisionError:
            print('Error:ZeroDivisionError')


import random


class C:
    def getRundomNumber(self):
        return random.randint(1, 30)

    def guessNumber(self):

        print


if __name__ == '__main__':
    b = B()
    b.name = 'libeibei'
    b._B__school = 'huashida'
    b.say()
    b.runtimeException()
    c = C()
    c.name()
