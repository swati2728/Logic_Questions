# var_1=45
# b=2.1
# c="swati"
# print(var_1,b,c)
# print(type(var_1))
# print(type(b))
# print(type(c))

# a = b = c = 1
# print(a,b,c)

# a,b,c = 1,2,"john"
# print(a,b,c)

# str = 'Hello World!'

# print (str)          
# print (str[0])       
# print (str[2:5])     
# print (str[2:])      
# print (str * 2 )     
# print (str + "TEST") 

# gurukul="swati"
# var_nav=2.5
# print(gurukul,var_nav)

# ============================================================================

# conversion

# [sting to interger]

# var_a="12"
# var_b=int(var_a)
# print(var_a)
# print(var_b)
# print(var_a+var_a)
# print(var_b+var_b)

# var_a="12houses"
# var_b=int(var_a)
# print(var_a)
# print(var_b)

# [sting to float]

# var_a="12"
# var_b=float(var_a)
# print(var_a)
# print(var_b)
# print(var_a+var_a)
# print(var_b+var_b)

# var_a="12.2"
# var_b=float(var_a)
# print(var_a)
# print(var_b)

# [float to interger]

# var_a=12.5
# var_b=int(var_a)
# print(var_a)
# print(var_b)

# a=45
# b=float(a)
# print(a)
# print(b)

# [float to string]
# a="swati"
# b=float(a)
# print(a)
# print(b)

# a="45"
# b=int(a)
# print(a)
# print(b)

# =============================

# question 1

# var_12="2"
# var_13=float(var_12)
# print(var_12)
# print(var_13)

# var1=(input("enter a string input"))
# var2=(input("enter a string input"))
# sum=var1+var2
# print(sum)


# var1=int(input("enter a interger input"))
# var2=int(input("enter a interger input"))
# sum=var1+var2
# print(sum)


# =============
 # Declare a variable and initialize it
# f = 101
# print (f)
# # Global vs. local variables in functions
# def someFunction():
# # global f
#     f = 'I am learning Python'
#     print (f)
# someFunction()
# print (f)

# ====================================

# a=int("50")
# b=int("50")
# print(a,b)
# ====================================
# num1=45
# num2=21
# if num1>num2:
# 	print("num1 is maximum")
# else:
# 	print("num2 is not maximum")	

# num1=int(input("enter a number1:"))
# num2=int(input("enter a number2:"))
# if num1>num2:
# 	print("num1 is maximum")
# else:
# 	print("num2 is maximum")

# ======================================

# num1=12
# num2=42
# num3=5
# if num1>num2:
# 	print("num1 is maximum")
# elif num2>num1:
# 	print("num2 is maximum")
# elif num2>num3:
# 	print("num2 is maximum")
# elif num3>num2:
# 	print("num3 is maximum")
# else:
# 	print("invalid")		


# num1=int(input("enter a number1:"))
# num2=int(input("enter a number2:"))
# num3=int(input("enter a number3:"))
# if num1>num2:
# 	print("num1 is maximum")
# elif num2>num1:
# 	print("num2 is maximum")
# elif num2>num3:
# 	print("num2 is maximum")
# elif num3>num2:
# 	print("num3 is maximum")
# else:
# 	print("invalid")		

# =============================================

# user=int(input("enter a number"))
# if user<0:
# 	print("it is nagative")
# elif user>0:
# 	print("it is positive")
# elif user==0:
# 	print("it is zero")
# else:
# 	print("nothing")		

# ==================================

# num=int(input("enter a number"))
# if num%2==0:
# 	print("it is even number")
# else:
# 	print("it is odd number")	

# ============================
# year=int(input("enter a year:"))
# if year%4==0:
# 	print("it is a leap year")
# else:
# 	print("it is not a leap year")\

# ==========================

# letter=input("enter a letter")
# if letter=="a"or letter=="A"or letter=="b"or letter=="B"or letter=="c"or letter=="C"or letter=="d"or letter=="D"or letter=="e"or letter=="E"or letter=="f"or letter=="F"or letter=="g"or letter=="G"or letter=="h"or letter=="H"or letter=="i"or letter=="I"or letter=="j"or letter=="J"or letter=="k"or letter=="K"or letter=="l"or letter=="L"or letter=="m"or letter=="M"or letter=="n"or letter=="N"or letter=="o"or letter=="O"or letter=="p"or letter=="P"or letter=="q"or letter=="Q"or letter=="r"or letter=="R"or letter=="s"or letter=="S"or letter=="t"or letter=="T"or letter=="u"or letter=="U"or letter=="v"or letter=="V"or letter=="w"or letter=="W"or letter=="x"or letter=="X"or letter=="y"or letter=="Y"or letter=="z"or letter=="Z":
# 	print("it is alphabet")
# else:
	# print("no an alphabet")	

# ==================================

 # user = input("enter any letter")
# if user == 'a'or user == 'e'or user == 'i'or user == 'o'or user == 'u':
# 		print("it is vowel")
# elif user == 'A'or user == 'E'or user == 'I'or user == 'O'or user == 'U':
#         print("it is vowel")
# else:
#     print("it is consonant")                 

# ===============================
# weeks=int(input("enter a week"))
# if weeks==1:
# 	print("monday")
# elif weeks==2:
# 	print("tuesday")
# elif weeks==3:
# 	print("wed")
# elif weeks==4:
# 	print("thursday")
# elif week==5:
# 	print("friday")
# elif weeks==6:
# 	print("satursday")
# elif weeks==7:
# 	print("sunday")
# else:
# 	print("nothing")							

# ===================================
# nested if_else


# year=int(input("enter a year"))
# if year%4==0:
# 	if year%100:
# 		if year%400:
# 			print("it is a leap year",year)
# 		else:
# 			print("it is not a leap year",year)
# 	else:
# 		print("it is a leap year",year)
# else:
# 	print("it is not a leap year",year)			
# ============================================================

# day=input("enter a day")
# meal=input("enter a meal")
# if day=="monday":
# 	if meal=="breakfast":
# 		print("poha")
# 	elif meal=="lunch":
# 		print("rajma chawal") 	
# 	else:				
# 		print("poori sabji")
# elif day=="tuesday":
# 	if meal=="breakfast":
# 		print("poori sabji")
# 	elif meal=="lunch":
# 		print("dosa")
# else:
# 	print("nothing")					

# ======================================]

# weeks=int(input("enter a week"))
# if weeks==1:
# 	print("monday")
# elif weeks==2:
# 	print("tuesday")
# elif weeks==3:
# 	print("wed")
# elif weeks==4:
# 	print("thursday")
# elif week==5:
# 	print("friday")
# elif weeks==6:
# 	print("satursday")
# elif weeks==7:
# 	print("sunday")
# else:
# 	print("nothing")						

# ==================================================	

# SP=int(input("enter a cost"))
# CP=int(input("enter a cost"))
# amount=SP-CP
# if SP>CP:
# 	print("it is profit",amount)
# else:
# 	print("it is losss",amount)	
# =============================================


# length1=int(input("enter a mesure"))
# length2=int(input("enter a mesure"))
# length3=int(input("enter a mesure"))
# if length1==length2==length3:
# 	print("triangle is equilateral.")
# elif(length1==length2 or length2==length3):
# 	print("triangle is Isosceles.")
# else:
# 	print("it is scalene triangle.")
		

# ========================================

# num=int(input("enter a num"))
# if num<10:
# 	print("10 se chota hai")
# elif num>10 and num<20:
# 	print("20 se chota hai")
# else:
# 	print("20 se bada hai")		

# ========================================


# phy=int(input("enter pyhics  marks:"))
# chem=int(input("enter chem marks"))
# bio=int(input("enter bio marks"))
# math=int(input("enter math marks"))
# comp=int(input("enter comp marks"))
# percentage=5/phy+chem+bio+math+comp*100
# if(percentage>=90):
# 	print("grade 'A':",percentage)
# elif (percentage>=80):
# 	print("grade:'B'",percentage)
# elif (percentage>=70):
# 	print("grade:'C'",percentage)
# elif (percentage>=60):
# 	print("grade:'D'",percentage)
# elif (percentage>=40):
# 	print("grade:'E'",percentage)
# else:
# 	print("grade:'F'",percentage)

# =====================================================================

# charge=int(input("enter a electric bill charge"))
# unit=0
# amount=0
# if unit<=50:
# 	print(amt = unit * 0.50+)


# num=int(input("enetr a num"))
# varx = 300 - 123
# if num==varx:
# 	print("barabar hai ")
# else:
# 	print("barabar nahi hai")	
# ==========================================
# num=int(input("enetr a num"))
# number = 44 * 30
# if num>number:
# 	print("bada hai")
# else:
# 	print("barabar hahi")	

# ==========================================================

# water=int(input("enter a num"))
# if water<1:
# 	print("pani bharo")
# elif water<1 and water>=10:
# 	print("aur nahi bharna")
# else:
# 	print("over flow")		
# =================================================

# electricity=int(input("enter a num"))
# unit=0
# amount=0
# if unit<=50:
# 	if amt = unit * 0.50:
# 		print()

# if unit>=50 and unit<=100:
# 	if amt = 25 + ((unit-50) * 0.75):
			
# ==============================

# LOOP BASIC

# counter = 0
# while counter < 5:
# 	print ("NavGurukul")
# 	counter = counter + 1


# counter = 0 
# while counter < 5:
# 	print ("NavGurukul")
# 	counter = counter + 1
# print ("Yeh sirf ek baar print hoga")
  

# a = 1
# sum = 0
# while a<=100:
# 	num = int(input("enter your num"))
# 	sum = sum + num
# 	print(sum)
# a = a + 1

# i=1
# while i<=100:
# 	if i % 2 == 0:
# 		print(-i)
# 	else:
# 		print(i)
# 	i = i + 1

#=============================================
# var = 10
# while var > 0:              
#    print ('Current variable value :', var)
#    var = var -1
#    if var == 5:
#       break
# print ("Good bye!")


#============================================
# for letter in 'Python':     
#    if letter == 'h':
#       break
#    print ('Current Letter :', letter)

# ===================================

# for letter in 'Python': 
#    if letter == 'h':
#       pass
#       print('This is pass block')
#    print ('Current Letter :', letter)

# print ("Good bye!")

# ======================================

# var1=["p","y","t","h","o","n"]
# # var1="python"
# index=0
# while index<len(var1):
# 	if var1[index]=="h":
# 		break
# 	print(var1[index])		
# 	index=index+1

# ===================================

# user=int(input("enter a number"))
# if user%5==0 and user%15==0:
# 	print("divided by both 5 and 15")
# else:
# 	print("false")	

# ===================================

# 5 saal ki umar ke baad school ja sakte ho.
# 18 saal ki umar ke baad vote de sakte ho.
# 21 saal ki umar ke baad car drive kar sakte ho.
# 24 saal ki umar ke baad shaadi kar sakte ho.
# 25 saal ke baad legally drink kar sakte ho.

# age=int(input("enter a number"))
# if age<=5:
# 	print("school ja sacta hai")
# elif age <= 18:
# 	print("vote kar sacta hai")
# elif age<=21:
# 	print("car drive kar sacta hai")	
# elif age<=24:
# 	print("shaadi kar sacta hai")
# else:
# 	print("legally drink kar sakte ho")			
# =====================================================

# i=1
# while i<100:
# 	if i%7==0:
# 		print(i)
# 	i=i+1	

# =====================

# index=1
# sum=0
# while index<=10:
# 	num=int(input("enter a number"))
# 	if sum%2!=0:
# 		print("it is prime number")
# 	else:
# 		print("not a prime")	
# 	num=int(input("enter a number"))
# 	sum=sum+num
# 	index=index+1
# print(sum)



# index=1
# sum=0
# while index<=10:
# 	num=int(input("enter a number"))
# 	if sum%2!=0:
# 		sum=sum+1
# 		index=indexx+1
# 	print(sum)	
# a = 2
# prime=True
# b = int(input("a num: "))
# while a < b:
# 	if b % a == 0:
# 		prime=False
# 		print(b,"not a prime number")
# 		break
	
# 	a = a + 1

# if prime:
# 	print ("it is prime hai")


# amount=int(input("enter a num"))
# if amount==1000:
# 	print(" two notes of five hundred")
# elif amount==100:
# 	print("two notes of fifty")
# else:
# 	print("opps nothing")		
# 	`	


# sum = 0
# i = 1
# while i<=100:
#    print(i)
#    sum = sum+i
#    i = i+1
# #    print(sum)
#
 # i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     break
#   print(i)

# i = 1
# while i < 6:
#   i=i+1
#   if i == 3:
#    	break
#   print(i)

# name=input("enter a name:")
# age=int(input("enter a age:"))
# hight=int(input("enter a hight:"))
# gender=input("enter a gender:(male/female):")
# if age >=18:
# 	if age>40:
# 		print(name,"not aligeble")
# 	elif gender=="male":
# 		if hight>160:
# 			print(name,"congrants!! you are selected for male police force")
# 	elif gender=="female":
# 		if hight>150:
# 			print(name,"congrants!! you are selected for female police force")	
# 	elif gender=="male" and hight<160:
# 		print(name,"not aligeble")
# else:	
# 	print(name,"not aligeble")					

# ==============================================


# name=input("enter a name:")
# age=int(input("enter a age:"))
# hight=int(input("enter a hight:"))
# gender=input("enter a gender:(male/female):")

# if age <18 or age >40:
# 	print(name,"not aligible as age should be grater and smaller than 40")
# elif gender=="male":
# 	if hight>160:
# 		print(name,"congrants!! you are selected for male police force")
# 	else:
# 		print(name,"not aligeble becoz hight is not matching to profile it should be grater than 160")
# elif gender=="female":
# 	if hight>150:
# 		print(name,"congrants!! you are selected for female police force")	
# 	else:
# 		print(name,"not aligeble becoz hight is not matching to profile it should be grater than 150")
# else:
# 	print("invalid input")
# ===========================================================


# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

# gross_salary=int(input("enter a gross_salary:"))

# if gross_salary<=10000:
# ======================================================================

# day=input("enter a day")
# meal=input("enter a meal")
# if day=="morning":
# 	if meal=="chicken":
# 		print("only chicken will make")
# 	elif day=="lunch":
# 		if meal=="mumose":
# 			print("only mumose will make")
# elif day=="monday" or day=="tuesday":
# 	print("only dal rice")
# else:
# 	print("only dal rice whole day")					

# =================================================================

# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(num, end=" ")  
#     print(" ")


# row=5
# for row in range(1,row+1):
# 	for colum in range(1,row+1):
# 		print(colum,end=" ")
# 	print(" ")	

# row=5
# for i in range(row):
# 	for colum in range(i):
# 		print(colum,end="")
# 	print(" ")

# ======================+++++++++++++++++++=======================
# (print the length of the list without len functions)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# count=0
# while index<len(numbers):
# 	count=count+1
# 	index=index+1
# print(count)	


# (print the number which is grather thaan 20 and less than 40)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# count=0
# while index<len(numbers):
# 	if numbers[index]>20 and numbers[index]<40:
# 		count=count+1
# 	index=index+1
# print(count)		

# (print maximum of the list)

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# maximum=0
# while index<len(numbers):
# 	if numbers[index]>maximum:
# 		maximum=numbers[index]
# 	index=index+1
# print(maximum)		

# (print minimum of the list)		

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]		
# index=0
# maximum=0
# while index<len(numbers):
# 	if numbers[index]>maximum:
# 		maximum=numbers[index]
# 	index=index+1
# print("maximum of the list",maximum)	
# i=0
# minimum=numbers[i]
# while i<len(numbers):
# 	if numbers[i]<minimum:
# 		minimum=numbers[i]
# 	i=i+1
# print("minimum of the list",minimum)	

# (print sum of te list and averageof that sum)

# list1=[12,2,45,2,36,12,45,85,3,6]
# index=0
# sum=0
# average=0
# while index<len(list1):
# 	sum=sum+list1[index]
# 	index=index+1
# average=sum/len(list1)   
# print("total sum of list is",sum)
# print("total avarge of list is", average)	

# 
# (print how many time number is printing)

# list1 = [ 23 ,45 ,56 ,23 ,36, 56 , 34 ,23 ,44, 44,44,67 ,76, 76, 22 ]
# index=0
# list2=[ ]
# while index<len(list1):
#     if(list1[index] not in list2): 
#         list2.append(list1[index])    
#     index=index+1  
# i=0
# while i<len(list2):
# 	num=list2[i]
# 	j=0
# 	count=0
# 	while j<len(list1): 
# 		if num==list1[j]:
# 			count=count+1
# 		j=j+1
# 	print(num," ",count)
# 	i=i+1
# print(num," ",count)


# (print multiples of the list and putt in other list)

# list1 = [ 1 ,2 , 3,  4,  5,  6,  7,  8,   9,  10,  11 ]
# index=0
# list2=[ ]
# while index<len(list1)-1:
# 	mul = list1[index]*list1[index+1]
# 	list2.append(mul)
# 	index=index+1
# print(list2)


# (multiples of seven start from 1)

# list1=[12,7,14,21,28,56,48,15,91,105,133]
# index=0
# list2=[ ]
# list3=[ ]
# while index<len(list1):
# 	if list1[index]%7==0:
# 		list2.append(list1[index])
# 	index=index+1
# # print(list2)
# j=0
# while j<len(list2):
# 	if list2[index]%10==0:
		
# 	list3.append(list2[index])
# 	j=j+1
# print(list3)		

# (find second maximum number of the list)

numbers = [50, 40, 23, 700, 6, 12, 5, 10, 7]
index=0
maximum=0
second_max=0
while index<len(numbers):
	if numbers[index]>maximum:
		maximum=numbers[index]
	index=index+1
	i=0
	while i<len(numbers):
		if maximum>numbers[i] and second_max<numbers[i]: 
			second_max=numbers[i]
		i=i+1
print(maximum)
print(second_max)	




# numbers = [6, 9, 3, 1]
# sorted(numbers)


# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=-1
# while i>=-len(places):
# 	print(places[i])
# 	i=i-1 

# places=["delhi","gujrat","rajasthan","punjab", "kerala"]
# for places in reversed(places):
# 	print(places)


# palindrom numbers

# name=['y','o','u','s','u','f']
# index=""
# length=len(name)-1
# x=[]
# while length >= 0:
# 	x.append(name[length])
# 	length=length-1
# print(x)
# if name==x:
# 	print("panlindrome number")
# else:
# 	print("not panlindrome number")
# ================================================

# num=list(input("enter a binary number:"))
# result=0
# for i in range(len(num)):
# 	x=num.pop()
# 	if x=="1":
# 		result=result+(2**i)
# print("the decimal value is",result)


# ==========================================================
