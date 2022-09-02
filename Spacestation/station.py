import sys
import math
A = tuple(map(int,sys.stdin.readline().split()))
B = tuple(map(int,sys.stdin.readline().split()))
C = tuple(map(int,sys.stdin.readline().split()))
D = tuple(map(int,sys.stdin.readline().split()))

def pointOnLine(point_A,point_B,t):
    x = t*point_A[0] +(1-t)*point_B[0]
    y = t*point_A[1] +(1-t)*point_B[1]
    z = t*point_A[2] +(1-t)*point_B[2]
    return (x,y,z)

def sqrLenOfTube(point_A,point_B):
    length_sqr =(math.pow(point_A[0]-point_B[0],2)+math.pow(point_A[1]-point_B[1],2)+math.pow(point_A[2] - point_B[2],2))
    return length_sqr

def findShort(t1,t2):
    for i in range(3):
       if A[i] == C[i]  or  A[i] == D[i] or B[i] ==C[i] or B[i] ==D[i]:
           return 0
    n=0.00005
    last_length = sqrLenOfTube(pointOnLine(A,B,t1),pointOnLine(C,D,t2))+1
    for i in range(int(1/n)):
        if last_length == sqrLenOfTube(pointOnLine(A,B,t1),pointOnLine(C,D,t2)):
            return math.ceil(math.sqrt(sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2))))
        if sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2)) < last_length:
            last_length = sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2))
        if t1<0+n or t1>1-n or t2<0+n or t2>1-n:
            return math.ceil(math.sqrt(sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2))))
        for i in range(2):
            if sqrLenOfTube(pointOnLine(A,B,t1-n),pointOnLine(C,D,t2)) < sqrLenOfTube(pointOnLine(A,B,t1),pointOnLine(C,D,t2)):
                t1= t1-n
        for i in range(2):
            if sqrLenOfTube(pointOnLine(A, B, t1), pointOnLine(C, D, t2-n)) < sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2)):
                t2 = t2-n
        for i in range(2):
            if sqrLenOfTube(pointOnLine(A, B, t1+n), pointOnLine(C, D, t2)) < sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2)):
                t1 = t1+n
        for i in range(2):
            if sqrLenOfTube(pointOnLine(A, B, t1), pointOnLine(C, D, t2+n)) < sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2)):
                t2 = t2+n
    return math.ceil(math.sqrt(sqrLenOfTube(pointOnLine(A, B, t1),pointOnLine(C, D, t2))))

print(findShort(0.5,0.5))