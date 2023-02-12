n = int(input("Enter the number of rows:"))  
  
# iterarte upto n  
for i in range(n):  
   # adjust space  
   print(' '*(n-i), end='')  
  
   # compute power of 11  
   print(' '.join(map(str, str(11**i))))

sum=0
row=int(input("Enter the row number: "))
sum = sum + (1 << row)
print(sum)

# Sum of all elements
sum=0
for row in range(n):
   sum = sum + (1 << row)
print(sum)
