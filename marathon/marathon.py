import sys
from copy import copy
N,M=map(int,sys.stdin.readline().split())
input_list=[]
for _ in range(M):
    input_list.append(sys.stdin.readline().split())
input_list.sort()
mystack=[]
visit= dict()
result=[]
for i in input_list:
    print(i)
    visit[i[0]]=True
    visit[i[1]]=True



for i in input_list:
    if i[0]=='a':
        mystack.append(i)
    else:
        break

length_sum=0
path=[]

while mystack:
    print(mystack)
    info=mystack.pop()
    start=info[0]
    end=info[1]
    length=int(info[2])
    if end in path:
        continue
    if length_sum+length>42:
        continue
    if end=='a':
        if length_sum+length== 42:
            result.append(path)
            print("성공")
            continue
        else:
            continue
    path.append(start)
    length_sum+=length
    for i in input_list:
        if i[0]==end :
            mystack.append(i)
        if i[1]==end :
            temp=[i[1],i[0],i[2]]
            mystack.append(temp)
