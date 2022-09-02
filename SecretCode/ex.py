import sys
from itertools import combinations
def palin(word):
    if word == word[::-1]:
        return True
    return False



sentence = list(sys.stdin.readline().rstrip())
table = [[""]*(len(sentence)+1) for _ in range(len(sentence)+1)]

for i in range(len(sentence)):
    table[0][i+1] = [sentence[i]+str(i)]
    table[i+1][0] = [sentence[i]+str(i)]


for i in range(len(sentence)+1):
    print(table[i])


def check1(word1,word2):
    word2=set(word2)-set(word1)
    new_word = (word1+list(word2))
    return new_word

def check(word1,word2):
    sublist=[]
    pal_list = []
    word2=set(word2)-set(word1)
    new_word = word1+list(word2)


    for i in range(0, len(new_word) + 1):
        c = combinations((new_word), i)
        sublist.extend(list(c))
    for i in range(len(pal_list)):
        if palin(sublist[i][0]):
            pal_list.append(list(sublist))
    print(list(sublist))
    pal_list = sorted(pal_list, key=len)
    for i in range(len(pal_list)):
        if len(pal_list[i][0])!=len(pal_list[0][0]):
            pal_list.pop(i)
        print(1)
        print(pal_list)
        return pal_list[0]

    return new_word

for i in range(len(sentence)):
    table[i+1][i+1] = check(table[0][i+1],table[i+1][0])


for i in range(len(sentence)+1):
    print(table[i])

