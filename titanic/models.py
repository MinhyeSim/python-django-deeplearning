from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.label = this.train['Survived']
        this.id = this.test['PassengerId']
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this,  'SibSp', 'Parch', 'Ticket', 'Cabin')
        this = self.extract_title_from_name(this)
        self.remove_duplicate(this)
        self.sex_nominal(this)

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
        ic(f'10. id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        ic(type(feature))
        #문제의도 : 콘솔창에 출력시 해당 5개의 feature가 삭제되면 됨
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
        return this

    @staticmethod
    def create_train(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            ic()
        return this

    @staticmethod
    def extract_title_from_name(this) -> object:
        '''
        'Lady', 'Mr', 'Dona', 'Mlle', 'Capt', 'Master', 'Jonkheer', 'Mrs', 'Countess',
        'Dr', 'Ms', 'Miss', 'Rev', 'Col', 'Sir', 'Major', 'Don', 'Mme'
        '''
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for dataset in [this.train, this.test]:
            a += list(set(dataset['Title']))
        a = list(set(a))
        print(f'>>>{a}')
        '''
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme' ]
        Mr : ['Mile']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def sex_nominal(this) -> object:
        a = []
        for dataset in [this.train, this.test]:
            a += list(set(dataset['Sex']))
        a = list(set(a))
        print(f'>>>{a}')
        gander_mapping = {'male': 0, 'femail': 1}
        return gander_mapping


    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def sibsp_garbage(this) -> object:
        return this

    @staticmethod
    def parch_garbage(this) -> object:
        return this

    @staticmethod
    def ticket_garbage(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def cabin_garbage(this) -> object:
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this