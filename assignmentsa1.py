# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NugYQZE-IYF9EElI9zsXNfZD7RuiGVjG

#ques 1
"""

credits=int(input())
if credits>=7500 : 
  print("Tera leader")
elif 6000 <= credits < 7500 :
   print("Gega leader")
elif 6000 <= credits < 7500 : 
  print("Gega leader")
else :
  print("Rising star")

"""#ques 2"""

P = float(input())
R = float(input())
t= float(input())
simpleinterest =P*(1/100)*R*t
print(simpleinterest)

"""#ques 3"""

def compute_gcd(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
    return gcd
num1 = 54 
num2 = 24
print("The gcd is", compute_gcd(num1, num2))

"""#ques 4"""

def evenSeries(n):
    i = 2 # Assigning first term of the series
    for x in range(1,n):
        if(x!=n-1):
            print(i,end=", ")
        else:
            print(i," .")
        i+= 4*x 
evenSeries(int(input("Enter number of terms : ")))

"""#ques 5"""

n=100000
n=str(n)
deep=len(n)
print(deep)

"""#ques 6"""

n = 9735
rev = 0
 
while(n > 0):
    num = n % 10
    rev = rev * 10 + num
    n = n // 10
 
print(rev)

"""#ques 7

#pattern a
"""

for i in range(5):
  for j in range(i+1):
    print("* ",end="")
  print()

"""#pattern b"""

n=5
for i in range(1,n+1):
	for j in range(1,i+1):
	    	print(j,end=" ")
	print()

"""#pattern c"""

odd=1
space=3
for i in range(1,5):
    k=0
    for j in range(1,space+1):
       print(" ",end=" ")
    for j in range(1,odd+1):
       if j<=i:
	        k=k+1
       else:
	        k=k-1
       print(k,end=" ")
    print()
    odd=odd+2
    space=space-1

"""#pattern f"""

n=5
for i in range(n):
   print(" "*(n-i-1)+"* "*(i+1))
for j in range(n-1,0,-1):
   print(" "*(n-j)+"* "*(j))

"""# pattern g """

a=5
spaces=2*a-2
for i in range (1,a):
  print("*"*i+" "*spaces+"*"*i)
  spaces=spaces-2
spaces=0
for j in range(a,0,-1):
 print("*"*j+" "*spaces+"*"*j)
 spaces=spaces+2

"""#pattern h"""

n=5
for i in  range(n,0,-1):
  for j in range(i,0,-1):
    print("*",end=" ")
  for j in range(2*(n-i)):#for space
    print(" ",end=" ")
  for j in range(i+1,1,-1):
    print("*",end=" ")
  print()
for i in  range(1,n):
  for j in range(i+1):
    print("*",end=" ")
  for j in range(2*(n-i-1)):#for space
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()