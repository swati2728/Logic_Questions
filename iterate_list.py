# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# # print (len(students))
# # print (len(marks))

# length = len(students) 
# counter = 0
# while counter<len(students):
# 	print (students[counter] +" " + str(marks[counter]))
	# counter=counter+1	
# ================================================================
# kitne admi the (question 1)

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# even=0
# odd=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		even=even+1
# 		print(elements[index]," " + "it is a even number" + " ") 
# 	else:
# 		print(elements[index]," " + "it is odd number" + " ")
# 		odd=odd+1
# 	index=index+1
# print(even,"is total number of evan numbers")			
# print(odd,"is total number of odd numbers")			



# ======================================================================
# (question 2)


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# even=0
# odd=0
# sum=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		even=even+1
# 		print(elements[index]," " + "it is a even number" + " ") 
# 	else:
# 		print(elements[index]," " + "it is odd number" + " ")
# 		odd=odd+1
# 	sum=sum+elements[index]
# 	index=index+1
# print(even,"is total number of evan numbers")			
# print(odd,"is total number of odd numbers")			
# print(sum)


# =====================================================
# (question 3/4)

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# even=0
# odd=0
# sum=0
# average=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		even=even+1
# 		print(elements[index]," " + "it is a even number") 
# 	else:
# 		print(elements[index]," " + "it is odd number")
# 		odd=odd+1
# 	sum=sum+elements[index]
# 	average=sum/2                                                  
# 	index=index+1
# print(even,"is total number of evan numbers")			
# print(odd,"is total number of odd numbers")			
# print(sum)
# print(average)

# ===================================================================
#
 # Kitne Crorepati? question 1

# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000,
# 				 5600000, 690909090, 31010101, 532010, 510, 4100]
# count=0
# index=0
# while index < len(kitna_paisa_hai):
# 	if kitna_paisa_hai[index]>=10000000:
# 		print(kitna_paisa_hai[index]," " + "they are Crorepati")
# 	elif kitna_paisa_hai[index]>=100000:
# 		print(kitna_paisa_hai[index]," "+ "they are lakhpati")
# 	else:
# 		print(kitna_paisa_hai[index]," " + "they are dilwale")	
# 	index=index+1
			
# ===================================================================
# question 2


# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000,
# 				 5600000, 690909090, 31010101, 532010, 510, 4100]
# count=0
# index=0
# Crorepati=0
# lakhpati=0
# dilwale=0
# while index < len(kitna_paisa_hai):
# 	if kitna_paisa_hai[index]>=10000000:
# 		print(kitna_paisa_hai[index]," " + "they are Crorepati")
# 		Crorepati=Crorepati+1

# 	elif kitna_paisa_hai[index]>=100000:
# 		print(kitna_paisa_hai[index]," "+ "they are lakhpati")
# 		lakhpati=lakhpati+1
	
# 	else:
# 		print(kitna_paisa_hai[index]," " + "they are dilwale")	
# 		dilwale=dilwale+1
	
# 	index=index+1

# print(Crorepati,"total Crorepati hai")
# print(lakhpati,"total lakhpati hai")
# print(dilwale,"total dilwale hai")

# ============================================================================

# question 3

# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# index=0
# a=0
# n=0
# t=0
# x=0
# u=0
# g=0
# while index<len(char_list):
# 	if char_list[index]=="a":
# 		a=a+1
# 	elif char_list[index]=="n":
# 		n=n+1
# 	elif char_list[index]=="t":
# 		t=t+1
# 	elif char_list[index]=="x":
# 		x=x+1
# 	elif char_list[index]=="u":
# 		u=u+1
# 	else:
# 		g=g+1
# 	index=index+1
# print("a is =",a,"n is =",n,"t is =",t,"x is =",x,"u is =",u)		    


# # ==========================================================================
# question 4

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13,20,11]
# index=0
# empty_list=[]
# while index<len(n):
# 	if n[index] not in empty_list:
# 		empty_list.append(n[index])
# 	index=index+1
# print(empty_list)
		
# =================================================================

# question 5

# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# index=0
# x=mainStr.split()
# x.pop()
# x.replace("on")
# print(x)

# ==============================================

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# odd=0
# even=0
# sum=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		print(elements[index]," " + "it is a even number") 
# 		even=even+1
# 	else:
# 		print(elements[index]," "+ "it is odd number")
# 		odd=odd+1
# 	sum=sum+elements[index]
# 	index=index+1
# print(odd,"this are total numbers of odd nummbers")	
# print(even,"this is total numbers of even numbers")
# print(sum,"total sum")		
	

# ======================================================


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# odd=0
# even=0
# sum=0
# average=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		print(elements[index]," " + "it is a even number") 
# 		even=even+1
# 	else:
# 		print(elements[index]," "+ "it is odd number")
# 		odd=odd+1
# 	sum=sum+elements[index]
# 	average=sum/len(elements)
# 	index=index+1
# print(odd,"this are total numbers of odd nummbers")	
# print(even,"this is total numbers of even numbers")
# print(sum,"total sum")		
# print(average)


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# odd=0
# even=0
# sum=0
# average=0
# while index<len(elements):
# 	if elements[index]%2==0:
# 		print(elements[index],"it is even numbers")
# 		even=even+1
# 	else:
# 		print(elements[index],"it is odd numbrs")
# 		odd=odd+1
# 	sum=sum+elements[index]
# 	average=sum/len(elements)
# 	index=index+1
# print(even,"total number of even number")	
# print(odd,"total number of odd number")	
# print(sum)
# print(average)




# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000,
# 					 690909090, 31010101, 532010, 510, 4100]

# Crorepati=0
# Lakhpati=0
# Dilwale=0
# index=0
# count=0
# while index<len(kitna_paisa_hai):
# 	if kitna_paisa_hai[index]>=10000000:
# 		print(kitna_paisa_hai[index],"they are Crorepati")
# 		Crorepati=Crorepati+1
# 	elif kitna_paisa_hai[index]>=100000:
# 		print(kitna_paisa_hai[index],"they are lakhpati")
# 		Lakhpati=Lakhpati+1
# 	else:
# 		print(kitna_paisa_hai[index],"they are dilwale")
# 		Dilwale=Dilwale+1
# 	count=count+1
# 	index=index+1
# print(Crorepati,"total Crorepati are")
# print(Lakhpati,"total lakhpati are")
# print(Dilwale,"total dilwale ares")	
# print(count)		


# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# a=0
# n=0
# t=0
# x=0
# u=0
# g=0
# index=0
# while index<len(char_list):
# 	if char_list[index]=="a":
# 		a=a+1
# 	elif char_list[index]=="n":
# 		n=n+1
# 	elif char_list[index]=="t":
# 		t=t+1
# 	elif char_list[index]=="x":
# 		x=x+1
# 	elif char_list[index]=="u":
# 		u=u+1			
# 	else:
# 		g=g+1
# 	index=index+1
# print("a =",a,"n =",n,"t =",t,"x =",x,"u =",u,"g =",g)

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# list1=[]
# index=0
# while index<len(n):
# 	if n[index] not in list1:
# 		list1.append(n[index])
# 	index=index+1
# print(list1)			

# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# list1=[]
# index=0
# while index<(char_list):
	# if char_list[index]not in list1:
		# list1.append(char_list[index])
	# index=index+1
# print(list1)		

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# sum=0
# index=0
# while index<len(marks):
# 	sum=sum+int(marks[index])
# 	index=index+1
# print(sum)	



# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	total_marks = total_marks + int(marks[counter])
# 	counter = counter + 1
# print(total_marks)	

# name = ["Savitri", "Phule", "26"]
# # Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print (name[0]+" "+name[1]+" "+name[2])
# # Code mei dekhiye naam theek se print kyu nahi ho raha

