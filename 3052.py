num=[]
count=1

for i in range(10):
    n=int(input())
    n=n%42
    num.append(n)

num.sort()

for i in range(0,9):
    if num[i]!=num[i+1]:
        count+=1
        
print(count)
    
