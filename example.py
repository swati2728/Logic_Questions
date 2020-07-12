# hey = 1
# hey1 = "swatiraniparveen"
# hey2 = "d"
# print(hey,hey1,hey2)


# ccd = "i am good"
# de = "wait"
# print(ccd + " " + de)

# x = 50
# y = 10

# d = x +y
# e = x * y
# f = x - y
# g = x / y
# print(d,e,f,g)

# x = 2
# y = 10
# # 3 ^ 2 = 9
# ans = x ** 2
# print(ans)

# x = "Laptop"
# y = "education"
# print(x+y)
# print(x + " " + y)

# balloon = "sammy has a balloon"
# print(" ".join())
# print(" ".join(reversed(balloon)))
# print(balloon.split())

# string1 = "i love mangoes and apples"
# # string2 = "i love mangoes and apples"
# print(string1.replace("mangoes","apples"))
# print(string1.replace("apples","mangoes"))

# length = len(string1)
# if length > 20:
# 	print("hello")

# print(" ".join(reversed(string1)))
# print(string1.replace(" ",""))

# list2 = [2,3,4,45,6]
# a = min(list2)
# print(a)

# list2 = [2,3,4,45,6]
# a = min(list2)
# b = max(list2)
# print(a,b)

# list4 = [34,2,3,4,66,78,89,54,2,2]
# print(list4.index(2))

# if False:
# 	print("hi")
# if True:
# 	print("ok!")
# else:
# 	print("by")

# a = 10
# if a * 2 == 20:
# 	print ("a variable ko 2 se multiply kar ke 20 aata hai")
# else:
# 	print ("Nah! a variable ko 2 se multiply kar ke 20 nahi aata.")

# # (question 1)
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

# (question 2)

# i = 1
# for i in range(1,6):
# 	while i>=5:
    	
# 		print(i+1)





# (question3)

# for i in range(1,11):
# 	print("6 * "+str(i)+" = ",i*6)

# (question3 4)

# lst = [32,34,34,12,21,56 ,67]
# list(reversed(lst))





a = [10, 11, 12, 13, 14, 15] 
length = len(a)
for i in range(int(length/2)):
	n = a[i]
	a[i] = a[length-i-1]
	a[length-i-1] = n
print(a)	




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




















