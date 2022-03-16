# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
from titanic.views import TitanicView
if __name__ == '__main__':
    view = TitanicView()

    while 1:

        menu = input('1.전처리 2.템플릿')
        if menu == '1':
            print(' #### 1.전처리 #### ')
            models = TitanicModel('train.csv', 'test.csv')
            break
        elif menu == '2':
            print(' #### 2.템플릿 ####')
            templates = TitanicTemplates(train_fname='train.csv')
            break