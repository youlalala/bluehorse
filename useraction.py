def useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user):
    if 낸카드 == "♞A ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞A":
                a = i
            i=i+1

        if a ==0 :#A가 1등임
            if 쁠마 == "+":
                horsename[a],horsename[a+1]=horsename[a+1],horsename[a]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif a == 6: #A가 꼴등임
            if 쁠마 == "-":
                horsename[a],horsename[a-1]=horsename[a-1],horsename[a]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                
        else:
            if 쁠마 == "+":
                horsename[a],horsename[a+1]=horsename[a+1],horsename[a]
            elif 쁠마 == "-":
                horsename[a],horsename[a-1]=horsename[a-1],horsename[a]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)

    elif 낸카드 == "♞B ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞B":
                b = i
            i=i+1

        if b ==0 :#b가 1등임
            if 쁠마 == "+":
                horsename[b],horsename[b+1]=horsename[b+1],horsename[b]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif b == 6: #b가 꼴등임
            if 쁠마 == "-":
                horsename[b],horsename[b-1]=horsename[b-1],horsename[b]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[b],horsename[b+1]=horsename[b+1],horsename[b]
            elif 쁠마 == "-":
                horsename[b],horsename[b-1]=horsename[b-1],horsename[b]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)

    elif 낸카드 == "♞C ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞C":
                c = i
            i=i+1

        if c ==0 :#c가 1등임
            if 쁠마 == "+":
                horsename[c],horsename[c+1]=horsename[c+1],horsename[c]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif c == 6: #c가 꼴등임
            if 쁠마 == "-":
                horsename[c],horsename[c-1]=horsename[c-1],horsename[c]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[c],horsename[c+1]=horsename[c+1],horsename[c]
            elif 쁠마 == "-":
                horsename[c],horsename[c-1]=horsename[c-1],horsename[c]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
    elif 낸카드 == "♞D ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞D":
                d = i
            i=i+1
        if d ==0 :#d가 1등임
            if 쁠마 == "+":
                horsename[d],horsename[d+1]=horsename[d+1],horsename[d]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif d == 6: #d가 꼴등임
            if 쁠마 == "-":
                horsename[d],horsename[d-1]=horsename[d-1],horsename[d]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[d],horsename[d+1]=horsename[d+1],horsename[d]
            elif 쁠마 == "-":
                horsename[d],horsename[d-1]=horsename[d-1],horsename[d]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)

    elif 낸카드 == "♞E ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞E":
                e = i
            i=i+1
        if e ==0 :#e가 1등임
            if 쁠마 == "+":
                horsename[e],horsename[e+1]=horsename[e+1],horsename[e]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif e == 6: #e가 꼴등임
            if 쁠마 == "-":
                horsename[e],horsename[e-1]=horsename[e-1],horsename[e]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[e],horsename[e+1]=horsename[e+1],horsename[e]
            elif 쁠마 == "-":
                horsename[e],horsename[e-1]=horsename[e-1],horsename[e]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                
    elif 낸카드 == "♞F ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞F":
                f = i
            i=i+1
        if f ==0 :#f가 1등임
            if 쁠마 == "+":
                horsename[f],horsename[f+1]=horsename[f+1],horsename[f]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif f == 6: #f가 꼴등임
            if 쁠마 == "-":
                horsename[f],horsename[f-1]=horsename[f-1],horsename[f]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[f],horsename[f+1]=horsename[f+1],horsename[f]
            elif 쁠마 == "-":
                horsename[f],horsename[f-1]=horsename[f-1],horsename[f]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)

    elif 낸카드 == "♞G ±1":
        쁠마=input("♞+ or - 중 선택하시오.")
        i=0
        for x in horsename:
            if x == "♞G":
                g = i
            i=i+1
        if g ==0 :#g가 1등임
            if 쁠마 == "+":
                horsename[g],horsename[g+1]=horsename[g+1],horsename[g]
            elif 쁠마 == "-":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        elif g == 6: #g가 꼴등임
            if 쁠마 == "-":
                horsename[g],horsename[g-1]=horsename[g-1],horsename[g]
            elif 쁠마 == "+":
                horsename
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
        else:
            if 쁠마 == "+":
                horsename[g],horsename[g+1]=horsename[g+1],horsename[g]
            elif 쁠마 == "-":
                horsename[g],horsename[g-1]=horsename[g-1],horsename[g]
            else:
                useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)

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
        print("♞"+user+"님의 마권카드 :"+"\t"*7+"      ♞\n"
                  "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
                  "♞│",user_horsecard[0],"ㅣ","│",user_horsecard[1],"ㅣ"+"\t"*7+"      ♞\n"
                  "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")
        def change():
            교환 = input("♞교환할 마권카드 한 장을 선택하세요.(1~2)")
            if 교환 == "1":
                user_horsecard[0] = 남은마권카드[0]
            elif 교환 == "2":
                user_horsecard[1] = 남은마권카드[0]
            else:
                change()
        change()

        print("♞교환 후 "+user+"님의 마권카드 :"+"\t"*6+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
              "♞│",user_horsecard[0],"ㅣ","│",user_horsecard[1],"ㅣ"+"\t"*7+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")
        
    print("♞"+"\t"*3+"<<<<<<< 경주마 랭킹 >>>>>>>"+"\t"*3+"      ♞\n♞"+"\t"*9,"     ♞")
    print("♞     1          2          3          4          5          6          7    ♞") 
    print("♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞\n"
          "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
          "♞│",horsename[0]," ㅣ","│",horsename[1]," ㅣ","│",horsename[2]," ㅣ","│",horsename[3]," ㅣ","│",horsename[4]," ㅣ","│",horsename[5]," ㅣ","│",horsename[6]," ㅣ♞\n"
          "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
          "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞")
    print("♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞")

