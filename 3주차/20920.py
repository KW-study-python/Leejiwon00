import sys
N,M = map(int, input().split())
dic={}
for _ in range(N):
    s = sys.stdin.readline().strip()
    if len(s) >= M:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
dic = sorted(dic.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
for i in dic:
    print(i[0])
