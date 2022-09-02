import sys

def solution(n, fishes):
    # 각 테케별로
    for fish in fishes:
        count = 0
        for i in range(n):
            # 자기 자리가 아님
            if abs(fish[i]) != i + 1:
                left = i
                right = abs(fish[i]) - 1
                while left <= right:
                    fish[left], fish[right] = -fish[right], -fish[left]
                    left += 1
                    right -= 1
                count += 1
            # 자리 자리긴 한데 음수임.
            if abs(fish[i]) == i + 1 and fish[i] < 0:
                fish[i] = -1 * fish[i]
                count += 1
            if count >= 3:
                print ('over')
                break;
        if count == 1:
            print ('one')
        elif count == 2:
            print ('two')


def main():
    fishes=[]
    n = int(sys.stdin.readline().strip())
    for i in range(5):
        fishes.append(list(map(int, sys.stdin.readline().split())))
    solution(n, fishes)


main()