# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:07:10 2017
@author: Soumahoro Kady
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:57:26 2017
@author: 3407073
"""

from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction,SoccerState
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
#from LancerSimu import i
#from __init__ import get_team, get_team_adv

#import weakref

PLAYER_RADIUS= 1.
BALL_RADIUS= 0.65
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 #


#mes variables globales

POS_DEFAUT = Vector2D(20,45)     #goal team 1

POS_DEFAUT2 = Vector2D(GAME_WIDTH+45,GAME_WIDTH/2)  #goal team 2



# parametres utilisés


'''      
###########################################################
#LA BASE = outils 
############################################################ 
'''  

class MyState(object):          
    def __init__(self,state,id_team,id_player): #__init__ appelée automatiquement après la création de l'objet, pour creer l'état de départ= initilisation
        self.state = state
        self.idt= id_team
        self.idp = id_player
    
     
    @property #transforme la methode en proprièté, methode est considèré dcomme un attribut = utiliser les methode sans parenthèses 
    def my_position(self):
        """retourne la position du joueur""" #specification
        return (self.state.player_state(self.idt,self.idp)).position
        
    @property
    def ball_position(self):
        """retourne la position de la balle"""
        return self.state.ball.position
        
    #pour aller vers un point donné
    def aller(self,p): 
        return SoccerAction(p-self.my_position,Vector2D())
    
    #pour shooter vers qqun ou qq chose 
    def shoot(self,p): 
        return SoccerAction(Vector2D(),p-self.my_position,Vector2D())
      
    @property
    def distance_ball_player(self):
        """retourne distance entre le joueur et la balle"""
        return self.ball_position.distance(self.my_position)
  
    @property
    def distance_but_ball(self):
        """retourne la distance entre la balle et les cages/buts"""
        if self.est_team1():
            return self.ball_position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        else: 
            return self.ball_position.distance(Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_WIDTH,(GAME_GOAL_HEIGHT/2)))

    
    @property
    def but(self,id_team): 
        """retourne la position des cages/buts  d'un joueur (self.cage)"""
        if self.est_team1():
            return (Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        else:
            return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_WIDTH,(GAME_GOAL_HEIGHT/2)))
      
    
    #@property
    def est_team1(self):
        """retourne True si le joueur/self est dans l'équipe 1 sino False """
        if self.idt == 1: 
            return True
        return False
    
    
    #@property
    def adv(self):
        """retourne id_team de l'équipe adverse (ne sert pas vraiment vu qu'il y a est_team1)"""
        if self.idt == 1: 
            return 2
        return 1
    
    #le joueur reste à sa place, et ne fait rien
    @property
    def en_attente(self):
        return SoccerAction()
    
    @property
    def PR_BR(self): 
        return PLAYER_RADIUS+BALL_RADIUS

    @property 
    def pos_attaquant(self): 
        return  SoccerAction(Vector2D(10,GAME_WIDTH-60) -(self.state.player_state(self.idt,self.idp)).position)
'''       
###########################################################
#NOUVELLE CLASSE = versOu
############################################################ 
'''  
class versOu(object): 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
    
    @property
    def vers_les_but_adv(self):
        """retourne """
        mystate= MyState(self.state,self.idt,self.idp)
        if mystate.est_team1(): 
              V =  Vector2D(angle=6.18,norm=10)
        else:
              V = Vector2D(angle=3.14,norm=10) 
        return V

'''       
###########################################################
#NOUVELLE CLASSE = Qui à la balle
############################################################ 
'''  
class Qui_a_la_balle(object): 
    def __init__(self,state,id_team,id_player): 
        self.state= state
        self.idt= id_team
        self.idp = id_player
        
    @property
    def j_ai_la_balle(self): 
        mystate= MyState(self.state,self.idt,self.idp)
        if mystate.distance_ball_player > mystate.PR_BR:
            return False
        return True
    
    def mon_equipe_a_la_b(self): 
        mystate= MyState(self.state,self.idt,self.idp)
        pos=Position(self.state,self.idt,self.idp)
        liste= pos.position_tout_les_joueurs()
        for i in liste: 
            if i<mystate.PR_BR:
                return True
            else: 
                return False
        
'''    
###########################################################
#NOUVELLE CLASSE = POSITION
############################################################ 
'''              
class Position(object):#emplacements 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
    
    def se_placer_goal(self): 
        """retourne la position des goals par défaut"""
        mystate = MyState(self.state,self.idt,self.idp)
        if  mystate.est_team1():
            return POS_DEFAUT-mystate.my_position
        else: 
            return POS_DEFAUT2-mystate.my_position
     

    def position_tout_les_joueurs(self): 
        #mystate = MyState(self.state,self.idt,self.idp)
        #liste_cle = SoccerState.players.WeakKeyDictionary()#retourne la liste des cles de joueurs
        """retourne la position des joueurs """
        liste_joueur= []
        if self.idt == 1:
            #            while i>0:
#                pos = self.state.player_state(1, i).position
#                liste_joueur.append(pos)
#                print(liste_joueur)
#                i=i-1
#        else: 
#            while i>0:
#                pos = self.state.player_state(2, i).position
#                liste_joueur.append(pos)
#                print(liste_joueur)
#                i=i-1
            if self.state.nb_players(1) == 1:
                liste_joueur.append(self.state.player_state(1, 0).position)
            elif self.state.nb_players(1) == 2:
                for i in range(2):
                    pos = self.state.player_state(1, i).position
                    liste_joueur.append(pos)
            elif self.state.nb_players(1) == 4:
                for i in range(4):
                    pos = self.state.player_state(1, i).position
                    liste_joueur.append(pos)
                    
        elif self.idt == 2:
            if self.state.nb_players(2) == 1:
                liste_joueur.append(self.state.player_state(2, 0).position)
            elif self.state.nb_players(2) == 2:
                for i in range(2):
                    pos = self.state.player_state(2, i).position
                    liste_joueur.append(pos)
            elif self.state.nb_players(2) == 4:
                for i in range(4):
                    pos = self.state.player_state(2, i).position
                    liste_joueur.append(pos)
        #print(liste_joueur)            
        #Retourne une liste de toutes les positions de mes joueurs, quelque soit la team ou le nombre de joueurs.
        return liste_joueur

#==============================================================================

    def joueur_le_plus_proche(self,rang=1):#state,id_team,id_player): 
        """retourne la position du joueur(de mon equipe) le plus proche """
    
        mystate = MyState(self.state,self.idt,self.idp)  
        distances = {}
        liste = []
        monrg = self.position_tout_les_joueurs
        for i in monrg():
            if i != mystate.my_position:#sauf moi
                d = mystate.my_position.distance(i)
                distances[round(d,2)] = i # round arrondir a 2 chiffres apres la virgule,ici
        for i in distances.keys():
            liste.append(i)
        sorted(liste)
        #print(liste)        
        pos = distances.get(liste[0])#liste[rang-1])#clé
        return pos#Retourne la position
       
       
#        if liste_players!= []: 
#            distance = mystate.my_position - mystate.my_position(liste_players[0])
#            plus_proche = liste_players[0]
#        
#        #liste_players = get_team(2).nb_player
#         
#            for player in liste_players : #range(1,liste_players): 
#                distance_deuxieme = mystate.my_position- mystate.my_position(liste_players[player])
#     
#                if distance<distance_deuxieme: 
#                    plus_proche = liste_players[player]
#            return plus_proche
         
#==============================================================================

'''        
###########################################################
#NOUVELLE CLASSE = ACTION 
############################################################ 
'''
class Action(object): 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
       
    
    def aller_vers_balle(self):
        mystate = MyState(self.state,self.idt,self.idp)
        return SoccerAction(mystate.distance_ball_player,Vector2D(angle=3.14,norm=55))
    
    #je vais vers la balle si je n'ai pas la balle et si personne n'a la balle dans mon equipe
    def aller_vers_balle_condition(self):
        mystate = MyState(self.state,self.idt,self.idp)
        #if( mystate.est_team1(self)):
        liste_players = self.idt.nb_players #team1.nb_players
        #else: 
         #   liste_players = team2.nb_players
        distance_self = mystate.distance_ball_player
        for player in liste_players: 
            distance = mystate.ball_position - mystate.my_position(liste_players[player])
            if distance<= mystate.PR_BR: 
                return SoccerAction(mystate.en_attente)
        return SoccerAction(mystate.distance_ball_player,Vector2D(angle=3.14,norm=55))       
        
    def aller_vers_but(self):
        essai=MyState(self.state,self.idt,self.idp)
        if essai.est_team1():
            return SoccerAction(POS_DEFAUT-essai.my_position,Vector2D(3.14,20))
        return SoccerAction(POS_DEFAUT2-essai.my_position,Vector2D(6.18,20))

#    def passe1(self,state,id_team,id_player): 
#        mystate = MyState(self.state,self.idt,self.idp)
#        posi  = Position(self.state,self.idt,self.idp)
#        distance = mystate.distance_ball_player
#        if distance <= mystate.PR_BR:
#            print("ici")
#            if posi.joueur_le_plus_proche(): 
#               #return shoot(self,Position.joueur_le_plus_proche(self,state,id_team_id_player))
#                shoot = mystate.but(mystate.adv())-mystate.my_position
#                shoot.x =shoot.x - (GAME_GOAL_HEIGHT /2.4)
#                shoot.y =shoot.y - (GAME_GOAL_HEIGHT /2.4)
#                print("ici2")
#            return SoccerAction(posi.joueur_le_plus_proche(1)-mystate.my_position(),shoot(self))
#    
    def passe_test(self,state,id_team,id_player): 
        posi  = Position(self.state,self.idt,self.idp)
        mystate = MyState(self.state,self.idt,self.idp)
        proche= posi.joueur_le_plus_proche(self)
        
        if Qui_a_la_balle.j_ai_la_balle == True: 
            return SoccerAction(proche-mystate.ball_position,Vector2D(angle= 10))
        else:
            return SoccerAction()#SoccerAction(mystate.distance_ball_player)
        


    def passe1(self,state,id_team,id_player): 
        mystate = MyState(self.state,self.idt,self.idp)
        posi  = Position(self.state,self.idt,self.idp)
        distance = mystate.distance_ball_player
        if distance <= mystate.PR_BR:
            print("ici")
            if posi.joueur_le_plus_proche(id_player,self): 
               #return shoot(self,Position.joueur_le_plus_proche(self,state,id_team_id_player))
                shoot = mystate.but(mystate.adv())-mystate.my_position
                shoot.x =shoot.x - (GAME_GOAL_HEIGHT /2.4)
                shoot.y =shoot.y - (GAME_GOAL_HEIGHT /2.4)
                print("ici2")
            return SoccerAction(posi.joueur_le_plus_proche(id_player,self)-mystate.my_position(),shoot(self))
    
    def passe_test(self,state,id_team,id_player): 
        posi  = Position(self.state,self.idt,self.idp)
        mystate = MyState(self.state,self.idt,self.idp)
        proche= posi.joueur_le_plus_proche(self)
        
        if proche != mystate.my_position and Qui_a_la_balle.j_ai_la_balle: 
            return SoccerAction(proche-mystate.ball_position, 10)
        
#    def passe(self):
#        mystate = MyState(self.state,self.idt,self.idp)
#        posi  = Position(self.state,self.idt,self.idp)
#        print("ici")
#        if mystate.distance_ball_player < mystate.PR_BR : 
#            #return SoccerAction( Vector2D(), (posi.joueur_le_plus_proche(1)- mystate.ball_position ).norm_max(5))
#            
#            return SoccerAction(Vector2D(), (posi.joueur_le_plus_proche(self)- mystate.ball_position ).norm_max(5))
#        print("la")
#        return SoccerAction(mystate.ball_position - mystate.my_position)

    def shoot(self,state,id_team,id_player):
        mystate = MyState(self.state,self.idt,self.idp)
        sh = Vector2D(0,0)
        if mystate.distance_ball_player() < PLAYER_RADIUS + BALL_RADIUS:
            if mystate.distance_but_ball() < 40: 
                sh = Vector2D(10,10)
            if mystate.distance_but_ball() > 40:# and personne(): 
                sh = Vector2D(20)
        return sh


    def dribbler(self): 
        pos=Position(self.state,self.idt,self.idp)
        mystate = MyState(self.state,self.idt,self.idp)
        liste_adversaire=[]
        for i in pos.position_tout_les_joueurs(): 
            if self.idt == mystate.adv(): 
                liste_adversaire.append(i)
        for j in range(0,len(liste_adversaire)): 
            if (pos.joueur_le_plus_proche(1).x == liste_adversaire[j].x) and (pos.joueur_le_plus_proche(1).y == liste_adversaire[j].y):
                SoccerAction(((liste_adversaire[j])+Vector2D(10,0))- mystate.myposition,Vector2D(angle=0,norm=10))
            

#    def dribbler(self): 
#        liste=[]
#        for i in position_tout_les_joueurs(): 
#            if self.idt== mystate.adv(self): 
#                liste.append(i)
#        if 

