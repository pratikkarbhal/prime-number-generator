#This function generates all the prime numbers between 2 and n
def prime_generator(n):
prime=[True for i in range(n+1)]
p=2
while(p*p<=n):
if(prime[p]==True):
for i in range(p*p,n+1,p):
prime[i]=False
p+=1
return prime
t=int(input("Enter number of test cases="))
while(t!=0):
m=int(input("Enter the lower bound="))
n=int(input("Enter the upper bound="))
prime=prime_generator(n)
for i in range(m,n+1):
if(prime[i]):
print(i, end=" ")
t-=1
print()
print()
