def shuffle(l1,l2):
    new_list=[]
    n=len(l1)
    m=len(l2)
    x=min(n,m)
        
    for i in range(x):
        new_list.append(l1[i])
        new_list.append(l2[i])
        
    if len(l1)!=len(l2):
        if(n>m):
            new_list.append(l1[x:])
        elif (m>n):
            new_list.append(l2[x:])
    return new_list
            
#Driver Program
list1=[1,3,5]
list2=[2,4,6,8,10]
y=shuffle(list1,list2)
print(*y)
