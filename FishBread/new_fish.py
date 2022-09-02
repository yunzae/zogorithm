import sys
def minus(num):
    return -(num)

def myreverse(mylist,start,end):
    if start>end:
        t=end
        end=start
        start=t
    t = list(map(minus,list(reversed(mylist[start:end+1]))))
    newlist= mylist[:start]+t+mylist[end+1:]
    return newlist






n = sys.stdin.readline().strip()
for i in range(5):
    fish_list = list(map(int,sys.stdin.readline().split()))
