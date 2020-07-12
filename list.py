# STRINGS ki LIST

# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print (names_list)
# print (type(names_list))

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# print (banks_list)
# print (type(banks_list))

# INTEGERS ki LIST

# marks_list = [70, 80, 75, 65, 68]
# print (marks_list)   
# print (type(marks_list))

# FLOATS ki LIST

# temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
# print (temperature_list)
# print(type(temperature_list))

# MIXED Lists

# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print (type(mixed_list))

# names_list = ["swati", "yousuf", "kaliya", "swayou", "usuf"]
# print (names_list[3])

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]

# print (names_list[0]) # se "annu" print hoga

# print (names_list[4]) # se "rupa" print hoga

# print (names_list[5])


# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# # print (len(names_list))
# # # Agar humne list mein ek nayi value

# print (names_list)
# names_list.append("dhruv")
# print ("length of the list is ", len(names_list))
# print (names_list)

# print (names_list)
# names_list.append("dhruv")
# print ("length of the list is ", len(names_list))
# print (names_list)

# names_list.append("usuf")
# print ("length of the list is ", len(names_list))
# print (names_list)


# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# names_list.pop()
# print ("length of the list is ", len(names_list))
# print (names_list)

# names_list = ["swati","yousuf","swayou"]
# print (names_list)
# names_list.append("usuf")
# print ("length of the list is ", len(names_list))
# print (names_list)


# print ("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print ("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print ("length of the list is ", len(names_list), names_list)

# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
# 	print (students_list[index])
# 	index =index+1


# student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
# 	total_marks = student_marks[index] + total_marks
# 	index = index + 1
# print ("Total Marks: " + str(total_marks))

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
# 	marks = student_marks[index]
# 	if marks < 50:
# 		less_than50 = less_than50 + 1
# 	else:k
# 		more_than50 = more_than50 + 1
# 	index = index + 1
# print ("Marks more than 50: " + str(more_than50))
# print ("Marks less than 50: " + str(less_than50))


# (QUESTION 1)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(len(numbers))

# number = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i = 1
# while i<len(number):
# 	i = i+1
# print(i)


# length = 0
# for a in (50, 40, 23, 70, 56, 12, 5, 10, 7):
# 	length = length+1
# print(length)
	

# (QUESTION 2)	

# numbers = [50,40,23,70,56,12,5,10,7]
# count = 0
# i = 0
# while i < len(numbers):
# 	if numbers[i] > 20 and numbers[i] < 40:
# 		count = count+1
# 	i = i+1
# print(count)		


# i = 0
# list=[10,2,17,5,2,4,5]
# length=len(list)
# while i < len(list):
# 	if list[i]%2==0:
# 		print(list[i])
# 	i = i+1	
# 	

# # (question 3)
# i = 0
# index = 0
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# while i < len(numbers):
# 	print (numbers[i]) 
# 	i=i+1
# print("Largest element is:", max(numbers)) 

# my_list = [0, 2, 5, 6, 5, 8, 5, 8, 8]
# my_max = [ ]
# for list in my_list:
#        if list > 7:
#         my_max = my_max + [list]
# Print(my_max)


# (print stars)pattern

# num = int(input("Enter the number of num "))
# for i in range(1, num+1):
#     for a in range(1, i + 1):
#         print(i, end ="")
#     print()



# num = int(input("Enter the number of num "))
# for i in range(1, num+1):
#     for a in range(1, i + 1):
#         print(a, end ="")
#     print()



# num = int(input("Enter the number of num "))
# for i in range(1, num+1):
#     for a in range(1, i + 1):
#         print("*", end ="")
#     print()




# ========================================================

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i = 1
# while i < len(numbers):
# 	i = i+1
# print(i)

# ========================================================

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# i=0
# while i <len(numbers):
# 	if numbers[i]>20 and numbers[i]<40:
# 		count = count+1
# 	i = i+1
# print(count)		


# =================================================

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max_number=max (numbers)
# print(max_number)


# list = [3,8,2,9]
# max_number = max(list)
# print(max_number)

# ====================================================
# second maximum 

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=max(numbers[0]),max(numbers[1])
# secondmax=min(numbers[0]),min(numbers[1])
# while i<len(numbers):
# 	print(max(numbers))
# 	if i < secondmax:
# 		i=i+1
# 	print("second maximum number is","=", "secondmax(numbers)")	


# =====================================

# num=[50, 40, 23, 70, 56, 12, 5, 10, 7]		
# count=0
# i=0
# while i<len(num):
# 	if num[i]>20 and num[i]<40:
# 		count=count+1
# 	i = i+1
# print(count)		
# 

# =====================================================		

# num=[50,40,23,56,12,5,10,7]
# i=0
# index=0
# while i<len(num):
# 	print(num[i])
# 	i=i+1
# print("maximum number is","=" ,max(num))	

# ====================================================

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# x=len(places)
# for i in range(int(x/2)):
# 	n=places[i]
# 	places[i]=places[x-i-1]
# 	places[x-i-1]=n
# print(places)



# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=-1
# while i>=-len(places):
# 	print(places[i])
# 	i=i-1 


# places=["delhi","gujrat","rajasthan","punjab", "kerala"]
# for places in reversed(places):
# 	print(places)




# mylist = [1, 2, 3, 4, 5]
# for item in reversed(mylist):
# 	print(item)

# =================================================================
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




# b_n=[1,0,1,1,0,1,1]
# length=len(b_n)
# i=length-1
# a=1
# sum=0
# while i>=0:
# 	e=b_n[i]
# 	b=e*a
# 	sum=sum+b
# 	i=i-1
# 	a=a*2
# print(sum)


# =================================================================================================================

# (PRACTICE QUESTIONS)

# 1.(List)

# list1 = ["apple", "banana", "cherry"]
# print(list1)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])                                              

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


# list1=[[[[[[[[2,3]]]]]]]]
# print(list1[0][0][0][0][0][0][0][1])


# loop example

# list1=["AD","BD","AC"]
# for i in (list1):
# 	print("yex")

# name=["swati","evanjaline","salomi"]	
# print(name)
# print(type(name))

# money=[3000,125000,2460,1470,12580]
# print(money)
# print(type(money))

# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print(mixed_list)
# print (type(mixed_list))

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]

# print (names_list[0])

# print (names_list[4]) 

# print (names_list[5])

# names_list=["swati","usuf","evanjaline","salomi"]
# print (names_list)
# names_list.append("dhruv")
# names_list.append("alok")
# print ("length of the list is ", len(names_list))
# print (names_list)


# user=[1,2,3,4,5,6,8,5,4,5,2,3,6,]
# print(user)
# user.pop()
# print(len(user))
# print(user)
# print ("length of the list is ", len(user), user)
# user.pop(2)
# print ("length of the list is ", len(user), user)
# user.pop(2)
# print ("length of the list is ", len(user), user)


# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
# 	print (students_list[index])
# 	index = index + 1

# student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
# 	total_marks = student_marks[index] + total_marks
# 	index = index + 1
# print ("Total Marks: " + str(total_marks))

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# length=len(student_marks)
# index=0
# grater_than50=0
# less_than50=0
# while index<length:
# 	marks = student_marks[index]
# 	if marks<50:
# 		less_than50 = less_than50 + 1
# 	else:
# 		grater_than50 = grater_than50 + 1
# 	index = index + 1
# print ("Marks grater_than 50: " + str(grater_than50))
# print ("Marks less_than 50: " + str(less_than50))


# list_length = [1,2,3,4,5,6,]
# print(len(list_length))student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
# 	marks = student_marks[index]
# 	if marks < 50:
# 		less_than50 = less_than50 + 1
# 	else:
# 		more_than50 = more_than50 + 1
# 	index = index + 1
# print "Marks more than 50: " + str(more_than50)
# print "Marks less than 50: " + str(less_than50)


# =====================================================================================================

# # QUESTION 1
# num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(num):
# 	i=i+1
# print(i)	

# QUESTION 2

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(numbers):
# 	if numbers[i]>20 and numbers[i]<40:
# 		count=count+1
# 	i=i+1	
# print(numbers,"total count of numbers","=",count)	

# QUESTIONS 3

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))
# index=0
# while index<len(numbers):
# 	print(numbers[index])
# 	index=index+1
# print(max(numbers))	

# num = [50,56,12,7,19]
# a = 0
# maxi = 0
# while (a<len(num)):
# 	if (num[a] > maxi):
		# maxi = num[a]
	# a =  a + 1
# print(maxi)


# num = [50,56,12,7,19]
# a = 0
# first_mini = num[0]
# second_mini 22 = num[0]

# =====================================================================

# (print ho many element are there)

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



# (multiples)

# list1 = [ 1 ,2 , 3,  4,  5,  6,  7,  8,   9,  10,  11 ]
# index=0
# list2=[ ]
# while index<len(list1)-1:
# 	mul = list1[index]*list1[index+1]
# 	list2.append(mul)
# 	index=index+1
# print(list2)


#=============================================
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
# 		
# 	list3.append(list2[index])
# 	j=j+1
# print(list3)		

# =======================================================

# (multiplt index of both list and print ther product and pair)

# list1=[1,2,3,4]
# list2=[1,10,12,4]
# index=0
# mul=[]
# while index<len(list1):
# 	product=list1[index]*list2[index]
# 	mul.append(product)
# 	index=index+1
# print(mul)


# list1=[1,34,2,3,2]
# list2=[1,34,10,2,4]
# index=0
# maxi=0
# while index<len(list1):
# 	product=list1[index]*list2[index]
# 	if maxi < product:
# 		maxi = product
# 	index=index+1
# print("both elements are",list1[1],list2[1])
# print("higest product is:",maxi)

# 
# ====================================================================
 # (multi list multiplt index of both list and print ther product and pair)


"""debgging the line 618 how to multiply the index value"""


list1=[[1,2,3],[3,8,4],[7,3,5]]
index=0
maximum=[ ]
while index<len(list1):
	j=0
	while j<len(list1[index][j]):
		product=list1[0][0]*list1[1][0]*list1[2][0]
		maximum.append(product)
		j=j+1
	index=index+1
print(maximum)




# list1 = [[5,6,8], [7,4,3], [8,10,12]] 
# mult_list = [10,20,30] 
# index=0
# new_list=[ ]
# while index<len(list1):
# 	j=0
# 	while j<len(list1[index]):
# 		product=list1[index]*mult_list[j]
# 		new_list.append(product)
# 		j=j+1
# 	index=index+1 
# print(new_list)


# num1=int(input("enter a first number"))
# num2=int(input("enter a second numbers"))
# symbol=input("enter a symbol")
# if symbol=="-":
# 	answer=num1-num2
# 	print("total count is:",answer)
# elif symbol=="+":
# 	answer=num1+num2
# 	print("total count is:",answer)
# elif symbol=="/":
# 	answer=num1/num2
# 	print("total count is:",answer)
# elif symbol=="*":
# 	answer=num1*num2
# 	print("total count is:",answer)
# index=1
# while index<=answer:
# 	print(index)
# 	index=index+1				
# =======================================================================

