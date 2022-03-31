i=0
while i<=6:
    i=i+1
    print(i)

i=0
while i<=6:
    print(i)
    i+=1

a=[[9,6,8],[12,78],[9,8],[10,9]]
i=0
m=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        m.append(a[i][j])
        j=j+1
    i=i+1
print(m)

list=[1,2,3,2,1,4,5,6,7,8,5,6,7,]
i=0
x=[]
while i<len(list):
    if list[i] not in x:
        x.append(list[i])
    i=i+1
print(x)


for i in range(10):
    print("hello word")
