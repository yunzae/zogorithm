
from collections import deque
import sys


def radix_sort(nums, indexs):
    buckets = [deque() for _ in range(10)]
    buckets_index = [deque() for _ in range(10)]
    max_val = max(nums)
    Q = deque(nums)
    I = deque(indexs)
    cur_ten = 1

    while max_val >= cur_ten and type(cur_ten) == int:
        while Q:
            num = Q.popleft()
            index=I.popleft()
            buckets[(num // cur_ten) % 10].append(num)
            buckets_index[(num // cur_ten) % 10].append(index)
        for bucket in buckets:
            while bucket:
                Q.append(bucket.popleft())
        for bucket_index in buckets_index:
            while bucket_index:
                I.append(bucket_index.popleft())

        cur_ten *= 10

    return list(Q), list(I)


def convert(frag):
    frag_list = []
    for i in frag:
        if i == 'a':
            frag_list.append('1')
        elif i == 'c':
            frag_list.append('2')
        elif i == 'g':
            frag_list.append('3')
        elif i == 'n':
            frag_list.append('4')
        elif i == 't':
            frag_list.append('5')
    frag_str = "".join(frag_list)
    return frag_str


index_list = []
input_list = []
N = int(sys.stdin.readline())
k = 0
while (True):
    temp = (sys.stdin.readline().rstrip())
    k += 1
    if temp == "":
        break
    else:
        temp_int = convert(temp)
        temp_int=temp_int.ljust(100,'0')
        input_list.append(int(temp_int))
        index_list.append(k)
max_num= max(input_list)
max_len=len(str(max_num))
for i in range(len(input_list)):
    input_list[i]=int(str(input_list[i]).ljust(max_len,'0'))

result=radix_sort(input_list, index_list)
print(result[1][N-2])
print(result[1][N-1])
print(result[1][N])
