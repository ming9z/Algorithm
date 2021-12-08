C=int(input())

for i in range(0,C):
    score=list(map(int,input().split()))
    sum=0
    count=0
    num=score[0]
    
    for j in range(1,num+1):
        sum=sum+score[j]
    
    avg=sum//num
    
    for x in range(1,num+1):
        if score[x]>avg:
            count=count+1
        else:
            pass
    answer='{:.3f}%'.format((count/num)*100)
    print(answer)
    
