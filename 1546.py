x=[]
N=int(input())
x=list(map(int,input().split()))

sum=0
M=max(x) # 최댓값

for i in range(len(x)):
    x[i]=x[i]/M*100
    sum+=x[i]

avg=sum/len(x)
print(avg)
    
