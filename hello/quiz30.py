import string
import pandas as pd
from icecream import ic
import numpy as np
import random

from hello.domains import myRandom, members


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

    @staticmethod
    def createDf(keys, vals, length):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(length)])

    def quiz33(self) -> str:
        df = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(0, 100, 4),
                           length=3)

        #ic(df)
        #ic(df.iloc[0])#시리즈 구조로 떨어진다.
        '''
        ic| df.iloc[0]: a    43
                        b    99
                        c    53
                        d    11
                        Name: 0, dtype: int32
        '''
        #ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:    a   b   c   d
                          0  5  35  52  70
        '''
        #ic(df.iloc[[0, 1]])
        '''
        ic| df.iloc[[0, 1]]:     a   b   c   d
                              0  86  80  71  22
                              1  86  80  71  22
        '''
        #ic(df.iloc[:3])
        ''' 
        ic| df.iloc[:3]:     a   b   c   d
                          0  88  44  48  22
                          1  88  44  48  22
                          2  88  44  48  22
        '''
        #ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:     a   b   c   d
                                          0  34  52  85  48
                                          2  34  52  85  48

        '''
        ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                 0  80  28  37  20
                                                 2  80  28  37  20
        '''
        ic(df.iloc[0, 1])
        '''
        ic| df.iloc[0, 1]: 28
        '''
        ic(df.iloc[[0, 2], [1, 3]])
        '''
        ic| df.iloc[[0, 2], [1, 3]]:     b   d
                                     0  28  20
                                     2  28  20
        '''
        ic(df.iloc[1:3, 0:3])
        '''
        ic| df.iloc[1:3, 0:3]:     a   b   c
                               1  80  28  37
                               2  80  28  37
        '''
        ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  80  37
                                                    1  80  37
                                                    2  80  37
        '''
        ic(df.iloc[:, lambda df: [0,2]])
        '''
        ic| df.iloc[:, lambda df: [0,2]]:     a   c
                                          0  80  37
                                          1  80  37
                                          2  80  37
        '''
        return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None