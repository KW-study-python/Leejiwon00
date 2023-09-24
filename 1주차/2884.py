H, M = map(int, input().split())
M -= 45
if M >= 0:
    print(H, M)
elif H==0:
    print(23, M + 60)
else:
    print(H - 1, M + 60)