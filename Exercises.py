
#Exercice N°1

for i in range(-998, 2340):
	if (i%7==0):
		print(i, "is devisible by 7")
for i in range(-998, 2340):
	if (i%5==0):
		print(i, "is a multiple of 5")

#Exercice N°2

word=str(input("Enter a word that you want to reverse:"))
L= list(word)
print ("Your reversed word is:",''.join(list(reversed(L))))

#Exercice N°3
print("Fibonacci Serie from 0 to 50:")

def Fib(n):  
   if n <= 1:  
       return n  
   else:  
       return (Fib(n-1) + Fib(n-2))  
for i in range(0,50):
	if Fib(i)<50:
		print(Fib(i))
	else:
		break


#Exercice N°4

x=int(input("Enter your value thet you wanna sum its serie of numbers:"))
somme=0
for i in range(0,x+1):
	somme=somme+i
print("The sum of your numbers is:", somme)

#Exercice N°5

L1=["Khobz",5,"Kilo ba6a6a", 255]
L2=[]
for i in L1:
	L2.append(i)
print("List 2 Elements:",L2)

#Exercice N°6

a=int(input("Please enter the value of a:"))
b=int(input("Please enter the value of b:"))
c=int(input("Please enter the value of c:"))
if a%c==0:
	print("a is devisible by c")
else:
	print("a is not devisible by c")
if b%c==0:
	print("b is devisible by c")
else:
	print("b is not devisible by c")

#Exercice N°7
x=int(input("Insert your range (if it's 100 insert 101 (n+1)"))
print("Printing numbers from your range:")
for i in range(x):
	print(i)
print("Printing only prime numbers from your range:")
if (2 in range(x)):
	print(2)
if (3 in range(x)):
	print(3)
if (5 in range (x)):
	print(5)
for j in range(x):
	if (j%2!=0 and j%3!=0 and j%5!=0):
		print(j)
