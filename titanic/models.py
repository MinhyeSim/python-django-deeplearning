from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다.
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        # Entity에서 Object로 전환
        this = self.drop_feature(this)
        '''
        this = self.create_label(this)
        this = self.create_train(this)
        this = self.drop_feature(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.age_ratio(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1.Train의 타입 : {type(this.train)}\n')
        ic(f'2.Train의 컬럼 : {this.train.columns}\n')#columns의 syntext: ()이 없으니까 property ()있으면 메소드
        ic(f'3.Train의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4.Train의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5.Test의 타입 : {type(this.test)}\n')
        ic(f'6.Test의 컬럼 : {this.test.columns}\n')
        ic(f'7.Test의 상위 1개 :{this.test.head(1)}\n')
        ic(f'8.Test의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9.id의 타입 : {type(this.id)}\n')
        ic(f'10.id의 상위 10개 : {this.id[:10]}\n')
        print('*' * 100)

    @staticmethod
    def drop_feature(this, *feature) -> object:
        #문제의도 : 콘솔창에 출력시 해당 5개의 feature가 삭제되면 됨
        #a = [i for i in []]
        columns = ['Name',  'SibSp', 'Parch', 'Ticket', 'Cabin']
        [this.train.drop(columns, inplace=True, axis=1) for i in [this.train]]
        [this.test.drop(columns, inplace=True, axis=1) for i in [this.test]]

        '''
        this.train = this.train.drop('Name', axis=1)
        this.train = this.train.drop('SibSp', axis=1)
        this.train = this.train.drop('Parch', axis=1)
        this.train = this.train.drop('Ticket', axis=1)
        this.train = this.train.drop('Cabin', axis=1)

        this.test = this.test.drop('Name', axis=1)
        this.test = this.test.drop('SibSp', axis=1)
        this.test = this.test.drop('Parch', axis=1)
        this.test = this.test.drop('Ticket', axis=1)
        this.test = this.test.drop('Cabin', axis=1)
        '''


        return this

    @staticmethod
    def create_train(this) -> object:
        return this

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