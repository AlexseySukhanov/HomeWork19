import abc


class Simple(abc.ABC):

    @abc.abstractmethod
    def check(self):
        pass

class Number(Simple):

    def __init__(self, value: int):
        self.value = value

    def check(self):
        self.check = True
        for i in range(2, self.value):
            if not self.value % i:
                self.check = False
        return self.check

class Anoter_number:

    def __init__(self, value: int):
        self.value = value

    def check(self):
        self.check = True
        for i in range(2, self.value):
            if not self.value % i:
                self.check = False
        return self.check

Number.register(Anoter_number)


s = Number(7)
x = Anoter_number(6)

print(s.check())
print((x.check()))