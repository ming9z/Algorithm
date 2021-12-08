A=[]

max=0
count=0

for i in range(0,9):    
    A.append(int(input()))
    if A[i]>max:
        max=A[i]
        count=i+1

print(max)
print(count)
