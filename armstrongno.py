n=int(input("enter number: "))
sum=0
while n>=0:
	r=n%10
	sum=sum+r
n=n+1
if n==sum:
	print ("armstrong number")
else:
	print ("not armstrong number")