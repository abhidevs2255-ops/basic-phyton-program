x = int(input())
count=0
while x!=0:
   k=x%10
   if k==0:
      count=count+1
   x=x//10
print(count)
