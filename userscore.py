def score(남은마권카드,낸카드,horsename,horsecards,user_horsecard,P2_horsecard,P3_horsecard,actioncards,user_actioncard,P2_actioncard,P3_actioncard,user):

    one=horsename[0]
    two=horsename[1]
    three=horsename[2]
    four=horsename[3]
    five=horsename[4]
    six=horsename[5]
    seven=horsename[6]

    user_score=0
    P2_score=0
    P3_score=0

    for i in range(2):
        if P2_horsecard[i][0:2]==one:
            P2_score+=10
        elif P2_horsecard[i][0:2]==two:
            P2_score+=8
        elif P2_horsecard[i][0:2]==three:
            P2_score+=6
        elif P2_horsecard[i][0:2]==four:
            P2_score+=4
        elif P2_horsecard[i][0:2]==five:
            P2_score+=3
        elif P2_horsecard[i][0:2]==six:
            P2_score+=2
        elif P2_horsecard[i][0:2]==seven:
            P2_score+=1

    for i in range(2):
        if P3_horsecard[i][0:2]==one:
            P3_score+=10
        elif P3_horsecard[i][0:2]==two:
            P3_score+=8
        elif P3_horsecard[i][0:2]==three:
            P3_score+=6
        elif P3_horsecard[i][0:2]==four:
            P3_score+=4
        elif P3_horsecard[i][0:2]==five:
            P3_score+=3
        elif P3_horsecard[i][0:2]==six:
            P3_score+=2
        elif P3_horsecard[i][0:2]==seven:
            P3_score+=1

    
    for i in range(2):
        if user_horsecard[i][0:2]==one:
            user_score=user_score+10
        elif user_horsecard[i][0:2]==two:
            user_score=user_score+8
        elif user_horsecard[i][0:2]==three:
            user_score=user_score+6
        elif user_horsecard[i][0:2]==four:
            user_score=user_score+4
        elif user_horsecard[i][0:2]==five:
            user_score=user_score+3
        elif user_horsecard[i][0:2]==six:
            user_score=user_score+2
        elif user_horsecard[i][0:2]==seven:
            user_score=user_score+1


    print("P2님의 총점 :",P2_score)
    print("P3님의 총점 :",P3_score)
    print(user+"님의 총점 :",user_score)

    
    def rank(user_score,P2_score,P3_score):
        hi={}
        hi[user]=(user,user_score)
        hi['P2']=('P2',P2_score)
        hi['P3']=('P3',P3_score)

        a=sorted(hi.items(),key=lambda x: x[1][1])

        print(" ")
        print("♞♞♞♞♞♞♞순위 발표♞♞♞♞♞♞♞♞")
        print("♞1등♞ :",a[2][1][0])
        print("♞2등♞ :",a[1][1][0])
        print("♞3등♞ :",a[0][1][0])
        
    rank(user_score,P2_score,P3_score)

    


