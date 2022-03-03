import sys
n = int(sys.stdin.readline().strip())
result=""
def palin(word):
        for i in range(len(word)//2):
            if word[i]!=word[-(i+1)]:
                return False
        return True

def quasiPalin(word): # 일일이 하나씩 글짜 빼서 확인하다가 하나라도 되면 True
    for i in range(len(word)):
        newword=list(word)
        newword.pop(i)
        if palin(newword):
            return True
    return False

for i in range(n):
    inputword=sys.stdin.readline().rstrip("\n")
    if palin(inputword):
        result+="1"+"\n"
    elif quasiPalin(inputword):
        result+="2"+"\n"
    else:
        result+="3"+"\n"

print(result)

