from matplotlib import font_manager, rc


from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
import icecream as ic
import matplotlib.pyplot as plt
import seaborn as sns

font_path = 'C:/Windows/Fonts/H2GTRE.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

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
        #self.pclass(this)
        #self.sex(this)
        #self.embarked(this)

    @staticmethod
    def survived(this) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))  # nrows=2, ncols=1, figsize=18inch, 8inch
        this['Survived'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
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
