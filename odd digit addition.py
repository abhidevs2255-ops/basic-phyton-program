#x =153
x= int(input())
sum=0
while x!=0:
  k = x%10
  if k%2!=0:
    sum =sum + k
  x =x//10
print(sum)
