n=int(input("Enter the number of elements: "))
L=[]
while True:
    if len(L)==n:
        break
    else:
        num=input("Enter the element: ")
        L.append(num)
print(L)
max_val=max(L)
index_val=L.index(max_val)
print("Index of peak value: ", index_val)

