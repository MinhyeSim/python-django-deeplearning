from context.domains import Dataset
import pandas as pd
import numpy as np
import sklearn


class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dname = './data/'
        this.sname = './save/'

    def new_model(self, fname) -> object:
        this = self.ds
        #index_col=0 해야 기존 index 값이 유진된다.
        #0은 컬럼명 중 첫번째를 의미한다(배열구조)
        #pd.read_csv('경로/파일명.csv',index_col = 인덱스로 지정할 c
        return pd.read_csv(f'{this.dname}{fname}', index_col=0)

    def save_model(self, fname, dframe):
        this = self.ds
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')