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
POS_DEFAUT = Vector2D(6,45) #goal team 1
POS_DEFAUT2 = Vector2D(145,45)#goal team 2

class MyState(object): #action
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
        #return ball_position(self).distance(position_player(self,state,id_team,id_player))
        #return state.ball.position.distance(state.player_state(id_team,id_player).position)
        
    def distance_but_ball(self):
        if self.est_team1():
            return self.ball_position().distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        return self.ball_position().distance(Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_WIDTH,(GAME_GOAL_HEIGHT/2)))
         #return state.ball.position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
    
    def est_team1(self):
        if self.idt == 1: 
            return True
        return False
        
class Position(object):#emplacements 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
   # def position_but_team1_defaut(): #ne sert a rien
    #    return Vector2D(6,45)
    #def position_but_team2_defaut():#ne sert a rien 
     #   return Vector2D(145,45)
    #def position_player(self,state,id_team,id_player):
     #   return(state.player_state(id_team,id_player).position)
    
    
        
#    def joueur_le_plus_proche(self,state,id_team_id_player): 
#        liste_players = team1.nb_players
#        
#        if est_team1(self,state,id_team_id_player): 
#            distance = 
#            for player in range(1,team1.nb_players): 
#                if distance

class Action(object): 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
        
       
    def aller_vers_balle(self):
        return SoccerAction(MyState.ball_position(self) -( self.my_position(),Vector2D(angle=3.14,norm=55)))
       # return SoccerAction(ball_position(self) -(position_player(self,state,id_team,id_player),Vector2D(angle=3.14,norm=55))
        #
    def aller_vers_but(self):
        essai=MyState(self.state,self.idt,self.idp)
       
        if essai.est_team1():
            return SoccerAction(POS_DEFAUT-(essai.my_position(),Vector2D(3.14,20)))
 
         #   return SoccerAction(POS_DEFAUT-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
       #return  SoccerAction(POS_DEFAUT2-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
          
#    def shoot_goal(self,state,id_team,id_player): 
#        distance =distance_ball_player(self,state,id_team,id_player)
#        if distance < PLAYER_RADIUS + BALL_RADIUS:
#            return shoot(self,)
##    
#    def passe(self,state,id_team,id_player): 
#        distance =distance_ball_player(self,state,id_team,id_player)
#        if distance < PLAYER_RADIUS + BALL_RADIUS:
#            return shoot(self,joueur_le_plus_proche(self,state,id_team_id_player))
