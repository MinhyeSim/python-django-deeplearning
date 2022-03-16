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
        df = self.train
        df = self.create_label(df)
        df = self.create_train(df)
        df = self.drop_feature(df)
        df = self.pclass_ordinal(df)
        df = self.fare_ratio(df)
        df = self.age_ratio(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)#=>정제되어있는 완제품.
        return df

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def create_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:
        a = [i for i in []]
        df = self.parch_garbage(df)
        df = self.name_garbage(df)
        df = self.sibsp_garbage(df)
        df = self.ticket_garbage(df)
        df = self.cabin_garbage(df)
        return df

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_garbage(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def sibsp_garbage(df) -> object:
        return df

    @staticmethod
    def parch_garbage(df) -> object:
        return df

    @staticmethod
    def ticket_garbage(df) -> object:
        return df

    @staticmethod
    def fare_ratio(df) -> object:
        return df

    @staticmethod
    def cabin_garbage(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df) -> object:
        return df