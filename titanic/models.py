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
        #코딩 순서 1. 결합도를 낮춰야 한다.
        df = self.parch_garbage(df)
        df = self.name_garbage(df)
        df = self.sibsp_garbage(df)
        df = self.ticket_garbage(df)
        df = self.cabin_garbage(df)
        df = self.create_label(df)
        df = self.create_train(df)
        df = self.drop_feature(df)
        df = self.pclass_ordinal(df)
        df = self.fare_ratio(df)
        df = self.age_ratio(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)#=>정제되어있는 완제품.

    @staticmethod
    def create_label(create_label) -> object:
        return create_label

    @staticmethod
    def create_train(create_train) -> object:
        return create_train

    @staticmethod
    def drop_feature(drop_feature) -> object:
        return drop_feature

    @staticmethod
    def pclass_ordinal(pclass_ordinal) -> object:
        return pclass_ordinal

    @staticmethod
    def name_garbage(name_garbage) -> object:
        return name_garbage

    @staticmethod
    def sex_nominal(sex_nominal) -> object:
        return sex_nominal

    @staticmethod
    def age_ratio(age_ratio) -> object:
        return age_ratio

    @staticmethod
    def sibsp_garbage(sibsp_garbage) -> object:
        return sibsp_garbage

    @staticmethod
    def parch_garbage(parch_garbage) -> object:
        return parch_garbage

    @staticmethod
    def ticket_garbage(ticket_garbage) -> object:
        return ticket_garbage

    @staticmethod
    def fare_ratio(fare_ratio) -> object:
        return fare_ratio

    @staticmethod
    def cabin_garbage(cabin_garbage) -> object:
        return cabin_garbage

    @staticmethod
    def embarked_nominal(embarked_nominal) -> object:
        return embarked_nominal