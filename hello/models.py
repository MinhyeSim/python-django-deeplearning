class Quiz01Calculater(object):
    # (object)를 추가 함으로써 코드를 간결화 시킨다

    def __init__(self, num1, op, num2):
        # __init__은 초기화때 사용되는 메소드이다.
        ##'__'가 의미하는 바는
        # init는 생성자이다. 생성자란 인스턴스를 만드는 것
        # (self, num1 ,num2 )
        self.num1 = num1
        self.op = op
        self.num2 = num2
        # print('Hello Python')->self._num1=num1
        # '._'은 자바로 치면 private

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

class Quiz02Bmi(object) :

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def fat(self):
        return self.weight / (self.height * self.height)*10000 > 25
    def nomal(self):
        return self.weight / (self.height * self.height)*10000 >= 18.5
    def slim(self):
        return self.weight / (self.height * self.height)*10000 < 18


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

class Quiz03Grade :
    def __init__(self,name,kor,eng,math):
        self.name = name

    def sum(self):
        return  self.kor + self.eng + math
    def avg(self):
        return self.kor + self.eng + math /3
    def getGrade(self):
        pass
    def chkPass(self) : #60점이상이면 합격
            pass

class Quiz04GradeAuto :
    def __init__(self,name,kor,eng,math):
        self.name = name

    def sum(self):
        return  self.kor + self.eng + math
    def avg(self):
        return self.kor + self.eng + math /3
    def getGrade(self):
        pass
    def chkPass(self) : #60점이상이면 합격
            pass

class Diss :
    def __init__(self):
        pass


if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 (+, -, *, /) 2.BMi 3.Grade')
        if menu == 0:
            break
        elif menu == '1':
            calc = Quiz01Calculater(int(input('첫번째 수')),)
            num1 = int(input('첫번째 수'))
            opcode = input('연산자')
            num2 = int(input('두번째 수'))
            # 객체생성
            print('*' * 30)  # 입력 숫자들과 결과값을 구분하기 위함

            if opcode == "+":
                res = calc.add()
            elif opcode == "-":
                res = calc.sub()
            elif opcode == "*":
                res = calc.mul()
            elif opcode == "/":
                res = calc.div()
            print(f'{calc.num1} {opcode} {calc.num2} =  {res} ')

        elif menu == '2': #BMI
            name = input('이름')
            height = int(input('키'))
            weight = int(input('몸무게'))

            bmi = Quiz02Bmi(name,height,weight)
            print('*' * 30)
            print(bmi.getBmi())

        elif menu == '3' : #Grade
            for i in ['국어','영어','수학']:
                print(i)

            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math : int(input('수학 : '))
            grade = Quiz03Grade(name,kor,eng,math)
            print(f'{name}님의 ')



