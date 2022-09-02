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





def check1(word1,word2):
    if word1=="" and word2=="":
        return ""
    word2 = set(word2) - set(word1)
    new_word = list(word1)+list(word2)
    return new_word


def check(word1,word2):
    word1=list(word1)
    word2=list(word2)
    strlist=[]
    sublist=[]
    pal_list=[]
    str=""
    str_index=[]
    count=0
    if word1=="" and word2=="":
        return ""
    word2 = set(word2) - set(word1)
    new_word = list(word1)+list(word2)


    for i in range(0, len(new_word) + 1):
        c = list(combinations((new_word), i))
        sublist.extend(list(c))
        sublist[i]=list(sublist[i])

    for i in range(1,len(sublist)):
        for j in sublist[i]:

            str=str+j[0]
            str_index.append(j)
            str_ = "".join(str_index)
            strlist.append(str_)
            count+=1
            if palin(str):
                pal_list.append(strlist)
            else:
                str=""
                str_index=[]

    pal_list = sorted(pal_list, key=len,reverse=True)
    for i in range(len(pal_list)):

        if len(pal_list[i][0])!=len(pal_list[0][0]):
            pal_list.pop(i)

    return pal_list[0]




for i in range(len(sentence)):
    table[i+1][i+1] = check(table[0][i+1],table[i+1][0])

n= len(sentence)-1

for j in range(1,n+1):
    for i in range(n):
        if len(table[i+1][i+j])>2 or len(table[i+1+1][i+j+1])>2:
            table[i+1][i+j+1]=check(table[i+1][i+j],table[i+1+1][i+j+1])
        else:
            table[i + 1][i + j + 1] = check1(table[i + 1][i + j], table[i + 1 + 1][i + j + 1])
    n=n-1


for i in range(len(sentence)+1):
    print(table[i])


