#기말고사
#학번: 20241559
#이름: 서준성
#1
"""
while(True):
    n=input("패스워드 입력: ")
    if(len(n)<9):
        print("9자 이상 입력하세요.")
    else:
        a=0
        b=0
        flag=True
        for i in n:
            if(i>='1' and i<='9'):
                print("패스워드 사용 불가(숫자 사용 X)")
                flag=False
                break
            if(i>='a' and i<='z'):
                a+=1
            elif(i>='A' and i<='Z'):
                b+=1
        if(a>=1 and b>=1 and flag==True):
            print("패스워드 사용 가능")
            break
        elif(a>=1 and b==0 and flag==True):
            print("패스워드 사용 불가(대문자 없음)")
        elif(a==0 and b>=1 and flag==True):
            print("패스워드 사용 불가(소문자 없음)")
    print()
    """
#2
"""
import random
while(True):
    n=input("주사위를 던지시겠습니까? (Y/y or N/n): ")
    if(n.lower()=="y"):
        a=random.randint(1,6)
        b=random.randint(1,6)
        print(f"[인간] 주사위: {a}, [컴퓨터] 주사위: {b}")
        if(a==b):
            print("무승부")
        elif(a>b):
            print("인간 승리")
        elif(a<b):
            print("컴퓨터 승리")
    elif(n.lower()=="n"):
        print("종료합니다.")
        break
    else:
        print("다시입력하세요.")
    print()
"""
#3
"""
import random
l=[]
while(True):
    n=random.randint(1,45)
    flag=True
    for i in l:
        if(i==n):
            flag=False
            break
    if(flag==True):
        l.append(n)
    if(len(l)==6):
        break
l.sort(reverse=True)
print("내림차순 정렬된 로또 번호를 출력합니다.")
print(l)
"""
#4

import random
print("="*8,"메뉴","="*8)
print("1. 과일 추천 (fun1 함수)")
print("2. 과일 추가 (fun2 함수)")
print("3. 과일 삭제 (fun3 함수)")
print("4. 종료")
print("="*22)
a=["사과","바나나","포도","딸기"]
def fun1():
    print(f"'{a[random.randint(0,3)]}'을(를) 추천합니다.")
def fun2(s):
    a.append(s)
    print(f"추가된 과일 리스트를 출력합니다.\n{a}")
def fun3(s):
    a.remove(s)
    print(f"{s} 삭제 후 과일 리스트를 출력합니다.\n{a}")
while(True):
    k=int(input("메뉴 입력: "))
    if(k==1):
        fun1()
    elif(k==2):
        s=input("추가할 과일 입력: ")
        fun2(s)
    elif(k==3):
        s=input("삭제할 과일 입력: ")
        fun3(s)
    elif(k==4):
        print("종료합니다.")
        break
    else:
        print("1~4만 입력 가능합니다.")
    print()