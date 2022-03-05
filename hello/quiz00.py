import random

from hello.domains import myRandom, my100, Member, members


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        o2 = myRandom(0,4)
        s = o[o2]
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
        p = myRandom(1, 3)
        score = p-c
        # 1:가위 2:바위 3:보
        if score == 0:
            res = '무승부'
        elif score == -1 or score == 2:
            res = '승리'
        else:
            res = '패배'
        print(f'플레이어:{p} 컴퓨터:{c} 결과:{res}')

    def quiz04leap(self):
        y = myRandom(1000,3000)
        if (y & 4 == 0 and y % 100 != 0) or y % 400 == 0:
            res = '윤년'
        else:
            res = '평년'
        print(f'{y}년은 {res}입니다')

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = kor+eng+math
        avg = int((sum)/3)
        grade = ['A','B','C','D','E']
        if avg == 100:
            g_index = 0
        elif avg < 100 and avg >40:
            g_index = int((99-avg)/10)
        else:
            g_index = 5
        print(f'평균 점수가{avg}(으)로 {grade[g_index]}등급 입니다.')

        if avg >= 60:
            res = '합격'
        else:
            res = '불합격'
        print(f'국어 : {kor},영어 : {eng}, 수학 : {math} 합격여부 : {res}')

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        print(members[myRandom(0, 23)])

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass
