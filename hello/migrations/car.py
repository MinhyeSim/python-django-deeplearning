class Tmp:
    def __init__(self):
        self.name = 'sonata'
        self.speed = 0
        self.oil = 110

    def ctrl_speed(self, speed,oil):
        self.speed += speed
        self.oil = car.oil()

    def spend_oil(self, oil): #스피드를 증가하면 오일이 10씩 빠지게 하라.
        self.oil -= oil
        #Q4.자동으로 오일이 떨어지게 하라
        #7번 메소드를

#car는 인스턴스
#Tmp()는 클래스
if __name__ == '__main__':
    car = Tmp()
    print(f'변경 전 스피드 : {car.speed}')
    print(f'오일 잔량 : {car.oil}')
    car.ctrl_speed(50)# 인자(argument)의 값만큼 스피드 증가
    print(f'변경 후 스피드1 : {car.speed}')
    print(f'오일 잔량 : {car.oil}')
    car.ctrl_speed(10)  # 인자(argument)의 값만큼 스피드 증가
    print(f'변경 후 스피드2 : {car.speed}')
    print(f'오일 잔량 : {car.oil}')
