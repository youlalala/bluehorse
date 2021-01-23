import random
import time

aaa=["+","-"]
def P3action(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user):
    if 낸카드 == "♞A ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞A":
                a = i
            i=i+1

        if a ==0 :#A가 1등임
            if 쁠마 == "+":
                horsename[a],horsename[a+1]=horsename[a+1],horsename[a]
        elif a == 6: #A가 꼴등임
            if 쁠마 == "-":
                horsename[a],horsename[a-1]=horsename[a-1],horsename[a]
        else:
            if 쁠마 == "+":
                horsename[a],horsename[a+1]=horsename[a+1],horsename[a]
            else:
                horsename[a],horsename[a-1]=horsename[a-1],horsename[a]

    elif 낸카드 == "♞B ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞B":
                b = i
            i=i+1

        if b ==0 :#b가 1등임
            if 쁠마 == "+":
                horsename[b],horsename[b+1]=horsename[b+1],horsename[b]
        elif b == 6: #b가 꼴등임
            if 쁠마 == "-":
                horsename[b],horsename[b-1]=horsename[b-1],horsename[b]
        else:
            if 쁠마 == "+":
                horsename[b],horsename[b+1]=horsename[b+1],horsename[b]
            else:
                horsename[b],horsename[b-1]=horsename[b-1],horsename[b]

    elif 낸카드 == "♞C ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞C":
                c = i
            i=i+1

        if c ==0 :#c가 1등임
            if 쁠마 == "+":
                horsename[c],horsename[c+1]=horsename[c+1],horsename[c]
        elif c == 6: #c가 꼴등임
            if 쁠마 == "-":
                horsename[c],horsename[c-1]=horsename[c-1],horsename[c]
        else:
            if 쁠마 == "+":
                horsename[c],horsename[c+1]=horsename[c+1],horsename[c]
            else:
                horsename[c],horsename[c-1]=horsename[c-1],horsename[c]
    elif 낸카드 == "♞D ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞D":
                d = i
            i=i+1
        if d ==0 :#d가 1등임
            if 쁠마 == "+":
                horsename[d],horsename[d+1]=horsename[d+1],horsename[d]
        elif d == 6: #d가 꼴등임
            if 쁠마 == "-":
                horsename[d],horsename[d-1]=horsename[d-1],horsename[d]
        else:
            if 쁠마 == "+":
                horsename[d],horsename[d+1]=horsename[d+1],horsename[d]
            else:
                horsename[d],horsename[d-1]=horsename[d-1],horsename[d]

    elif 낸카드 == "♞E ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞E":
                e = i
            i=i+1
        if e ==0 :#e가 1등임
            if 쁠마 == "+":
                horsename[e],horsename[e+1]=horsename[e+1],horsename[e]
        elif e == 6: #e가 꼴등임
            if 쁠마 == "-":
                horsename[e],horsename[e-1]=horsename[e-1],horsename[e]
        else:
            if 쁠마 == "+":
                horsename[e],horsename[e+1]=horsename[e+1],horsename[e]
            else:
                horsename[e],horsename[e-1]=horsename[e-1],horsename[e]
                
    elif 낸카드 == "♞F ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞F":
                f = i
            i=i+1
        if f ==0 :#f가 1등임
            if 쁠마 == "+":
                horsename[f],horsename[f+1]=horsename[f+1],horsename[f]
        elif f == 6: #f가 꼴등임
            if 쁠마 == "-":
                horsename[f],horsename[f-1]=horsename[f-1],horsename[f]
        else:
            if 쁠마 == "+":
                horsename[f],horsename[f+1]=horsename[f+1],horsename[f]
            else:
                horsename[f],horsename[f-1]=horsename[f-1],horsename[f]

    elif 낸카드 == "♞G ±1":
        print("♞+ or - 중 선택하시오."+"\t"*7+"      ♞")
        random.shuffle(aaa)
        쁠마 = aaa[0]
        time.sleep(2)
        print("♞"+쁠마+"\t"*9+"      ♞")
        i=0
        for x in horsename:
            if x == "♞G":
                g = i
            i=i+1
        if g ==0 :#g가 1등임
            if 쁠마 == "+":
                horsename[g],horsename[g+1]=horsename[g+1],horsename[g]
        elif g == 6: #g가 꼴등임
            if 쁠마 == "-":
                horsename[g],horsename[g-1]=horsename[g-1],horsename[g]
        else:
            if 쁠마 == "+":
                horsename[g],horsename[g+1]=horsename[g+1],horsename[g]
            else:
                horsename[g],horsename[g-1]=horsename[g-1],horsename[g]

    elif 낸카드 == " 1st +3":
        for i in range(3):
            horsename[i],horsename[i+1]=horsename[i+1],horsename[i]
    elif 낸카드 == " 1st +2":
        for i in range(2):
            horsename[i],horsename[i+1]=horsename[i+1],horsename[i]
    elif 낸카드 == " 1st +6":
        for i in range(6):
            horsename[i],horsename[i+1]=horsename[i+1],horsename[i]
    elif 낸카드 == " 2nd +2":
        for i in range(2):
            horsename[i+1],horsename[i+2]=horsename[i+2],horsename[i+1]
    elif 낸카드 == " 2nd +3":
        for i in range(3):
            horsename[i+1],horsename[i+2]=horsename[i+2],horsename[i+1]
    elif 낸카드 == " 3rd +1":
        for i in range(2,3):
            horsename[i],horsename[i+1]=horsename[i+1],horsename[i]
    elif 낸카드 == " 3rd -2":
        for i in range(2,0,-1):
            horsename[i],horsename[i-1]=horsename[i-1],horsename[i]
    elif 낸카드 == " 4th +1":
        for i in range(3,4):
            horsename[i],horsename[i+1]=horsename[i+1],horsename[i]
    elif 낸카드 == " 4th -2":
        for i in range(3,1,-1):
            horsename[i],horsename[i-1]=horsename[i-1],horsename[i]
    elif 낸카드 == " 5th -3":
        for i in range(4,1,-1):
            horsename[i],horsename[i-1]=horsename[i-1],horsename[i]
    elif 낸카드 == " 6th -3":
        for i in range(5,2,-1):
            horsename[i],horsename[i-1]=horsename[i-1],horsename[i]
    elif 낸카드 == " 7th -2":
        for i in range(6,4,-1):
            horsename[i],horsename[i-1]=horsename[i-1],horsename[i]
        #elif 낸카드 == "↔"
    elif 낸카드 == "   ↔  ":
        print("♞P3님의 마권카드 :"+"\t"*7+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "♞│   ?  ㅣ","│   ?  ㅣ"+"\t"*7+"      ♞\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")
        print("♞교환할 마권카드 한 장을 선택하세요."+"\t"*5+"      ♞")
        time.sleep(2)
        ss=[1,2]
        random.shuffle(ss)
        
        if ss[0] == 1:
            교환 = P3_horsecard[0]
            print("♞선택한 마권카드 :"+"\t"*7+"      ♞\n"
                  "♞ ㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                  "♞│ "+교환+" ㅣ"+"\t"*8+"      ♞\n"
                  "♞ ㅡㅡㅡㅡ"+"\t"*8+"      ♞")
        elif ss[0] == 2:
            교환 = P3_horsecard[1]
            print("♞선택한 마권카드 :"+"\t"*7+"       ♞\n"
                  "♞ ㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                  "♞│ "+교환+" ㅣ"+"\t"*8+"      ♞\n"
                  "♞ ㅡㅡㅡㅡ"+"\t"*8+"      ♞")
        
        i = 0
        for x in P3_horsecard:
            if x == 교환:
                change = i
            i=i+1
        P2_horsecard[change] = 남은마권카드[0]
        print("♞교환 후 P2님의 마권카드 :"+"\t"*6+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "♞│   ?  ㅣ","│   ?  ㅣ"+"\t"*7+"      ♞\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")

    
        


    print("♞"+"\t"*3+"<<<<<<< 경주마 랭킹 >>>>>>>"+"\t"*3+"      ♞\n"
          "♞     1          2          3          4          5          6          7    ♞") 
    print("♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞\n"
          "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
          "♞│",horsename[0]," ㅣ","│",horsename[1]," ㅣ","│",horsename[2]," ㅣ","│",horsename[3]," ㅣ","│",horsename[4]," ㅣ","│",horsename[5]," ㅣ","│",horsename[6]," ㅣ♞\n"
          "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
          "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞")
    print("♞"+"\t"*9,"     ♞")
