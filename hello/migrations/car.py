class Coffee:
    def __init__(self):
        self.ice = False
        self.shot = 2
        self.size = 'tall'
        self.takeout = False


class CoffeeShop:
    def __init__(self):
        self.coffee = Coffee()

    def order(self, ice, shot, size, takeout):
        self.coffee.ice = ice
        self.coffee.shot = shot
        self.coffee.size = size
        self.coffee.takeout = takeout

    def give(self):
        print(f'주문하신 {self.coffee.ice, self.coffee.shot}커피 나왔음')
        #self가 인스턴스이다.


#파라미터의 값을 명시
if __name__ == '__main__':
    bana = CoffeeShop()
    bana.order(ice=True, shot=1, size='grande', takeout=True)
    bana.give()
