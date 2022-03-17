import random


class School:
    def __init__(self, money, speed):
        self.money = 10000
        self.speed = 100

    def mp(self, a, b):
        a = self.money
        b = self.speed

    def preprocess(self) -> object:
        self.bus()
        self.subway()
        self.taxi()

    @staticmethod
    def bus(this) -> object:
       return this

    @staticmethod
    def subway(this) -> object:
        return this

    @staticmethod
    def taxi(this) -> object:
        return this

if __name__ == '__main__':
    None


