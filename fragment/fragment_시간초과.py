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
        for bucket in range(len(buckets)):
            while buckets[bucket]:
                Q.append(buckets[bucket].popleft())
                I.append(buckets_index[bucket].popleft())

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
        input_list.append(int(temp_int.ljust(100,'0')))
        index_list.append(k)

result=radix_sort(input_list, index_list)
print(result[1][N-2])
print(result[1][N-1])
print(result[1][N])

