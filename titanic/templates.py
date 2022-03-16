from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
import icecream as ic
import matplotlib.pyplot as plt
'''
데이터  시각화
엔티티(개체)를 차트로 표현하는 것

모든 feature를 다 그려야 하지만, 시간 관계상
survived, pclass, sex, embarked의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오


'''
class TitanicTemplates(object):
    dataset = Dataset()
    model = Model()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        self.dataset = Dataset()
        self.model = Model()

    def visualize(self):
        self.draw_survived()
        self.draw_pclass()
        self.draw_sex()
        self.draw_embarked()

    def draw_survived(self) -> None:
        this = self.entity
        ic(f'트레인의 타임: {type(this.train)}')
        ic(f'트레인의 컬럼: {this.train}')
        ic(f'트레인의 상위5행: {this.train}')
        ic(f'트레인의 하위5행: {this.train}')
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived']
        plt.show()

    def draw_pclass(self) -> None:
        this = self.entity
        plt.show()

    def draw_sex(self) -> None:
        this = self.entity
        plt.show()

    def draw_embarked(self) -> None:
        this = self.entity
        plt.show()