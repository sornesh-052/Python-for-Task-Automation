#Employee bonus program
Grade=input("Enter the Grade: ")
sal=eval(input("Enter the Salary: "))
Bonus=0
total_sal=0
while sal>0:
    if sal<=10000:
        Bonus=sal*(2/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break
    elif(Grade=='A' and sal>10000):
        Bonus=sal*(5/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break
    else:
        Bonus=sal*(10/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break
