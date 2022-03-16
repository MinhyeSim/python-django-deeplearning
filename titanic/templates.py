from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
import icecream as ic
import matplotlib.pyplot as plt
'''
데이터  시각화
엔티티(개체)를 차트로 표현 하는 것

모든 feature를 다 그려야 하지만, 시간 관계상
survived, pclass, sex, embarked의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오


'''
class TitanicTemplates(object):
    def __init__(self, train_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)

    def visualize(self) -> None:
        this = self.train
        self.survived(this)
        self.survived(this)
        self.survived(this)
        self.survived(this)

    @staticmethod
    def survived(this) -> None:
        plt.show()

    @staticmethod
    def pclass(this) -> None:
        plt.show()

    @staticmethod
    def sex(this) -> None:
        plt.show()

    @staticmethod
    def embarked(this) -> None:
        plt.show()
        