# year =int(input("enter a year"))
# if year%4==0:
# 	print("it is leap year")
# else:
# 	print("it is not a leap year")		
 

# year=int(input("enter a year"))
# for i in range (1999,3001):
# 	if i%4==0:
# 		print(i)
# 	i=i+1

# ===================================

# num = int(input("enter any number"))
# if num < 0:
# 	print("it is postive number")
# else:
# 	print("it is nagative number")	

# ====================================

# number = int(input("enter a number"))
# if number < 10:
# 	print("10 se chota hai")
# elif number>10 and number < 20:
# 	print("20 se chota hai ")
# elif number>20:
# 	print("20 se bada hai")
# else:
# 	print("nothing")

# ====================================
# print sum of two numbers

# sum=0
# a=int(input("enter any number"))
# b=int(input("enter any number"))
# c=a+b
# if (a+b):
# 	print(c)
# else:
# 	print(nothing)



# a=2
# b=3
# print(a+b)
	 
# ==============================
# print factorial number 
   
# i = 1
# num = int(input("enter a factorial num"))
# fact = 1
# while i <= num:
# 	fact = fact*i
# 	i = i+1
# 	print(fact)


# ================================

# # print simpal interest
# formula of simpal interest(I=P*R*T)


# P = int(input("Enter the principal amount : "))
# N = int(input("Enter the number of years : "))
# R = int(input("Enter the rate of interest : "))
# SI = (P * N * R)/100.
# print(SI)

# ==============================================
# print compond interest

# P = int(input("enter a principal:"))
# R = int(input("enter a rate:"))
# t = int(input("enter a time period:"))
# amount = (P*((1 + R/100)))**t
# ci = amount - P
# print(ci)

# =========================================
# print perfect number

# num = int(input("enter a number"))
# sum = 0
# for i in range(1,num):
# 	if num%i==0:
# 		print(i)
# 		sum=sum+i
# 		i = i + 1
# print(sum)
# if num==sum:
# 	print("perfect")
# else:
# 	print("no perfect")

# =======================================

# num = int(input("enter a armstrong number"))
# sum = 0
# for i in range(1,num):
# 	if num%i==0:
# 		print(num**3)
# 		sum=sum+i
# 		i=i+1
# print(sum)
# if num==sum:
# 	print("it is armstrong number")
# else: 
# 	print("it is not a armstrong number")			

# ===============================================
num = 1
while num <= 10:
    i = 1
    while i <= num:
        product = num*i
        print(num, " * ", i, " = ", product, "\n")
        i = i + 1
    print("\n")
    num = num + 1