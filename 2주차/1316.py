N=int(input())
cnt=0
for _ in range(N):
    word=input()
    flag=0 # 떨어져서 나온 문자를 체크하기 위한 변수
    for i in range(len(word)-1):
        if word[i]!=word[i+1]: # 붙어 있는 문자가 다를 경우
            j=i+2 # 그 다음 단어의 인덱스 저장
            for k in range(j,len(word)): # 단어 끝까지 반복문을 돌며 해당 문자가 나오는 지 체크
                if word[i]==word[k]: # 나온다면 flag 변수에 1을 더해줌
                    flag+=1
    if flag==0: # 떨어져서 나온 문자가 하나도 없는 경우-->그룹 단어
        cnt+=1
print(cnt)
