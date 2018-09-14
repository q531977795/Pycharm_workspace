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


if __name__ == '__main__':
    b = B()
    b.name = 'libeibei'
    b._B__school = 'qinghua'
    b.say()
