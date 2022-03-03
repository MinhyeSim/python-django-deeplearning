import random


class Quiz01Calculater:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2




    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


class Quiz02Bmi(object):
    @staticmethod
    def getBmi(member):
        this = member
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            return f'비만'
        elif res > 23:
            return f'과체중'
        elif res > 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3


class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def getGrade(self):
        pass

    def chkPass(self):  # 60점이상이면 합격
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator(object):
    def getRandomGenerator(self):
        return random.randint(int(input('숫자1'), int(input('숫자2'))))


class Quiz07RandomChoice(object):
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']

    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps(object):
    # 외부에서 값을 받아오는지 아닌지 먼저 생각 -> 외부 값이 필요함
    def __init__(self, player):
        # 외부에서 값을 받아야 하기 때문에 player기재
        self.player = myRandom(1, 3)
        self.computer = myRandom(1, 3)

    def game(self):
        c = self.computer
        p = self.player
        score = self.player - self.computer
        # 1 : 가위   2: 바위  3: 보
        if score == 0:
            res = f'플레이어: {p}, 컴퓨터: {c}, 결과: 무승부'
        elif score == -1 or score == 2:
            res = f'플레이어: {p}, 컴퓨터: {c}, 결과: 승리'
        else:
            res = f'플레이어: {p}, 컴퓨터: {c}, 결과: 패배'

        return res


class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def leapyear(self):
        y = self.year

        if (y & 4 == 0 and y % 100 != 0) or y % 400 == 0:
           res = '윤년'

        else:
           res = '평년'
        return res

class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object):  # 책받침구구단
    def __init__(self):
        pass
