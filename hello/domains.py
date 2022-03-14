from dataclasses import dataclass
import random

@dataclass
class Member:

    name: str
    height: float
    weight: float

    @property
    def name(self) -> str: return self._name;

    @name.setter
    def name(self,name): self._name = name

    @property
    def height(self) -> float: return self._height;

    @height.setter
    def height(self,height): self._height = height

    @property
    def weight(self) -> float : return self._weight;

    @weight.setter
    def weight(self,weight): self._weight = weight

def myRandom(start, end): return random.randint(start, end)
def my100(): return myRandom(1,100)
def members() -> []:
    return ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
def my_abc() -> [] :
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



