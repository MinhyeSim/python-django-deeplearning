import random

from hello.domains import myRandom, my100, Member, members


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        o2 = o[myRandom(0,5)]
        #List Slicing으로 사용
        if (o2 =='+'):
            c = self.add(a,b)

        elif(o2 == '-'):
            c = self.sub(a,b)

        elif(o2 == '*'):
            c = self.mul(a,b)

        elif(o2 == '/'):
            c = self.div(a,b)

        elif(o2 == '%'):
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
        name = members[myRandom(0,24)]
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

        print(f'{name}님은 {res}입니다')

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
        print('----legacy------')
        y = myRandom(1000,3000)
        if (y & 4 == 0 and y % 100 != 0) or y % 400 == 0:
            res = '윤년'
        else:
            res = '평년'
        print(f'{y}년은 {res}입니다')

        print('----comprehension----')
        y = myRandom(1000,3000)
        #s = T if   else F
        s = '윤년' if y % 4 == 0 and y % 100 !=0 or y % 400 == 0 else '평년'
        '''Java Style => String s = : () ? : ;
         s = (y % 4 == 0 && y % 100 !=0) ? '윤년' : '평년' '''

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
        print(members[myRandom(0, 24)])

    def quiz07lotto(self):
        mylotto = random.sample(range(1,46),6)
        mylotto.sort()
        print(f'{mylotto}')

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        print(f'{Account().to_string()}')
        a = Account()
        a.main()

    def quiz09gugudan(self):  # 책받침구구단
        pass

'''
08번 문제 해결을 위한 클래스는 다음과 같다. 
[요구사항 (REP)]
은행 이름은 Bitbank
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다. 
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
예를 들면 123-12-123456이다. 
금액은 100만원 ~ 999만원 사이로 랜덤하게 입금된다.
'''
class Account(object):
    def __init__(self):
        self.BANK_NAME = '비트은행'
        self.name = members()[myRandom(0,23)]
        #self.account_number = f'{myRandom(0,1000):0>3}-{myRandom(0,1000):0>2}-{myRandom(0,1000):0>6}'
        self.account_number = self.creat_account_number()
        self.money = myRandom(100, 999)

    def to_string(self):

        return f'은행 : {self.BANK_NAME},' \
               f'입금자 : {self.name}  ' \
               f'계좌번호 : {self.account_number} ' \
               f'금액 : {self.money} 만원'

    def creat_account_number(self):
        '''
        #코딩을 할 때 먼저 계좌번호 ls를 몇가지를 만들어야 하는가 확인 => "3자리" -"2자리" - "6자리"이므로 총 3개의 ls 생성
        #다음 range가 각 몇가지로 줘야하는지 확인한다 => "3"가지 -"2"가지 -"6"가지 이므로 range()에 각 값을 기입
        #랜덤값을 준다 = myRadom (0,10)입력
        #"-"를 사용하기 위해 str를 붙인다.
        #모든 값이 출력
        ls = [str(myRandom(0,10)) for i in range(3)]
        ls = ls.append("-")
        ls += [str(myRandom(0,10)) for i in range(2)]
        ls = ls.append("-")
        ls += [str(myRandom(0,10)) for i in range(6)]
        ls = ls.append("-")
        return "".join(ls)'''
        #return "".join([i if str(myRandom(0,9)) else '-' for i in range(13)])
        return "".join(['-' if i==3 or i ==6 else str(myRandom(0,9)) for i in range(13)])
        #return "".join([str(myRandom(0,9)) if i != 3 and i != 6 else '-' for i in range(13)])
        #for 뒤에 있는 "i"는 index가 아니라 element이다


    def main(self):
        ls = []
        #ls []는 list이다.
        while 1 :
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5. 계좌해지')
            if menu == '0' :
                break
            if menu == '1' :
                acc = Account()
                #Account() 는 생성자. acc는 객체이다
                print(f'{acc.to_string()}... 개설되었습니다.')
                ls.append(acc)
                #mean => acc(Account())를 리스트로 쌓아간다
            elif menu == '2' : #계좌값을 출력하려고한다.
                a = "".join([i.to_string() for i in ls])
                #ls = account 여러개. i는 여러개의 accout중의 1개. i.to_string()은 그 account에서 to_string 값을 불러오라는 뜻이다.
                #i를 이름 바꿔도 되는 이유?
                print(a)
                #"i"는 ls(list)의 입력값을 출력한다.
                # for 뒤에 있는 i는 ls중의 하나이다.
                #[<표현식> for <변수명> in <시퀀스>] => 출력은 뒤에서 한다.
            elif menu == '3' :
                account_number = input('입금할 계좌번호')
                deposit = input('입금액')
               #for i,j in enumerate(ls):
                   #if j.account_number == account_nuber :

            elif menu == '4' :
                account_number = input('출금할 계좌번호')
                money = input('출금액')
                #추가코드 완성
            elif menu == '5' :
                account_nuber = input('탈퇴할 계좌번호')
            else:
                print('Wrong Number.. ')
                continue