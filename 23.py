list1=[6,7,8,9,10]
list2=[1,2,3,4,5]
n={}
for i in range(len(list1)):
    for i in range(len(list2)):
        k=list1[i],list2[i]
        n.update({k})
        i=i+1
print(n)

list=[1,2,3],[4,5,6],[7,8,9]
i=0
sum=0
m=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        m.append(list[i][j])
        j=j+1
    i=i+1
print(m)


i=0
while i<5:
    i+=1
    if i==4:
        continue
    print(i)

    if i==6:
        break
    print(i)

list=[1,2,3],[4,5,6],[7,8,9]
i=0
sum=0
while i<len(list):
    k=0
    while k<len(list[i]):
        print(list[i][k],end="")
        k=k+1
    i=i+1
print(sum)

list1=[1,2,3],[4,5,6],[7,8,9]
i=0
sum=0
m=[]
while i<len(list1):
    print(list1[i])

    i=i+1
   

x=[[1,2,3],[4,5,6],[7,8,9]]
i=0
sum=0
n=[]
while i<len(x):
    k=0
    while k<len(x[i]):
        sum=sum+x[i][k]
        k=k+1
    i=i+1
n.append(sum)
print(n)


