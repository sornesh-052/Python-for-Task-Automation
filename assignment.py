num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))

x=min(num1,num2)
l=[]
for i in range(1,x+1):
    if num1%i==0 and num2%i==0:
        l.append(i)
print(l, "\nNo. of intergers: ",len(l))

if(num1*num2)%(num1+num2)==0:
    print("YEAH")
else:
    print("NAH")
