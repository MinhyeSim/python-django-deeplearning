from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', '']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다.
        #데이터셋은 수정을 할 수 없다 따라서 {} 또는 [] 상태로 받아야 한다.
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.label = this.train['Survived']
        this.id = this.test['PassengerId']
        # Entity에서 Object로 전환
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this,  'SibSp', 'Parch', 'Ticket', 'Cabin')
        #self.kwargs_sample(name='이순신') => kwargs 샘플... 타이타닉 흐름과 무관
        this = self.name_nominal(this)
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
        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id 의 타입  {type(this.id)}')

    #@staticmethod
    #def kwargs_sample(this, **kwargs) -> None:
     #   ic(type(kwargs))
      #  {print(''.join(f'key: {i},val : {j}')) for i, j in kwargs.items()}

    @staticmethod
    def drop_feature(this, *feature) -> object:
        #문제의도 : 콘솔창에 출력시 해당 5개의 feature가 삭제되면 됨
        #a = [i for i in []]


        # [this.train.drop(feature, inplace=True, axis=1) for i in [this.train]]
        # [this.test.drop(feature, inplace=True, axis=1) for i in [this.test]]
        #for i in feature:
        #    this.train = this.train.drop(i, axis=1)
        #    this.test = this.test.drop(i, axis=1)

        # for i in feature:
        #   [this.i.drop(feature, axis=1) for i in ['train', 'test']]
        #   this.train.drop(feature, axis=1)
        #   this.test.drop(feature, axis=1)
        #   [i for i in [] ]

        #이중 for loop
        #for i in [this.train, this.test]:
        #    for j in feature:
        #        i.drop(j, axis=1, inplace=True)
        #위의 이중 for loop를 한줄로 줄이기
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]


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
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            ic()
        return this

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