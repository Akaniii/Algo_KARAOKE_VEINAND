import random
class Player:

    #initialisation de la classe player
    def __init__(self,pseudo,score0,score1,score2,score3,score4,moyenne,total,meilleurechanson):
        self.__pseudo = pseudo
        self.__score0 = score0
        self.__score1 = score1 
        self.__score2 = score2
        self.__score3 = score3
        self.__score4 = score4
        self.__moyenne = moyenne
        self.__total = total
        self.__meilleurchanson = meilleurechanson

    #getter de la classe player
    def getPseudo(self):
        return self.__pseudo
    def getscore0(self):
        print(self.__score0) 
        return self.__score0
       
    def getscore1(self):
        return self.__score1 
    def getscore2(self):
        return self.__score2 
    def getscore3(self):
        return self.__score3 
    def getscore4(self):
        return self.__score4
    def getmoyenne(self):
        return self.__moyenne
    def gettotal(self):
        return self.__total
    def getmeilleurchason(self):
        return self.__meilleurchanson
    
    
    
    #setter de la classe player
    #la variable currenscore sers a récupéré le score de la chanson que l'on vient de chanter
    def setpseudo(self,pseudo):
        self.__pseudo=input()
        return self.__pseudo
    def setscore0(self,score0,currentscore):
        self.__score0 = currentscore
        return self.__score0
    def setscore1(self,score1,currentscore):
        self.__score1 = currentscore
        return self.__score1
    def setscore2(self,score2,currentscore):
        self.__score2 = currentscore
        return self.__score2
    def setscore3(self,score3,currentscore):
        self.__score3 = currentscore
        return self.__score3
    def setscore4(self,score4,currentscore):
        self.__score4 = currentscore
        return self.__score4
    def setmoyenne(self,score0,score1,score2,score3,score4):
        self.__moyenne = (score0+score1+score2+score3+score4)/5
        return self.__moyenne
    def settotal(self,score0,score1,score2,score3,score4):    
        self.__total = (score0+score1+score2+score3+score4)
    def setmeilleurchanson(self,score0,score1,score2,score3,score4):
        scores=[score0,score1,score2,score3,score4]
        plusgrandscore=0
        test=0
        for i in range(0,len(scores)): 
            test = scores[i]
            if(test>scores[i+1]):
                plusgrandscore=scores[i]
            elif():
                plusgrandscore=scores[i+1]
            
#je passes au test voir si j'ai pas fais n'importe quoi

coco = Player("Coco",0,0,0,0,0,0,0,0)

def chanson0(Player):
    currentscore=random.randint(50,100)
    ancienscore=0
    if(ancienscore<currentscore):
        coco.setscore0=currentscore
        print(currentscore,"  ",ancienscore)
    print (coco.score0)
   
print(chanson0(coco))

test=0
test=coco.getscore0
print(test, "ca marche pas putain")
