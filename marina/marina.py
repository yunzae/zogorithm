import sys
ans=[]
map_x=[0]
map_y=[0]
N = int(sys.stdin.readline())
for i in range(N):
    input_temp=list(map(int,sys.stdin.readline().split()))
    map_x.append(int(input_temp[0]))
    map_y.append(int(input_temp[1]))

map_x[0]=map_x[N]
map_y[0]=map_y[N]
map_x.append(map_x[1])
map_y.append(map_y[1])

for i in range(N+1):
    signedArea =0
    signedArea += (map_x[i-1]*map_y[i]+map_x[i]*map_y[i+1]+map_x[i+1]*map_y[i-1])
    signedArea -= (map_y[i-1]*map_x[i]+map_y[i]*map_x[i+1]+map_y[i+1]*map_x[i-1])
    if signedArea<0:
        ans.append(i)

for i in range(len(ans)):
    print(ans[i])