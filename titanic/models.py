import pandas as pd
from icecream import ic
from context.domains import Dataset
from context.models import Model
import numpy as np


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
                   'Fare', 'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.label = this.train['Survived']
        this.id = this.test['PassengerId']
        this.train = this.train.drop('Survived', axis=1) #Entity에서 Object로 전환
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')



        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id 의 타입  {type(this.id)}')
        ic(f'10. id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
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
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
        return this

    @staticmethod
    def remove_duplicate(this) -> {}:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        #print(f'>>>{a}')
        '''
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme' ]
        Mr : ['Mile']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}#Map을 사용하기위해 {}로 표현
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)#종류 6가지에 해당되지 않는 값이 아예 없는 이름들은 0으로 처리한다
            these['Title'] = these['Title'].map(title_mapping)# 키 값에 해당되는 element들을 value값으로 바꾼다.
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        for these in [this.train, this.test]:
            gander_mapping = {'male': 0, 'female': 1}
            these['Gender'] = these['Sex'].map(gander_mapping)#map 은 male -> 0 으로 바꾸는 기능을 갖고있는 메소드이다.
            #값을 바꾼 컬럼인 'Sex'를 바탕으로 새로운 'Gender'컬럼으로 할당한다.
        return this

    @staticmethod
    def embarked_nominal(this) -> object:#목적: 비어있는 null 값을 채우기 위함 (Null의 값이 있을 경우 데이터를 분석하지 못하기 때문에 값을 근사값 범위로 채운다)
        for these in [this.train, this.test]:
            embarked_mapping = {'S': 1, 'C': 2, 'Q': 3} #null값은 가우스의 분포에 따라 가장 많은 값인 's'로 분류하기로 한다.
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
            this.train = this.train.fillna({'Embarked': 'S'})
            #{'Embarked' : 's'} -> 'Embarked의 null값들을 's'로 분류한다는 의미
            #fillna -> null(na)값을 채운다(fill)라는 의미
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] #np.inf는 나이를 알 수 없는 상태이다.
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in [train, test]:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['Age'] = pd.cut(these['Age'], bins, labels=labels)
            these['AgeGroup'] = these['Age'].map(age_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        bins = [-1, 8, 15, 31, np.inf]
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this