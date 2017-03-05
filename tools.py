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
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D

#from __init__ import get_team, get_team_adv



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

POS_DEFAUT = Vector2D(10,45)     #goal team 1

POS_DEFAUT2 = Vector2D(150,120)  #goal team 2



# parametres utilisés


'''      
###########################################################

#LA BASE

############################################################ 
'''  

class MyState(object):          #action
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
        
    def my_position(self): 
        return (self.state.player_state(self.idt,self.idp)).position
        
    def ball_position(self): 
        return self.state.ball.position
        
    def aller(self,p): 
        return SoccerAction(p-self.my_position(),Vector2D())
        
    def shoot(self,p): 
        return SoccerAction(Vector2D(),p-self.position(),Vector2D())
      
    def distance_ball_player(self):
        return self.ball_position().distance(self.my_position())
  
    def distance_but_ball(self): #retourne la distance entre les buts et la balle
        #return ball_position(self).distance(position_player(self,state,id_team,id_player))
        #return state.ball.position.distance(state.player_state(id_team,id_player).position)

        if self.est_team1():
            return self.ball_position().distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        else: 
            return self.ball_position().distance(Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_WIDTH,(GAME_GOAL_HEIGHT/2)))
       
    def but(self,id_team): #retourne la position de self.cage

         #return state.ball.position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        if self.est_team1():
            return (Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        else:
            return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_WIDTH,(GAME_GOAL_HEIGHT/2)))
        
    
    def est_team1(self): #retourne vrai si self est dans la team1 sinon faux
        if self.idt == 1: 
            return True
        return False


    def adv(self): #retourne id de l'adversaire
        if self.idt == 1: 
            return 2
        return 1
 
    def en_attente(self):
        return SoccerAction( Vector2D(0,0), Vector2D(0,0))
 
 
class versOu(object): 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
    def vers_les_but_adv(self):
        return
        
'''      
=======
    def adv(self): 
        if self.idt == 1: 
            return 2
        return 1
        
###########################################################

#NOUVELLE CLASSE = POSITION

############################################################ 

'''      

        
class Position(object):#emplacements 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
    

    def se_placer_goal(self): #retourne la position des goals par défaut 
        mystate = MyState(self.state,self.idt,self.idp)
        if  mystate.est_team1():
            return POS_DEFAUT-mystate.my_position()
        else: 
            return POS_DEFAUT2-mystate.my_position()
                  
        #mofifier vendredi 10 fev
#==============================================================================
    def joueur_le_plus_proche(self,state,id_team_id_player): 
        mystate = MyState(self.state,self.idt,self.idp)   
 #        if  MyState.est_team1(self,state,id_team_id_player): 
 #            liste_players = team1.nb_players
 #        else: 
 #            liste_players = team2.nb_players 
        liste_players = self.idt.nb_player
        distance = mystate.my_position(self) - mystate.my_position(liste_players[0])
        plus_proche = liste_players[0]
        
        liste_players = get_team(2).nb_player
         
        for player in liste_players: 
            distance_deuxieme = mystate.my_position(self)- mystate.my_position(liste_players[player])
        distance = mystate.my_position(self) - mystate.my_position(liste_players[0])
        plus_proche = liste_players[0]
        
        for player in range(1,liste_players): 
            distance_deuxieme = MyState.my_position(self)- MyState.my_position(liste_players[player])
 
            if distance<distance_deuxieme: 
                plus_proche = liste_players[player]
        return plus_proche
         
#==============================================================================


    def pos_goal(self):
        mystate = MyState(self.state,self.idt,self.idp)
        if mystate.est_team1(self): 
            return POS_DEFAUT-(self.state.player_state(self.idt,self.idp).position),Vector2D(3.14,20)
        return POS_DEFAUT2 -(self.state.player_state(self.idt,self.idp).position),Vector2D(6.18,20)
'''       
=======
#    def position_defaut_goal(self): 
#        if  MyState.est_team1(self): 
#             return POS_DEFAUT#position_defaut = Vector2D(6,45) #dans le tools 
#        return POS_DEFAUT2 #position_defaut2 = Vector2D(145,45) #dans le tools

    def pos_goal(self): 
        if MyState.est_team1(self): 
            return POS_DEFAUT-(self.state.player_state(self.idt,self.idp).position),Vector2D(3.14,20)
        return POS_DEFAUT2 -(self.state.player_state(self.idt,self.idp).position),Vector2D(6.18,20)
        
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
        return SoccerAction(mystate.ball_position(self) -( self.my_position(),Vector2D(angle=3.14,norm=55)))
      
    def aller_vers_balle_condition(self):
        mystate = MyState(self.state,self.idt,self.idp)
        if( mystate.est_team1(self)):
            liste_players = self.idt.nb_players #team1.nb_players
        else: 
            liste_players = team2.nb_players
            
        distance_self =mystate.distance_ball_player()
        for player in liste_players: 
            distance = mystate.ball_position(self) -  mystate.my_position(liste_players[player])

        return SoccerAction(MyState.ball_position(self) -( self.my_position(),Vector2D(angle=3.14,norm=55)))       
        
    def aller_vers_but(self):
        essai=MyState(self.state,self.idt,self.idp)
        if essai.est_team1():
            return SoccerAction(POS_DEFAUT-essai.my_position(),Vector2D(3.14,20))
        return SoccerAction(POS_DEFAUT2-essai.my_position(),Vector2D(6.18,20))

    def passe(self,state,id_team,id_player): 
        mystate = MyState(self.state,self.idt,self.idp)
        posi  = Position(self.state,self.idt,self.idp)
        distance = mystate.distance_ball_player()
        if distance <= PLAYER_RADIUS + BALL_RADIUS:
            if posi.joueur_le_plus_proche(id_player,self): 
               #return shoot(self,Position.joueur_le_plus_proche(self,state,id_team_id_player))
                shoot = mystate.but(mystate.adv())-mystate.my_position()
                shoot.x =shoot.x - (GAME_GOAL_HEIGHT /2.4)
                shoot.y =shoot.y - (GAME_GOAL_HEIGHT /2.4)
            return SoccerAction(posi.joueur_le_plus_proche(id_player,self)-mystate.my_position(),shoot(self))
        
    def shoot(self,state,id_team,id_player):
        mystate = MyState(self.state,self.idt,self.idp)
        sh = Vector2D(0,0)
        if mystate.distance_ball_player() < PLAYER_RADIUS + BALL_RADIUS:
            if mystate.distance_but_ball() < 40: 
                sh = Vector2D(10,10)
            if mystate.distance_but_ball() > 40:# and personne(): 
                sh = Vector2D(20)
        return sh
