from models import Quiz01Calculater, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz09GetPrime, Quiz10LeapYear, Quiz06RandomGenerator
from domains import Member
from hello.domains import Member
from hello.quiz00 import Quiz00
from hello.quiz10 import Quiz10
from hello.quiz20 import Quiz20
from hello.quiz30 import Quiz30
from hello.quiz40 import Quiz40
if __name__ == '__main__':
    q0 = Quiz00()
    q1 = Quiz10()
    q2 = Quiz20()
    q3 = Quiz30()
    q4 = Quiz40()
    while 1:
        menu = input('0.Exit 1.계산기 (+, -, *, /) 2.Bmi 3.Grade 4.Grade Auto\n'
                     '5.Dice 6.Random 7.Choice 8.Rps 9.Get Prime 10.Leap Year\n'
                     '11.Number Golf 12.Lotto 13.Bank 14.Gugudan 15. 16. 17.소수 18. 19. 20\n'
                     '21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32.')

        if menu == 0:
            break
        elif menu == '1':
             q1 = Quiz01Calculater(int(input('첫번째 수')), input('연산자'),int(input('두번째 수')))

             if q1.op == '+':
                 res = q1.add()
             elif q1.op == '-':
                 res = q1.sub()
             elif q1.op == '*':
                 res = q1.mul()
             elif q1.op == '/':
                 res = q1.div()

             print(f'{q1.num1} {q1.op} {q1.num2} =  {res}')

        elif menu == '2':
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = q2.getBmi(member)
            print(f'이름: {member.name}, 키 : {member.height}, 몸무게 : {member.weight}, BMI상태 : {res}')

        elif menu == '3':
            q3 = Quiz03Grade()

        elif menu == '4':
            q4 = Quiz04GradeAuto()
            for i in ['국어', '영어', '수학']:
                print(i)
            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math: int(input('수학 : '))
            grade = Quiz03Grade(name, kor, eng, math)
            print(f'{name}님의 국어{kor} 영어{eng} 수학 {math} 합계{grade.sum()} 평균{grade.avg()}')

        elif menu == '5':
            print(Quiz05Dice.cast())

        elif menu == '6':
            q6 = Quiz06RandomGenerator()
            print(q6.getRandom())

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu =='8':
            q8 = Quiz08Rps(0) #1 : 가위 2.바위 3. 보
            print(q8.game())

        elif menu == '9':
            q9 = Quiz09GetPrime()
            print(q9.game())

        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('윤년 평년 구하기 ')))
            print(f'{q10.year}은{q10.leapyear()}입니다.')

        elif menu == '11':
            q11 = Quiz09GetPrime()
            print(q11.game())

        elif menu == '12':
            q9 = Quiz09GetPrime()
            print(q8.game())

        elif menu == '13':
            q9 = Quiz09GetPrime()
            print(q8.game())

        elif menu == '14':
            q9 = Quiz09GetPrime()
            print(q8.game())

        elif menu == '17': q1.quiz17prime()

        elif menu == '18': q1.quiz18golf()


        elif menu == '30':
            print(Quiz30.quiz30list())

        elif menu == '31':
            print(Quiz30.quiz30list())
        elif menu == '32':
            print(Quiz30.quiz30list())


