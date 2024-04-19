while(True):
    print("수학 연산 프로그램입니다.")
    n=int(input("1. 집합 연산 2. 절댓값 3. 거듭제곱 4. 종료\n입력: "))
    if(n==1):
        print("집합을 구하는 프로그램 입니다.")
        a={1,2,3,4,5,6,7}
        b={2,3,4,8,9,10}
        print("a집합: ",a)
        print("b집합: ",b)
        while(True):
            print("구하고 싶은 집합을 선택하시오.")
            m=int(input("1. 합집합 2. 교집합 3. 차집합 4. 종료\n입력: "))
            if(m==1):
                print("a와 b의 합집합: ",a|b)
            elif(m==2):
                print("a와 b의 교집합: ",a&b)
            elif(m==3):
                print("a에서 b를 뼨 차집합: ",a-b)
            else:
                print("종료합니다...")
                break
    elif(n==2):
        print("절댓값을 구하는 프로그램입니다")
        m=int(input("구하고 싶은 절댓값을 입력하시오: "))
        print("절댓값은 ", abs(m),"입니다.")
    elif(n==3):
        print("거듭제곱을 구하는 프로그램입니다.")
        m=int(input("구하고 싶은 거듭제곱의 아래값을 입력하시오:"))
        k=int(input("지수 값을 입력하시오: "))
        print("거듭 제곱의 값은 ",m**k,"입니다.")
    else:
        print("종료합니다...")
        break;
