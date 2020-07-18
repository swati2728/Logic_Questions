num = 1
while num <= 100:
	i = 1
	while i <= 100:
		user=int(input("enter a number"))
		if user%2==0:
			print("it is prime")
		else:
			print("not a prime")
	print()
	num=num+1
	i=i+1			
# ==============================================


# a=1
# while a<=100:
# 	if a>1:
# 		b=2
# 		prime=True
# 		while b<a:
# 			if a%b==0:
# 				print(a,"it is not a prime")
# 				prime=False
# 				break
# 			b=b+1
# 		if(prime):
# 			print(a,'it is prime')
# 	a=a+1

# # # =======================================================
# num=1
# while num<=10:
# 	b=1
# 	while b<=10:
# 		product=num*b
# 		print(num,"*",b,"=",product,)
# 		b=b+1
# 	print("")
# 	num=num+1		

# # =======================================================


# user1=int(input("enter a number"))
# user2=int(input("enter a number"))
# while user1<=user2:
# 	b=1
# 	while b<=10:
# 		product=user1*b
# 		print(user1,"*",b,"=",product," ")
# 		b=b+1
# 	print("")
# 	user,1=user1+1

# ===========================================================/
# pattern questions
# i=1
# while i<=5:
# 	j=1
# 	while j<=5:
# 		print(j,end="")
# 		j=j+1
# 	print()
# 	i=i+1	
# ==============================================
# pattern questions

# a=1
# while a<=3:
# 	b=1
# 	while b<=3:
# 		print(b,end="")
# 		b=b+1
# 	print()
# 	a=a+1	





# ======================================
# reversed questions
# a=6545
# i=0
# while a>0:
# 	r=a%10
# 	i=i*10+r 
# 	a=a//10
# print(i)	
# ===============================================
# sum questions

# x=3256
# sum=0
# while x>0:
# 	i=x%10
# 	sum=sum+i
# 	x=x//10
# print(sum)	

# ========================================================


# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print (i, " is prime")
#    i = i + 1

# print ("Good bye!")