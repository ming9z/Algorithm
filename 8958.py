'''
T=int(input())


for i in range(T):
    A=str(input())
    sum=0
    score=0
    
    for j in range(len(A)):
        if A[j]=="0":
            score+=1
        else:
            score=0
        sum=sum+score  
        
    print(sum)
'''

count = int(input())
for i in range(count):
    oxString = str(input())
    oCount = 0
    oCountSum = 0
    for j in range(len(oxString)):
        if oxString[j] == 'O':
            oCount += 1
        else:
            oCount = 0
        oCountSum += oCount
    print(oCountSum)
