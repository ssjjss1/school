# 중간 고사
#학번 : 20241559
#이름 : 서준성

#1번

n=int(input("단(2~9) 입력: "))
while(n<=1 or n>=10):
    print("2~9 사이만 입력 가능합니다.\n")
    n=int(input("단(2~9) 입력: "))
print(f"=== {n}단 ===")
for i in range(1,10):
    if(len(str(n*i))==1):
        print(f"{n} * {i} =  {n*i}")
    else:
        print(f"{n} * {i} = {n*i}")

#2번
"""
n=int(input("정수 입력: "))
while(True):
    if(n<3):
        print("3이상의 숫자만 입력해주세요.\n")
        n=int(input("정수 입력: "))
    elif(n%3==0):
        print("3의 배수가 아닌 숫자를 입력하세요.\n")
        n=int(input("정수 입력: "))
    else:
        break
sum=0
for i in range(1,n+1):
    if(i==1):
        print("1/1 ",end="")
        sum+=1
    elif(i%2==0):
        print(f"+ 1/{i} ",end="")
        sum+=1/i
    elif(i%2!=0):
        print(f"- 1/{i} ",end="")
        sum-=1/i
print(f"= %0.1f" %sum)
"""
#3번
"""
import random
n1=random.randint(10,40)
n2=random.randint(10,40)
while(n1<n2):
    n1=random.randint(10,40)
    n2=random.randint(10,40)
print("랜덤 숫자 2개를 발생합니다.")
print(f"n1 = {n1}, n2 = {n2}")
print()
print(f"{n1} / {n2} = ",end="")
print("%0.1f"%(n1/n2))
print(f"{n1} % {n2} = ",end="")
print("%d"%(n1%n2))
"""
#4번
"""
while(True):
    n=int(input("3자리 숫자 입력: "))
    while(True):
        if(n//100>=1 and n//100<=9):
            break
        else:
            print("3자리 숫자만 입력하시오.\n")
            n=int(input("3자리 숫자 입력: "))
    max=0
    sum=10
    while(n>0):
        k=n%10
        if(max<k):
            max=k
        if(sum>k):
            sum=k
        n//=10
    print(f"최댓값은 {max}, 최솟값은 {sum}입니다.")
    s=input("종료하시겠습니까? (yes/no) : ")
    if(s=="yes"):
        print("종료합니다.")
        break
    print()
    """
