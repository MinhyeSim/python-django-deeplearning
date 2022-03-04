import random

from hello.domains import myRandom, my100, Member, members


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        o2 = myRandom(0,4)
        s =o[o2]
        if (s =='+'):
            c = self.add(a,b)

        elif(s == '-'):
            c = self.sub(a,b)

        elif(s == '*'):
            c = self.mul(a,b)

        elif(s == '/'):
            c = self.div(a,b)

        elif(s == '%'):
            c = self.mod(a,b)
        print(c)
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
        name = members()
        h = myRandom(100,200)
        w = myRandom(10,100)
        bmires = w / (h * h) * 10000
        if bmires > 25:
            res = '비만'
        elif bmires > 23:
            res = '과체중'
        elif bmires > 18.5:
            res = '정상'
        else:
            res = f'저체중'

        print(f'님은 {res}입니다')

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
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = kor+eng+math
        avg = (kor+eng+math)/3
        grade = ['A','B','C','D','E','F']
        
        return [sum, avg, grade]

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
