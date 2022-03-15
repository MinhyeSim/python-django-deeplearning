from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplates(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()
        self.titanic = TitanicModel('train.csv', 'test.csv')
         #타이타닉 모델 불러오기