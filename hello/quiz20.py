import random
import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup
from urllib.request import urlopen

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

    def quiz24zip(self) -> str:
        print('------legacy------')
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        #접속할 url

        html_doc = urlopen(url)
        # 해당 url 페이지에서 가져온 HTML코드

        soup = BeautifulSoup(html_doc, 'lxml')#html.parser vs lxml
        #HTML코드를 파싱 가능한 형태로 만듦
        #print(soup.prettify())

        a = [i for i in soup.find_all('p', {'class':'artist'})]
        #print(typer(artists)) #<class 'bs4.element.ResulteSet'>
        a = [i.get_text()for i in a]
        #print(type(artists))
        print(''.join(i for i in a))

        t = [i for i in soup.find_all('p', {'class': 'title'})]
        print(''.join(i.get_text() for i in t))

        s = [i for i in soup.find_all('p', {'class': 'song'})]
        print(''.join(i.get_text() for i in t))


        return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(),'lxml')
        s = [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]
        #3개를 뽑아내고 싶으면 전체에서 3개를 추출해야한다. 따라서 인덱스 값을 준다 ex) [0:3] (=> 인덱스 0번부터 시작해서 출력. 마지막은 마지막값의 -1 일임)
        print('\n'.join(i.get_text().strip() for i in [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]))
        #띄어쓰기를 삭제하기 위해 '\n'와 .strip()를 추가 기재 한다
        print('----한줄로 줄이기----')
        print(''.join(i.get_text() for i in [i for i in soup.find_all('div', {'class':'ellipsis rank03'})[1:3]]))
        #중복되는 s의 값을 그대로 가져온다.


        return None

    def quiz28(self) -> str:
        a = [i if i ==0 or i==0 else i for i in range()]
        b = [i if i ==0 or i==0 else i for i in []]
        c = [(i,j)for i,j in enumerate([])]

        return None


    def quiz29(self) -> str: return None