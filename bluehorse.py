import random
def horseplay(): #경주마카드
    horsename=["♞A","♞B","♞C","♞D","♞E","♞F","♞G"]
    random.shuffle(horsename)
    return horsename

def horsecard(): #마권카드
    horsecards=["♞A1","♞A2","♞B1","♞B2","♞C1","♞C2","♞D1","♞D2","♞E1","♞E2","♞F1","♞F2","♞G1","♞G2"]
    random.shuffle(horsecards)
    return horsecards

def hit1(horsecards):
    if horsecards==[]:
        horsecards=horsecard()
    return (horsecards[0:2],horsecards[2:])

def actioncard():
    actionname=["♞A ±1","♞B ±1","♞C ±1","♞D ±1","♞E ±1","♞F ±1","♞G ±1"]
    actionrank=[" 1st +3"," 1st +2"," 1st +6"," 2nd +2"," 2nd +3"," 3rd +1"," 3rd -2"," 4th +1"," 4th -2"," 5th -3"," 6th -3"," 7th -2"]
    actionchange=["   ↔  "]
    actioncards=[]
    actioncards=actionname+actionrank+actionchange
    random.shuffle(actioncards)
    return actioncards


def hit2(actioncards):
    if actioncards==[]:
        actioncards=actioncard()
    return (actioncards[0:5],actioncards[5:])




from useraction import *
from P2action import *
from P3action import *
from userscore import *
import time



def bluehorse():
    print("\n☆★☆★☆★☆★☆★영찬이개빠름 WORLD에 오신 것을 환영합니다!★☆★☆★☆★☆★☆")
    play = input("\n게임을 시작하시겠습니까? (예/아니오)")
    print("\n")
    
    if play == "예":
        print("♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞")
        print("♞"+"\t"*9,"     ♞")
        user=input("♞이름을 입력하세요.")
        print("♞"+"\t"*9,"     ♞")
        print("♞경주마 랜덤 배치 시작!"+"\t"*6+"      ♞")
        horsename=horseplay()
        time.sleep(1)
        print("♞"+"\t"*3+"<<<<<<< 경주마 랭킹 >>>>>>>"+"\t"*3+"      ♞\n♞"+"\t"*9,"     ♞")
        print("♞     1          2          3          4          5          6          7    ♞") 
        print("♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞\n"
              "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
              "♞│",horsename[0],"ㅣ","│",horsename[1]," ㅣ","│",horsename[2]," ㅣ","│",horsename[3]," ㅣ","│",horsename[4]," ㅣ","│",horsename[5]," ㅣ","│",horsename[6]," ㅣ♞\n"
              "♞ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ","ㅣ      ㅣ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ ♞")
        
        horsecards=horsecard()
        card,horsecards=hit1(horsecards)
        user_horsecard=card
        card,horsecards=hit1(horsecards)
        P2_horsecard=card
        card,horsecards=hit1(horsecards)
        P3_horsecard=card
        남은마권카드=horsecards
        print("♞"+"\t"*9,"     ♞")
        print("♞"+"\t"*9,"     ♞")
        print("♞"+user+",P2,P3님, 마권카드를 나눠드리겠습니다."+"\t"*4+"      ♞")
        time.sleep(1)
        print("♞"+user+"님의 마권카드 :"+"\t"*7+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
              #"♞ㅣ      ㅣ","ㅣ      ㅣ"+"\t"*7+"      ♞\n"
              "♞│",user_horsecard[0],"ㅣ","│",user_horsecard[1],"ㅣ"+"\t"*7+"      ♞\n"
              #"♞ㅣ      ㅣ","ㅣ      ㅣ"+"\t"*7+"      ♞\n"
              "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")
              
        '''print("P2님의 마권카드 :\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n"
              "ㅣ      ㅣ","ㅣ      ㅣ\n"
              "│   ?  ㅣ","│   ?  ㅣ\n"
              "ㅣ      ㅣ","ㅣ      ㅣ\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n")
              
        print("P3님의 마권카드 :\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n"
              "ㅣ      ㅣ","ㅣ      ㅣ\n"
              "│   ?  ㅣ","│   ?  ㅣ\n"
              "ㅣ      ㅣ","ㅣ      ㅣ\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n")'''

        actioncards=actioncard()
        card,actioncards=hit2(actioncards)
        user_actioncard=card
        card,actioncards=hit2(actioncards)
        P2_actioncard=card
        card,actioncards=hit2(actioncards)
        P3_actioncard=card
        print("♞"+"\t"*9,"     ♞")
        print("♞"+"\t"*9,"     ♞")
        print("♞"+user+",P2,P3님, 액션카드를 나눠드리겠습니다."+"\t"*4+"      ♞")
        time.sleep(1)
        print("♞"+user+"님의 액션카드 :"+"\t"*7+"      ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞│",user_actioncard[0]," ㅣ","│",user_actioncard[1]," ㅣ","│",user_actioncard[2]," ㅣ","│",user_actioncard[3]," ㅣ","│",user_actioncard[4]," ㅣ"+"  ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞")
        print("♞"+"\t"*9,"     ♞")
        print("♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞\n")
                    
              
              #,user_actioncard,"\nP2님의 액션카드 : ['ㅁ','ㅁ','ㅁ','ㅁ','ㅁ']\nP3님의 액션카드 : ['ㅁ','ㅁ','ㅁ','ㅁ','ㅁ']\n")

        '''P2_actionshape = "P2님의 액션카드 :\n"
              " ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ\n"
              "ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ\n"
              "│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ\n"
              "ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ\n"
              " ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ\n"
        P3_actionshape = "P3님의 액션카드 :\n"
              " ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ\n"
              "ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ\n"
              "│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ","│    ?     ㅣ\n"
              "ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ\n"
              " ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ\n"'''

        cardshape="?"
        P2cardcount = [cardshape,cardshape,cardshape,cardshape,cardshape]
        P3cardcount = [cardshape,cardshape,cardshape,cardshape,cardshape]

        
        time.sleep(2)
        for i in range(5):
            L="~"+str(len(user_actioncard))
            LL=int(len(user_actioncard))
            
            if i == 4:
                L = ""
            print("♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞"+"ROUND"+str(i+1)+"♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞♞")
            print("♞"+"\t"*9,"     ♞")
            print("♞"+"※'+'는 오른쪽으로, '-'는 왼쪽으로 경주마가 이동합니다.","\t"*2+"      ♞")
            print("♞"+"\t"*9,"     ♞")
            #print("♞P2님의 액션카드 :"+"\t"*7+"      ♞\n"
            print("♞      1              2              3              4              5         ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞│    "+P2cardcount[4]+"     ㅣ","│    "+P2cardcount[3]+"     ㅣ","│    "+P2cardcount[2]+"     ㅣ","│    "+P2cardcount[1]+"     ㅣ","│    "+P2cardcount[0]+"     ㅣ"+"  ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞")
            print("♞P2님, 액션카드 한 장을 고르세요.(1"+L+")"+"\t"*5+"      ♞")
            time.sleep(2)
            
            낸카드 = P2_actioncard[i]
            #print("♞고른 액션카드 :"+"\t"*7+"      ♞")
            print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                  #"ㅣ          ㅣ\n"
                  "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                  #"ㅣ          ㅣ\n"
                  "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")
            
            P2action(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
            
            #P2cardcount.remove(P2cardcount[0])
            P2cardcount[i]='X'
            
            
            #print("P3님의 액션카드 :\n"
            print("♞      1              2              3              4              5         ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞│    "+P3cardcount[4]+"     ㅣ","│    "+P3cardcount[3]+"     ㅣ","│    "+P3cardcount[2]+"     ㅣ","│    "+P3cardcount[1]+"     ㅣ","│    "+P3cardcount[0]+"     ㅣ"+"  ♞\n"
              #"♞ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ"+"  ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞")
            print("♞P3님, 액션카드 한 장을 고르세요.(1"+L+")"+"\t"*5+"      ♞")
            time.sleep(2)
            낸카드 = P3_actioncard[i]
            print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                  #"ㅣ          ㅣ\n"
                  "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                  #"ㅣ          ㅣ\n"
                  "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")
            print("♞"+"\t"*9,"     ♞")

            P3action(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
            #P3cardcount.remove(P3cardcount[0])
            P3cardcount[i]='X'
            
            #print(user+"님의 액션카드 :\n"
            print("♞      1              2              3              4              5         ♞\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞")
              #"ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ")
            if i == 0:
                print("♞│",user_actioncard[0]," ㅣ","│",user_actioncard[1]," ㅣ","│",user_actioncard[2]," ㅣ","│",user_actioncard[3]," ㅣ","│",user_actioncard[4]," ㅣ"+"  ♞")
            elif i == 1:
                print("♞│",user_actioncard[0]," ㅣ","│",user_actioncard[1]," ㅣ","│",user_actioncard[2]," ㅣ","│",user_actioncard[3]," ㅣ","│    X     ㅣ"+"  ♞")
            elif i == 2:
                print("♞│",user_actioncard[0]," ㅣ","│",user_actioncard[1]," ㅣ","│",user_actioncard[2]," ㅣ","│    X     ㅣ","│    X     ㅣ"+"  ♞")
            elif i == 3:
                print("♞│",user_actioncard[0]," ㅣ","│",user_actioncard[1]," ㅣ","│    X     ㅣ","│    X     ㅣ","│    X     ㅣ"+"  ♞")
            elif i == 4:
                print("♞│",user_actioncard[0]," ㅣ","│    X     ㅣ","│    X     ㅣ","│    X     ㅣ","│    X     ㅣ"+"  ♞")
            elif i == 5:
                print("♞│    X     ㅣ","│    X     ㅣ","│    X     ㅣ","│    X     ㅣ","│    X     ㅣ"+"  ♞")
                
            print(#"ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ","ㅣ          ㅣ\n"
              "♞ ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ","  ㅡㅡㅡㅡㅡㅡ"+"   ♞")
            

            while True:
                print("♞"+user+"님의 마권카드 :"+"\t"*7+"      ♞\n"
                      "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞\n"
                      #"♞ㅣ      ㅣ","ㅣ      ㅣ"+"\t"*7+"      ♞\n"
                      "♞│",user_horsecard[0],"ㅣ","│",user_horsecard[1],"ㅣ"+"\t"*7+"      ♞\n"
                      #"♞ㅣ      ㅣ","ㅣ      ㅣ"+"\t"*7+"      ♞\n"
                      "♞ ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ"+"\t"*7+"      ♞")
                user내는카드 = input("♞"+user+"님, 액션카드 한 장을 고르시오.(1"+L+")")

                if int(user내는카드)>0 and int(user내는카드)<=LL:
                    
                    if user내는카드 == "1":
                        낸카드 = user_actioncard[0]
                        print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")
                        user_actioncard=user_actioncard[1:]
                        useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                        break
                    elif user내는카드 == "2":
                        낸카드 = user_actioncard[1]
                        print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")

                        user_actioncard=[user_actioncard[0]]+user_actioncard[2:]
                        useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                        break
                    elif user내는카드 == "3":
                        낸카드 = user_actioncard[2]
                        print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")

                        user_actioncard=user_actioncard[0:2]+user_actioncard[3:]
                        useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                        break
                    elif user내는카드 == "4":
                        낸카드 = user_actioncard[3]
                        print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")

                        user_actioncard=user_actioncard[0:3]+user_actioncard[4:]
                        useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                        break
                    elif user내는카드 == "5":
                        낸카드 = user_actioncard[4]
                        print("♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞│",낸카드," ㅣ"+"\t"*7+"      ♞\n"
                              #"ㅣ          ㅣ\n"
                              "♞ ㅡㅡㅡㅡㅡㅡ"+"\t"*8+"      ♞")

                        user_actioncard=user_actioncard[0:4]+user_actioncard[5:]
                        useraction(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)
                        break
                    else:
                        continue
                
         

            print("--------------------------------------------------------------------------------")
        print("게임 종료")
        print(user+"님의 마권카드 :\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "│",user_horsecard[0],"ㅣ","│",user_horsecard[1],"ㅣ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n")
        print("P2님의 마권카드 :\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "│",P2_horsecard[0],"ㅣ","│",P2_horsecard[1],"ㅣ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n")
        print("P3님의 마권카드 :\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              "│",P3_horsecard[0],"ㅣ","│",P3_horsecard[1],"ㅣ\n"
              #"ㅣ      ㅣ","ㅣ      ㅣ\n"
              " ㅡㅡㅡㅡ","  ㅡㅡㅡㅡ\n")
        score(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user)


    


                    

    elif play == "아니오":
        print("안녕~")

    else:
        bluehorse()
    


bluehorse()

