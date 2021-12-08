N=int(input())
count = 0

for i in range(1,N+1):
    if i<100:
        count+=1
    
    else:
        n=list(map(int,str(i)))
        if n[2]-n[1] == n[1] - n[0]:
            count+=1
            
print(count)
        # 253 이면 2-5랑  5-3 이 같아야한다?
