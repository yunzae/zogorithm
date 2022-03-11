import sys

def finder(s,t,t_cursor):
    print(s)
    print(t_cursor)
    if t_cursor > len(t)-1:
        return "Yes"
    if t_cursor ==0:
        return start(s,t)
    else:
        if s.find(t[t_cursor]) == -1 or s.find(t[t_cursor])%2 == 0:
            t_cursor -= 1
            s = s[s.find(t[t_cursor])+1:]
            return finder(s,t,t_cursor)
        else:
            s = s[s.find(t[t_cursor]):]
            t_cursor += 1
            if t_cursor == len(t)-1 and (len(s)-len(t))%2 == 0 :
                return "Yes"
            return finder(s,t,t_cursor)




def start(s,t):
    result = ""
    t_cursor=0
    if s.find(t[t_cursor]) == -1 :
        return "No"
    s=s[s.find(t[t_cursor]):]
    result1 = start(s[1:],t)
    t_cursor += 1
    result2 = finder(s,t,t_cursor)
    if result1 =="Yes" or result2 =="Yes":
        return "Yes"


n = int(sys.stdin.readline().rstrip())
for i in range(n):
    s=sys.stdin.readline().rstrip()
    t=sys.stdin.readline().rstrip()
    print(start(s,t))
