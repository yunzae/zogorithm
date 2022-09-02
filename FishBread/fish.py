import sys

def mi(n):
    return -(n)

def rev(ml,s,e):
    if s>e:
        t=e
        e=s
        s=t
    t = list(map(mi,list(reversed(ml[s:e+1]))))
    nl= ml[:s]+t+ml[e+1:]
    return nl

def Set(fl):
    c=0
    mtop=[]
    ptom=[]
    for i in range(len(fl)-1):
        if fl[i]>0 and fl[i+1] <0:
            ptom.append(i+1)
            c+=1
        if fl[i]<0 and fl[i+1] >0:
            mtop.append(i)
    if fl[0] < 0:
        c+=1
    if len(mtop)==0 and len(ptom)==0:
        c = 0
    return c,mtop,ptom

def c1(fl,mtop,ptom):
    minus=[]
    mpoint=[]
    plus=[]
    ppoint=[]
    c=0
    p=0
    for i in range(len(fl)):
        if fl[i]<0:
            minus.append(fl[i])
            mpoint.append(i+1)
    for i in range(len(minus)-2):
        if abs(fl[i+1]-fl[i]) != 1:
            c=+1

    for i in range(len(fl)):
        if fl[i]>0 and fl[i] != i+1:
            plus.append(fl[i])
            ppoint.append(i+1)
    for i in range(len(fl)-2):
        if abs(fl[i+1]-fl[i]) != 1:
            p=+1
    print(mpoint)
    print(ppoint)
    if len(ptom)>0 and (len(mtop)>0) and rev(fl,ptom[0],mtop[0]) == sorted(list(map(abs, fl))):
        return "one"
    if c==1:
        return "two"
    if p==1 and rev(fl,plus[0],plus[-1]) == sorted(list(map(abs, fl))):
        return "two"
    for i in range(len(mpoint)):
        if rev(fl,ppoint[0],mpoint[i]) == sorted(list(map(abs, fl))):
            return "two"
        if  rev(fl,ppoint[-1],mpoint[i]) == sorted(list(map(abs, fl))):
            return "two"
    return "over1"
def c2(fl,mtop,ptom):
    plus=[]
    ppoint=[]
    p=0
    minus=[]
    mpoint=[]
    c=0

    for i in range(len(fl)):
        if fl[i]<0:
            minus.append(fl[i])
            mpoint.append(i+1)
    for i in range(len(minus)-2):
        if abs(fl[i+1]-fl[i]) != 1:
            c=+1
    for i in range(len(fl)):
        if fl[i] != i+1:
            plus.append(fl[i])
            ppoint.append(i+1)
    for i in range(len(fl)-2):
        if abs(fl[i+1]-fl[i]) != 1:
            p=+1
    if p==1:
        fl1= rev(fl,plus[0],plus[-1])
        fl1_set = Set(fl1)
    for i in range(len(mpoint)):
         fl2 = rev(fl,ppoint[0],mpoint[i])
         fl2_set = Set(fl2)
         fl3 = rev(fl,ppoint[-1],mpoint[i])
         fl3_set = Set(fl3)

    if rev(fl1,fl1_set[2][0],fl1_set[1][0]) == sorted(list(map(abs, fl))) or rev(fl2,fl2_set[2][0],fl2_set[1][0]) ==sorted(list(map(abs, fl))) or rev(fl3,fl3_set[2][0],fl1_set[1][0])==sorted(list(map(abs, fl))):
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
    else:
        print("over3")



