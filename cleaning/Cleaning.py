import sys
job_list=[]
def mycmp(a,b,idx,DAY,PAY):
    if (a>b):
        if (idx != len(job_list) - 1):
            DAY[job_list[idx][0]] = DAY[job_list[idx+1][0]]
        return a
    else:
        if (idx==len(job_list) - 1):
            DAY[job_list[idx][0]] = job_list[idx][3]
        else:
            if b==PAY[job_list[idx+1][0]]:
                min_day = min(DAY[job_list[idx+1][0]],DAY[job_list[idx][1]+1]+job_list[idx][3])
                DAY[job_list[idx][0]]=min_day
            else:
                DAY[job_list[idx][0]] = DAY[job_list[idx][1]+1]+job_list[idx][3]
        return b
def clean(PAY,DAY):
    for i in range(len(job_list)-1,-1,-1):
        if (i==len(job_list)-1):
            PAY[job_list[i][0]]=mycmp(PAY[job_list[i][0] + 1], PAY[job_list[i][1] + 1] + job_list[i][2], i, DAY, PAY)
        else:
            if job_list[i][0] == job_list[i+1][0]:
                temp = mycmp(PAY[job_list[i][0] + 1], PAY[job_list[i][1] + 1] + job_list[i][2], i, DAY, PAY)
                if temp > PAY[job_list[i][0]]:
                    PAY[job_list[i][0]]=temp
            else:
                PAY[job_list[i][0]] = mycmp(PAY[job_list[i][0] + 1], PAY[job_list[i][1] + 1] + job_list[i][2], i, DAY, PAY)
        if(i != 0):
            for j in range(job_list[i-1][0]+ 1,job_list[i][0]):
                PAY[j] = PAY[job_list[i][0]]
                DAY[j] = DAY[job_list[i][0]]


n= int(sys.stdin.readline())
final_day=0
for i in range(n):
    temp_input =list(map(int,sys.stdin.readline().split()))

    temp_input[2] = temp_input[2]-10
    if (final_day < temp_input[1]):
        final_day=temp_input[1]
    days= temp_input[1]-temp_input[0]+1
    temp_input.append(days)
    job_list.append(temp_input)
job_list.sort(key=lambda x :x[0])
PAY=[0]*(final_day+2)
DAY=[0]*(final_day+2)
clean(PAY,DAY)
PAY.sort()
DAY.sort()
result1= PAY[-1]+10
result2=DAY[-1]
print(result1,result2)
