import random

from


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        o[''] = myRandom(0,4)
        if (o[''] =='+') :
            c = self.add(a,b)
            print(c)
        elif(o[''] == '-'):
            c = self.sub(a,b)
            print(c)
        elif(o[''] == '*'):
            c = self.mul(a,b)
            print(c)
        elif(o[''] == '')



        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            return f'비만'
        elif res > 23:
            return f'과체중'
        elif res > 18.5:
            return f'정상'
        else:
            return f'저체중'

    def quiz02dice(self):
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        pass

    def quiz05grade(self):
        kor = myRandom(0,100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.agv(kor, eng, math)
        grade = self.getGrade()
        passChk = self.passChk()
        return [sum, avg, grade, passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        return members[myRandom(0, 23)]

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass
