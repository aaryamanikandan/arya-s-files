age1 = int(input("Enter the age of the first individual: "))
age2 = int(input("Enter the age of the second individual: "))
age3 = int(input("Enter the age of the third individual: "))
if age1 >= age2 and age1 >= age3:
    eldest = age1
elif age2 >= age1 and age2 >= age3:
    eldest = age2
else:
    eldest = age3
if age1 <= age2 and age1 <= age3:
    youngest = age1
elif age2 <= age1 and age2 <= age3:
    youngest = age2
else:
    youngest = age3
print("The eldest is:", eldest)
print("The youngest is:", youngest)

