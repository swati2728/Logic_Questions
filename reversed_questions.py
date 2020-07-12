# (questions 1)

# a = [10, 11, 12, 13, 14, 15] 
# length = len(a)
# for i in range(int(length/2)):
# 	n = a[i]
# 	a[i] = a[length-i-1]
# 	a[length-i-1] = n
# print(a)	

# (example1)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# # Get list length
# L = len(numbers)
 
# # i goes from 0 to the middle
# for i in range(int(L/2)):
#     # Swap each number with the number in 
#     # the mirror position for example first 
#     # and last
#     n = numbers[i]
#     numbers[i] = numbers[L-i-1]
#     numbers[L-i-1] = n
 
# # At this point the list should be reversed
# print(numbers)

# (questions)

# (table of 6)
# for i in range(1,11):
# 	print("6 * "+str(i)+" = ",i*6)


# (question 1)

# name = input("enter a name")
# age = int(input("enter a age"))
# gender = input("enter a gender male or female")
# if gender =="female"
# 	elif age < 18:
# 		print(name +" " + "she is female and not adult")
# if age >= 18:
# 	print(name +" " + "she is female and adult and can go to collage")
# if gender=="male"
# 	elif age < 18:
# 		print(name +" " + "he is male and not adult")	
# if age >= 18:
# 	print(name +" " + "he is male and adult and can go to collage")
# else:
# 	print("ghar pe bet ja")	


# (example 2)

# Example input list of numbers
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# # Function takes a list as input
# def Reverse(numbers):
#       # Base case when the list is only one item
#       if (len(numbers)==1):
#          return numbers
#       # Otherwise
#       return Reverse(numbers[1:]) + numbers[0:1]
 
# # Test function
# print(Reverse(numbers))



# list = []
# x = 1
#     #Import 20 random numbers
# for i in range (0,20):
#     list.append (x)
#     print (list)
# for i in range(len(list) - 1, -1, -1):
#     print(list[i])

# n = 0
# i = 0
# for i in range(1,6):
# 	n = n+1
# print(n*1,n*2,n*3,n*4)


# (how to do reversed)

# a =["p","o","p"]
# i=-1
# while i<=-len(a):
# 	print(a[i])
# 	i=i-1

# x = [32,34,34,12,21,56,67]
x=["s","w","a","t","i"]
i = -1
while i>=-len(x):
	print(x[i])
	i = i-1


# num = int(input("enter a number"))
# while num > 1500 and num < 2700:
# 	if num%7==0 and num%5==0:
# 		print(num)
# 	num=num+1	

# # 
# x=[1,2,3,4]
# index=-1
# while index>=-len(x):
# 	print(x[index])
# 	index=index-1

