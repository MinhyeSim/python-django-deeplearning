import random
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from hello.domains import members
from quiz00 import Quiz00
from domains import myRandom

class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list[0], list[-1], list[-2], list[1:3])
        list2 = ['math', 'english']
        print(list[0])
        print(list2[0][1])
        list3 = [1, '2', [1, 2, 3]]
        print(list3)
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)
        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)
        a = range(10)
        print(a)
        sum(a)
        b = [2, 10, 0, -2]
        sorted(b)
        b.index(0)
        len(b)
        print(b.index(0), len(b))

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))
        a[0] = 4
        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_students": [40, 20]}
        type(a)
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        a.keys()
        list(a.keys())
        a.values()
        a.items()
        a.get('class')
        print("class" in a)

    def quiz23listcom(self) -> str:
        print('------legacy-----------')
        a = [] #list() -> []
        for i in range(5):
            a.append(i)
        print(a)
        print('-------comprehension-----')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')#html.parser vs lxml
        ls1 = self.find_music(soup, 'title')#중복된 키의 값으로 찾지 않기 위해 ls1을 타이틀로 둔다.
        ls2 = self.find_music(soup, 'artist')
        a = [i if i ==0 or i == 0 else i for i in range(1)]

        d = {i:j for i,j in zip(ls1,ls2)}
        l = [i + j for i, j in zip(ls1,ls2)]
        l2 =list(zip(ls1,ls2))
        d1 = dict(zip(ls1,ls2))
        print(d1)
        #self.dict1(ls1,ls2)

    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            print(type(f'타입 : {ls1[i]}'))
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1,ls2) -> None: #dict1번을 줄인 방법
        dict = {}
        for i,j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1,ls2):
            dict[j] = j
        print(dict)

    def print_music_list(self,soup):
        artists = soup.find_all('p',{'class':'artist'})
        #print(type(artists)) #<class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        #print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p',{'class':'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self,soup):
        for i,j in enumerate(['artist','title']):
            for i,j in enumerate(self.find_music(soup,j)):
                print(f'{i}위 : {j}')
            print('#'*100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = [i for i in soup.find_all('p', {'class': cls_nm})]
        return [i.get_text() for i in ls]

    def quiz25dictcom(self) -> str:
        #리스트로 5명, 0점~ 100점을 랜덤으로 뽑기
        q = Quiz00()
        c = set([q.quiz06memberChoice() for i in range(5)])
        while len(c) !=5:
            c.add(q.quiz06memberChoice())
        students = list(c)
        scores = [myRandom(0,100) for i in range(5)]
        print({i : j for i,j in zip(students, scores)})

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(),'lxml')
        s = [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]
        print('\n'.join(i.get_text().strip() for i in [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]))
        print('----한줄로 줄이기----')
        print(''.join(i.get_text() for i in [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]))
        return None

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict,orient='index')
        print(df)
        df.to_csv('./save/bugs.csv',sep=',',na_rep='NaN')
    '''
    다음 결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6
    '''
    def quiz29_pandas_df(self) -> object:
        d2 = {"1":[1,3,5],"2":[2,4,6]}
        df2 = pd.DataFrame.from_dict(d2,orient='index',columns=['a','b','c'])
        print(df2)
        
        return None