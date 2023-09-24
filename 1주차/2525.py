A, B = map(int, input().split())
C = int(input())
B += C
H = A + (B // 60)
if H >= 24:
    H -= 24
if B >= 60:
    B -= 60 * (B // 60)
print (H, B)