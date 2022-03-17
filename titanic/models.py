from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()#필요한 정보를 넣고 꺼내기 위해
    def __init__(self, train_fname, test_fname):

        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        self.id = self.test['PassengerId']
        self.label = self.train['Survived']
        #ic(f'트레인 컬럼 {self.train.columns}')
        #ic(f'트레인 헤드 {self.train.head()}')
        #id 추출

    def preprocess(self):
        this = self.create_this(self.dataset)
        self.print_this(this)
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

    def create_this(self, dataset) -> object:
        this = dataset #this 는 모델이다.
        that = this.model
        this.train = self.train #this.train,test,id를 dataset으로 합쳤따.
        this.test = self.test#train, 는 series id는 df
        this.id = self.id
        return this

    @staticmethod
    def drop_feature(this, *feature) -> object:
        a = [i for i in []]
        '''
        self.parch_garbage(df)
        self.name_garbage(df)
        self.sibsp_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
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