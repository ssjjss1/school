sum=0
n=int(input())
for i in range(1,n+1):
  if(i==1): 
    print(f"{i}",end='')
    sum+=i
  else:
    if(i%2==0):
      print(f" + {i}",end='')
      sum+=i
    if(i%2!=0):
      print(f" - {i}",end='')
      sum-=i
print(f' = {sum}')