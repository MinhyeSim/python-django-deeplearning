from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
import icecream as ic
import matplotlib.pyplot as plt
'''
데이터  시각화
엔티티(개체)를 차트로 표현하는 것


'''

class TitanicTemplates(object):
    dataset = Dataset()
    model = Model()
    def __init__(self, fname):
        self.entity = self.model.new_model(fname)

    def draw_survived(self):
        this = self.entity
        ic(f'트레인의 타임: {type(this.train)}')
        ic(f'트레인의 컬럼: {this.train}')
        ic(f'트레인의 상위5행: {this.train}')
        ic(f'트레인의 하위5행: {this.train}')
        f, ax = plt.sublots(1, 2, figsize=(18, 8))
        this['Survived']
        plt.show()