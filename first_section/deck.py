import collections
from random import choice


# namedtuple 构建一个简单的类来表示一张纸牌
card = collections.namedtuple("card",["rank","suit"])

class desc:
    rank = [str(n) for n in range(2, 11)] + list("JQKA")
    suit = "diamonds clubs hearts spades".split()

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suit
                      for rank in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

suit_value = {k: desc.suit.index(k) for k in desc.suit}
print(suit_value)
def sort_by(card):
    rank_value = desc.rank.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

a_desc = desc()

print(len(a_desc))
print(a_desc[0])
# 随机抽一张纸牌
print("随机抽一张纸牌")
print(choice(a_desc))
print("-----------------------------------")
# 实现了__getitem__后， 对象可以迭代
for i in a_desc:
    print(i)

# 排序
print("---------------------------------------------")
for i in sorted(a_desc, key=sort_by):
    print(i)
