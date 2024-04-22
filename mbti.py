import matplotlib.pyplot as plt
def f():
  print("MBTI 성격 유형검사를 시작합니다. 각 질문에 대해 가장 적합한 답변을 선택해주세요.")
  a=["성격 유형 테스트 E(외향), I(내향)","성격 유형 테스트 S(감각), N(직관)","성격 유형 테스트 T(사고), F(감정)","성격 유형 테스트 J(판단), P(인식)"]
  b=[["1) 나는 말이 없어 주변 사람들이 답답해 할 때가 있다 2) 나는 말하기를 너무 좋아해서 실수 할 때가 종종 있다.","1) 나는 새로운 사람을 잘 만나지 않는다. 2)나는 새로운 사람들을 많이 만난다.","1) 나는 혼자서 하거나 소수로 하는 것이 편하다. 2) 나는 팀으로 일하는 것이 편하다"],
   ["1) 나는 현실적이다 2) 나는 미래 지향적이다","1) 나는 경험으로 판단한다 2) 나는 떠오르는 직관으로 판단한다.","1) 나는 상식적이다 2) 나는 창의적이다."],
    ["1) 나는 분석적이다 2) 나는 감수성이 풍부하다.","1) 나는 객관적이다 2) 나는 공감적이다.","1) 나는 경쟁한다 2) 나는 양보한다."],
     ["1) 나는 계획된 여행이 편하다. 2)나는 갑자기 떠나는 여행이 편하다.","1) 나는 계획적이고 조직적이다. 2) 나는 순발력을 믿는다.","1) 나는 규범을 좋아한다. 2) 나는 자유로운 것을 좋아한다."]]
  m = {
      "E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0
  }
  for i in range(0,4):
    print()
    print(a[i])
    print()
    for j in range(0,3):
      print(b[i][j])
      n = int(input("\n답변을 입력해주세요: "))
      print()
      while n <1 or n>3:
          n = int(input("\n다시 입력해주세요: "))
          print()
      if(n==1):
        if(i==0):
          m["I"]+=1
        elif(i==1):
          m["S"]+=1
        elif(i==2):
          m["T"]+=1
        elif(i==3):
          m["J"]+=1
      elif(n==2):
        if(i==0):
          m["E"]+=1
        elif(i==1):
          m["N"]+=1
        elif(i==2):
          m["F"]+=1
        elif(i==3):
          m["P"]+=1
      labels = m.keys()
      values = m.values()

  plt.figure(figsize=(8, 6))
  plt.bar(labels, values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray'])
  plt.title("MBTI reuslt")
  plt.xlabel("MBTI type")
  plt.ylabel("regularity")
  plt.show()
  print("\nMBTI 검사 결과:")
  print("E" if m["E"] > m["I"] else "I",end="")
  print("S" if m["S"] > m["N"] else "N",end="")
  print("T" if m["T"] > m["F"] else "F",end="")
  print("J" if m["J"] > m["P"] else "P",end="")
f()