# append

# L = ['a', ['bb', 'cc'], 'd']
# L[1].append('xx')
# print(L)


# insert

# L = ['a', ['bb', 'cc'], 'd']
# L[1].insert(1,'xx')
# print(L)

# extend
# L = ['a', ['bb', 'cc'], 'd']
# L[1].axtend([1,2,3])
# print(L)


# pop
# L = ['a', ['bb', 'cc', 'dd'], 'e']
# x = L[1].pop(1)
# print(L)


# del
# L = ['a', ['bb', 'cc', 'dd'], 'e']
# del L[1][1]
# print(L)

# remove
# L = ['a', ['bb', 'cc', 'dd'], 'e']
# L[1].remove('cc')
# print(L)

# len
# L = ['a', ['bb', 'cc'], 'd']

# print(len(L))
# Prints 3
# 
# print(len(L[1]))
# Prints 2


# using for loop

# L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
# for list in L:
#     for number in list:
#         print(number, end=' ')

# ===================================================================

# questions 1

# list1 = [1,76,65,23,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# index=0
# for index in range (len(list1)) :
# 	if list1[index] not in list2:
# 		print(list1[index])
# 		index = index+1	

# ================================================================

# questions 2

# sum=0
# marks =[[78, 76, 94, 86, 88],
#        [91, 71, 98, 65, 76],
#        [95, 45, 78, 52, 49]]
# i = 0			
# for i in range(len(marks)):
# 	j = 0
# 	for j in range(len(marks[i])):
# 		print(marks[i][j])
# 		sum = sum+(marks[i][j])
# 		j = j + 1
# 	print(" ")
# 	i = i + 1
# print(sum)

# ===================================================================
# question 3

# marks = [[78, 76, 94, 86, 88],
#     	[91, 71, 98, 65, 76],
#     	[95, 45, 78, 52, 49]]
# for x in range(len(marks)):
# 	sum=0
# 	for y in range(len(marks[x])):
# 		print(marks[x][y])
# 		sum=sum+(marks[x][y])
# 	y=y+1
# 	print(" ")
# 	print(sum)
# x=x+1
# =============================================================

# questions 5

# magic_square = [[8, 3, 4 ],
#        			[1, 5, 9],
#       			[6, 7, 2]]
# row=0
# while row<len(magic_square):
# 	print(magic_square)
# 	col=1
# 	while col<len(magic_square):
# 		sum=0
# 		# col=col+1
# 		if row==sum and col==sum:
# 			print("it is magic_square")
# 		else:
# 			print("it is not a magic_square")
# 		col=col+1
# 		sum=sum+1	
# 	row=row+1
# print(sum)	



# magic_square = [[8, 3, 4 ],
#        			[1, 5, 9],
#       			[6, 7, 2]]
# i=0
# while i < len(magic_square):
# 	j=0
# 	sum=0
# 	while j < len(magic_square[0]):
# 		j=j+1
# 		if i==j:
# 			print("it is a magic_square")
# 		else:
# 			print("it is not a magic_square")
# 	i=i+1
# print(sum)				

# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# row=0
# while row<len(magic_square):
# 	index=0
# 	sum=0
# 	while index<len(magic_square[row]):
# 		sum=sum+magic_square[row][index]
# 		index=index+1
# 		if sum==sum:
# 			print("it is a magic_square")
# 		else:
# 			print("it is not a magic_square")	
# 	break   	
# 	row=row+1
# print(sum)				

# ====================================================================

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# count=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		count=count+1
# 		print(elements[index]," " + "it is a even number" + " ") 
# 	else:
# 		print(elements[index]," " + "it is odd number" + " ")
# 	count=count+1
# 	index=index+1
# print(count)			



# ========================================================================================================

# (NESTED LIST PRACTICE QUESTION) 

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# index=0
# list3=[ ]
# while index<len(list1):
# 	if list1[index] not in list2:
# 		list3.append(list1[index])
# 	index=index+1
# print(list3)	



# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]

# index=0
# sum=0
# while index<len(marks):
# 	j=0
# 	while j<len(marks[index]):
# 		sum=sum+marks[index][j]
# 		# print(marks)
# 		j=j+1
# 	# print(" ")
# 	index=index+1
# print(marks)
# print(sum)	


# marks = [
#     [78, 76, 94, 86, 88],3
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# index=0
# avarge=0
# while index<len(marks):
# 	sum=0
# 	j=0
# 	while j<len(marks[index]):
# 		sum=sum+marks[index][j]
	# 	avarge=sum/len(marks[index])
	# 	j=j+1
	# print(sum,avarge)
	# index=index+1


number=30
num=[10, 11, 12, 13, 14, 17, 18, 19]
index=0
list2=[ ]
while index<len(num):
	sum=0
	j=index+1
	while j<len(num):
		if num[index]+num[j]==number:
			a=[num[index],num[j]]
			list2.append(a)
		j=j+1
	index=index+1
print(list2)		


  
""" to improve the logical part """	
# magic_square = [[8, 123, 4],
#     			[1, 5, 9],
#     			[6, 7, 2]]
# row=0
# while row<len(magic_square):
# 	i=0
# 	sum=0
# 	while i<len(magic_square[row]):
# 		sum=sum+magic_square[row][i]
# 		if sum==sum:
# 			print("it is magic_square")
# 		else:
# 			print("it is not a magic_square")
# 		i=i+1
# 	row=row+1
# print(sum)		

