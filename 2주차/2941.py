croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for i in croatia:
    word=word.replace(i,'*') #크로아티아 알파벳 하나당 *로 바꿔준다
print(len(word))
