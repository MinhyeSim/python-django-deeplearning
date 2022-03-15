from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)

    def preprocess(self):
        self.create_label()

    def create_label(self)->object:
        pass

    def create_train(self)->object:
        pass

    def drop_feature(self)->object:
        pass

    def pclass_ordinal(self)->object:
        pass

    def name_nominal(self)->object: #garbage
        pass

    def sex_nominal(self)->object:
        pass

    def age_ordinal(self)->object:
        pass

    def sibsp_nominal(self)->object:
        pass

    def parch_nominal(self)->object:
        pass

    def ticket_nominal(self)->object: #garbage
        pass

    def fare_ratio(self)->object: #garbage
        pass

    def cabin_nominal(self)->object:
        pass

    def embarked_nominal(self)->object: #garbage
        pass