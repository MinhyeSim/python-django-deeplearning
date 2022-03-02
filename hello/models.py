import random
def main():
    while 1:
        menu = input('0.Exit 1.계산기 (+, -, *, /) 2.BMi 3.Grade 4.GradeAuto 5.Dice ')
        if menu == 0:
            break
        elif menu == '1':
             q1 = Quiz01Calculater(int(input('첫번째 수')),int(input('두번째 수')))
             print(f'{q1.num1} + {q1.num2} =  {q1.add()}')

        elif menu == '2':
            q2 = Quiz02Bmi(input('이름'), int(input('키'), input('몸무게')))
            print(f'이름: {q2.name}, 키 : {q2.height}, 몸무게 : {q2.weight}, BMI상태 : {q2.getBmi()}')

        elif menu == '3':
            for i in ['국어', '영어', '수학']:
                print(i)

            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math: int(input('수학 : '))
            grade = Quiz03Grade(name, kor, eng, math)
            print(f'{name}님의 국어{kor} 영어{eng} 수학 {math} 합계{grade.sum()} 평균{grade.avg()}')

        elif menu == '4':
            pass

        elif menu == '5':
            import random
            print(random.randint(1,6))

        elif menu == '6':
            q6 = Quiz06RandomGenerator(int(input('숫자1')),int(input('숫자2')))
            print(random.q6)


class Quiz01Calculater:

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        self.add()
        self.sub()

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        pass

class Quiz02Bmi(object) :

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    """def fat(self):
        return self.weight / (self.height * self.height)*10000 > 25
    def nomal(self):
        return self.weight / (self.height * self.height)*10000 >= 18.5
    def slim(self):
        return self.weight / (self.height * self.height)*10000 < 18"""


    def getBmi(self):
        res = self.weight/ (self.height * self.height) *10000
        if res > 25:
            return f'비만'
        elif res > 23:
            return f'과체중'
        elif res > 18.5:
            return f'정상'
        else:
            return f'저체중'

class Quiz03Grade(object) :
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return  self.kor + self.eng + self.math
    def avg(self):
        return self.kor + self.eng + self.math /3
    def getGrade(self):
        pass
    def chkPass(self) : #60점이상이면 합격
            pass

class Quiz04GradeAuto(object) :
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return  self.kor + self.eng + self.math
    def avg(self):
        return self.kor + self.eng + self.math /3
    def getGrade(self):
        pass
    def chkPass(self) : #60점이상이면 합격
            pass

class Quiz05Dice(object) :
    def __init__(self):
        self.random = random

class Quiz06RandomGenerator(object):
    def getRandomGenerator(self):
        return random.randint(int(input('숫자1'),int(input('숫자2'))))


class Quiz07RandomChoice(object) :
    def __init__(self): #803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이','김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종" ]

class Quiz08Rps(object):
    def __init__(self):
        pass

class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


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


if __name__ == '__main__':
   main()