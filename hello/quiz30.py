import string
import pandas as pd
from icecream import ic
import numpy as np
import random

from hello.domains import myRandom


class Quiz30:
    '''
        데이터프레임 문제 Q02
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4   10  11  12
    '''
    def quiz30_df_4_by_3(self) -> str:
        '''val = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        ind = range(1, 5) #range는 자체 타입이기 때문에 [],()과 동일한 타입과 함께 사용할 수 없다.
        col = ['A', 'B', 'C']
        df = pd.DataFrame(val, index=ind, columns=col)
        ic(df)
        return None'''

        a1 = [i for i in range(1, 4)]
        a2 = [i for i in range(4, 7)]
        a3 = [i for i in range(7, 10)]
        a4 = [i for i in range(10, 13)]
        #[1,4,7,10] 만들기
        b = [[i for i in range(j)] for j in range(1,11,3)]
        print(b)




    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic|df:      0   1   2
                0   97  57  52
                1   56  83  80
    '''

    def quiz31(self) -> str:

        return None
    '''
        데이터프레임 문제 Q04.
        국어, 영어, 수학, 사회 4과목을 시험 치른 10명의 학생들의 성적표 작성.
        단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID로 표기
        
         ic| df4:             국어  영어  수학  사회
                        lDZid  57   90   55   24
                        Rnvtg  12   66   43   11
                        ljfJt  80   33   89   10
                        ZJaje  31   28   37   34
                        OnhcI  15   28   89   19
                        claDN  69   41   66   74
                        LYawb  65   16   13   20
                        QDBCw  44   32    8   29
                        PZOTP  94   78   79   96
                        GOJKU  62   17   75   49
    '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def quiz32(self) -> str :
        col1 = ['국어', '영어', '수학', '사회']
        data1 = []
        idx = []

        df1 = pd.DataFrame([], [], [])
        print('--------------------------------')
        data2 = {}
        df2 = pd.DataFrame.from_dict({}, orient='index', columns=col1)
        return None
    def quiz33(self) -> str:
        #간소화하여 출력
        df = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(0, 100, 4),
                           length=3)
        ic(df)
        return None
    @staticmethod
    def createDf(keys, vals, length):
        return pd.DataFrame([dict(zip(keys,vals))for _ in range(length)])
        return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None