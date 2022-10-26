from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):

    # polimorfismo
    def falar(self):
        print('class B falando')


a = B()
a.falar()
