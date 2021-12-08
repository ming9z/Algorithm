def d(n):
        n=n+sum(map(int,str(n)))
        return n
    
nonNum=set()

for i in range(1,10001):
    nonNum.add(d(i))

for j in range(1, 10001):
    if j not in nonNum:
        print(j)
 
