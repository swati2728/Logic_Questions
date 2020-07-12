# for i in range(0,3):
# 	for j in range(0,3):
# 		print(i,j


# ========================================


# for i in range(0,7):
# 	for j in range(0,7):
# 		print(" ")
# 	print("0")	

# ================================

# for i in range(0,7):
# 	for j in range(0,7):
# 		print(" ",end="")
# 	print("0")

# =========================================


# for i in range(0,7):
# 	for j in range(0,7-i):
# 		print(" ",end="")
# 	print("0")	

# ========================================

# for i in range(0,7):
# 	for j in range(0,7-i):
# 		print(" ",end="")
# 	for k in range(0,i*2+1):
# 		print("0",end="")
# 	print("")

# =====================================
user = int(input("enter a number"))
i = 1
for row in range(1,user+1):
	for col in range(1,row+1):
		print(i,end="")
		i = i+1	
	print()

# =======================================


