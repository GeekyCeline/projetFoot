# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:01:06 2017

@author: 3407073
"""

from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from tools import MyState,Position,Action
from soccersimulator.settings import *


## Strategie aleatoire
class RandomStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player): 
		return SoccerAction(Vector2D.create_random(-10,10),Vector2D.create_random())
		
class StrikerStrategy(Strategy): #attaquant 
	def __init__(self): 
		Strategy.__init__(self,"Striker")
	def compute_strategy(self,state,id_team,id_player):
         return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 
          #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))

                 
class DefenderStrategy(Strategy): #defenseur        
	def __init__(self):
		Strategy.__init__(self,"Defender")
  
	def compute_strategy(self,state,id_team,id_player):
         mystate = MyState(state,id_team,id_player)
         act = Action(state,id_team,id_player)
		#return SoccerAction((state.player_state(id_team,id_player).position)-(state.player_state(self.id_team,self.id_player).position),Vector2D.create_random())
         distance =mystate.distance_ball_player(self,state,id_team,id_player) #distance avec la balle
         distance_but =mystate.distance_but_ball(self,state,id_team,id_player)#distance_but 
         if distance <40 :
                #position_defaut = POS_DEFAUT
             if distance < PLAYER_RADIUS + BALL_RADIUS:
                    #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
                 return  act.aller_vers_but(self,state,id_team,id_player) +act.aller_vers_balle(self,state,id_team,id_player)
    
class GoalKeeperStrategy(Strategy): 
    def __init__(self): 
        Strategy.__init__(self,"GoalKeeper")
        
        
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state,id_team,id_player)
        act = Action(state, id_team, id_player)
        #distance avec la balle
        distance = mystate.distance_ball_player()
         #est_team1(self,state,id_team,id_player):
        distance_but =mystate.distance_but_ball()
        if distance < 40 and distance_but < 20:                
                return act.aller_vers_but()
                      
        if distance < 40 and distance_but < 20 and distance < PLAYER_RADIUS + BALL_RADIUS:
                return act.aller_vers_but() #+ shoot(self,p)
               # return aller_vers_balle
                #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
           


