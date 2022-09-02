import sys

def calculation(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        print("error")
        return False

myinput = sys.stdin.readline().split()
number=[]
operator=[]

for i in range(0,len(myinput),2):
    number.append(int(myinput[i]))
for i in range(1,len(myinput),2):
    operator.append(myinput[i])

DP=[[0] * len(number) for _ in range(len(number))]
DP_min=[[0]*len(number) for _ in range(len(number))]

for i in range(len(number)):
    DP[i][i] = number[i]
    DP_min[i][i] = number[i]

for i in range(1,len(number)):
    for j in range(len(number)-i):
        l=i+1
        for k in range(1,i+1):
            l-=1
            op=operator[j+i-l]

            cal_list=[calculation(DP[j][j+i-l],DP[j+k][j+i],op),
                      calculation(DP[j][j+i-l],DP_min[j+k][j+i],op),
                      calculation(DP_min[j][j+i-l],DP[j+k][j+i],op),
                      calculation(DP_min[j][j+i-l],DP_min[j+k][j+i],op)]
            cal_list.sort()
            DP[j][j+i] = max(DP[j][j+i],cal_list[3])
            DP_min[j][j+i] = min(DP_min[j][j+i],cal_list[0])

print(DP[0][len(number)-1])
