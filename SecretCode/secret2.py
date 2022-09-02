import sys



sentence = list(sys.stdin.readline().rstrip())
table = [[""]*(len(sentence)+1) for _ in range(len(sentence)+1)]

for i in range(len(sentence)):
    table[0][i+1] = [str(i)+sentence[i]]
    table[i+1][0] = [str(i)+sentence[i]]





def check1(word1,word2):
    if word1=="" and word2=="":
        return ""
    word2 = set(word2) - set(word1)
    new_word = list(word1)+list(word2)
    return new_word


def check(word1,word2,table_n1,table_n2):
    word1=list(word1)
    word2=list(word2)

    if word1=="" and word2=="":
        return ""
    word2 = set(word2) - set(word1)
    new_word = list(word1)+list(word2)
    list(set(new_word))
    new_word.sort()
    if new_word[0][-1]==new_word[-1][-1]:
        new_word = find_same(new_word,table_n1,table_n2)
    else:
        new_word = find_differ(new_word,table_n1,table_n2)
    return new_word

def find_same(word,table_n1,table_n2):
    new_word= list(table[table_n1+1][table_n2-1][:])


    new_word.insert(0, word[0])
    new_word.append(word[-1])
    return new_word

def find_differ(word,table_n1,table_n2):
    str1=""
    str2=""
    new_word1= list(table[table_n1][table_n2-1][:])
    new_word2= list(table[table_n1 + 1][table_n2][:])

    if len(new_word1) > len(new_word2):
        return new_word1
    elif len(new_word1)==len(new_word2):
        for i in range(len(new_word1)):
            str1= str1+str(new_word1[i][-1])
            str2= str2+str(new_word2[i][-1])
        str_list=[str1,str2]

        str_list.sort()
        if str_list[0] == str1:
            return new_word1
        else:
            return new_word2

    else:
        return new_word2
for i in range(len(sentence)):
    table[i+1][i+1] = check1(table[0][i+1],table[i+1][0])

n= len(sentence)-1



for j in range(1,n+1):
    for i in range(n):
        if len(table[i+1][i+j])>1 or len(table[i+1+1][i+j+1])>1:
            table[i+1][i+j+1]=check(table[i+1][i+j],table[i+1+1][i+j+1],i+1,i+j+1)
        else:
            table[i + 1][i + j + 1] = check1(table[i + 1][i + j], table[i + 1 + 1][i + j + 1])
    n=n-1


result = table[1][len(sentence)]
answer = ""
for c in result:
    answer += c[-1]

print(answer)

