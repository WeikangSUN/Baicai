import random,time
class Poker():
    dict_all={'红桃':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],\
        '黑桃':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],\
        '方块':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],\
        '梅花':['A','2','3','4','5','6','7','8','9','10','J','Q','K']}
    list_all=[]
    joker=[('Red','Joker'),('Black','Joker')]
    for i in dict_all:
        for j in range(13):
            list_all.append((i,dict_all[i][j]))
    list_all+=joker
    #print(list_all)
    number_value={'A':13,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12}
    def __init__(self,player_num):
        self.player_num=player_num
        print('炸金花游戏现在开始！\n')
        time.sleep(2)
    def get_and_show(self):
        player_card=[]
        for i in range(self.player_num):
            player_card.append(1)
        list_game1=list(random.sample(self.list_all,3*self.player_num))
        for i in range(self.player_num):
            player_card[i]=[list_game1[i],list_game1[i+self.player_num],list_game1[i+2*self.player_num]]
        #print(player_card)
        return player_card
    def tonghuashun_rule_check(self,card):
        score=0
        card_type=[card[0][0],card[1][0],card[2][0]]
        typ_flag=len(set(card_type))
        card_number=[card[0][1],card[1][1],card[2][1]]
        card_value=[self.number_value[card_number[0]],self.number_value[card_number[1]],self.number_value[card_number[2]]]
        value_sorted=sorted(card_value)
        num_flag=value_sorted[2]-value_sorted[0]
        num_rep=len(set(card_number))
        if num_flag==0:                                  #炸弹   101-113
            score+=100+card_value[0]
        elif typ_flag==1 and num_flag==2:                #同花顺 81-93
            score+=80+value_sorted[2]
        elif typ_flag==1  and num_flag>2:                #同花   51-63
            score+=50+value_sorted[2]
        elif typ_flag>1  and num_flag==2 and num_rep==3: #顺子   31-43
            score+=30+value_sorted[2]
        elif num_rep==2:                                 #对儿   16-38
            score+=15+value_sorted[1]
        else:                                            #单儿   1-13
            score+=value_sorted[2]
        return score
    def score_making(self,card):
        num_joker=0
        card_number=[card[0][1],card[1][1],card[2][1]]
        score_list=[]
        final_score=0       
        for i in range(3):
            if card_number[i]=='Joker':
                num_joker+=1
                card_number[i]='2'
                k_joker=i
        card_value=[self.number_value[card_number[0]],self.number_value[card_number[1]],self.number_value[card_number[2]]]
        if num_joker==2:
            final_score=100+max(card_value)
        elif num_joker==1:
            list_subtitute=self.list_all
            for i in card:
                if i[1] != 'Joker':
                    list_subtitute.remove(i)               
            list_subtitute.remove(('Red','Joker'))
            list_subtitute.remove(('Black','Joker'))
            del card[k_joker]
            for i in list_subtitute: 
                card.append(i)               
                score_list.append(self.tonghuashun_rule_check(card))
                card.remove(i)
            final_score=max(score_list)
        else:
            final_score=self.tonghuashun_rule_check(card)
        return final_score
    def game_result(self,player_card):
        dict_result={}
        p=0
        q=1
        max_score=0
        for i in range(self.player_num):
            p+=1            
            print('第%d位选手的手牌为：'%p)
            print(player_card[i])
            time.sleep(1)

            dict_result[p]=self.score_making(player_card[i])
            
            print('得分为：%d'%(dict_result[p]))
            time.sleep(1)
            if dict_result[p]>max_score:
                max_score=dict_result[p]
                q=p
        input('敲任意键获得本局结果~')
        print('\n第%d位选手获胜'%q)        