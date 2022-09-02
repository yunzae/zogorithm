import sys

def minus(number):
    return -(number)

def rev(mylist,start,end):
    if start>end:
        t=end
        end=start
        start=t
    temp = list(map(minus,list(reversed(mylist[start:end+1]))))
    new_list= mylist[:start]+temp+mylist[end+1:]
    return new_list

def Set(fl):
    count=0
    mtop=[]
    ptom=[]
    for i in range(len(fl)-1):
        if fl[i]>0 and fl[i+1] <0:
            ptom.append(i+1)
            count+=1
        if fl[i]<0 and fl[i+1] >0:
            mtop.append(i)
    if fl[0] < 0:
        count+=1
    if len(mtop)==0 and len(ptom)==0:
        count = 0
    return count,mtop,ptom

def c1(fl,mtop,ptom):

    if len(mtop)==0 :
        nfl = rev(fl, ptom[0], -(fl[ptom[0]]) - 1)
        new_check = Set(nfl)
    else :
        nfl = rev(fl,mtop[0],-(fl[mtop[0]])-1)
        new_check=Set(nfl)

    if new_check[0] == 0 :
        if nfl == sorted(list(map(abs,fl))):
             return "one"
        else:
            return "over"
    elif new_check[0] ==1:
        if len(new_check[1])==1 and len(new_check[2])==1:
            fl=rev(nfl,new_check[1][0],new_check[2][0])
        elif len(new_check[1])==1 and len(new_check[2])==0:
            fl= rev(nfl, 0, new_check[1][0])
        else :
            fl = rev(nfl, new_check[2][0], len(fl)-1)
            print(fl)
        if fl == sorted(list(map(abs, fl))):
            return  "two"
        else:
            return "over"
    else:
        return "over"
def c2(fl,mtop,ptom):
    if len(mtop)==2 and len(ptom)==1:
        nfl=rev(fl,0,mtop[0])
        fl = rev(nfl,ptom[0],mtop[1])
    if len(mtop)==1 and len(ptom)==1:
        nfl=rev(fl,0,mtop[0])
        fl = rev(nfl,ptom[0],len(fl)-1)
    if len(mtop)==2 and len(ptom)==2:
        nfl=rev(fl,ptom[0],mtop[0])
        fl = rev(nfl,ptom[1],mtop[1])
    if len(mtop)==1 and len(ptom)==2:
        nfl=rev(fl,ptom[0],mtop[0])
        fl = rev(nfl,ptom[1],len(fl))
    if fl == sorted(list(map(abs,fl))):
         return "two"
    else:
        return "over"

def c0(fl):
    if rev(fl,0,len(fl)-1) == sorted(list(map(abs,fl))):
        return "one"
    elif -fl[0]!=len(fl):
        new_list = rev(fl, 0, -fl[0] - 1)
        fl = rev(new_list, -fl[0], len(fl)-1)
        if fl == sorted(list(map(abs,fl))):
            return "two"
    return "over"


n = sys.stdin.readline().strip()
for i in range(5):
    fl = list(map(int,sys.stdin.readline().split()))
    set = Set(fl)
    if set[0] == 1:
        print(c1(fl,set[1],set[2]))
    elif set[0] == 2:
        print(c2(fl,set[1],set[2]))
    elif set[0] ==0:
        print(c0(fl))
    else:
        print("over")