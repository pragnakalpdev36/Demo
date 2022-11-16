list1=[]
no4=int(input("Enter number:"))
no1=1
no2=1
no3=1
for i in range(1,no4+1):
    list1.append(i)
while no1< no4:
    no1=no1*2
    no2=no2+1
for j in range(0,no2):
    if len(list1)==1:
        break
    if no3==0:
        list1.remove(list1[0])
    for k in range(0,int(len(list1)/2)):
        list1[int(k*2+1)]=0
    no3=list1[int(len(list1)-2)]
    for m in list1:
        if m==0:
            list1.remove(m)
print(list1)
