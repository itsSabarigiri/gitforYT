a=[1,2,3]
k=2
count=0

for i in range(len(a)):
    current=0
    for j in range(i,len(a)):
        current+=a[j]
        if(current==k):
            count+=1
print("count",count)
