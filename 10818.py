N=int(input())
A=list(map(int,input().split()))

max=-10000000
min=10000000

for i in range(len(A)):
    if(A[i]>max):
        max=A[i]
        
    if(A[i]<min):
        min=A[i]
      
print("%d %d" %(min,max))

