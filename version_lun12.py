
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

import tools #pour les constantes

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
         mystate = MyState(state,id_team,id_player)
         act = Action(state,id_team,id_player)
         
         balle_proche =tools.PLAYER_RADIUS + tools.BALL_RADIUS#rayon ball + player
         shoot = 0 #Vector2D(0,0)
          #if id_team==1: 
          #    position_balle = state.ball.position
              
         if balle_proche >= mystate.distance_ball_player():# and state.ball.position != position_balle:
             return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))+ SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),shoot)#+ eviter(adv.) 
          
         if balle_proche <= mystate.distance_ball_player():
             shoot = Vector2D(angle=3.14,norm=55) 
              #on tire vers les buts 
              #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
             return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),shoot) #+eviter()

#         mystate = MyState(state,id_team,id_player)
#        # act.shoot(self)
#         return SoccerAction(mystate.ball_position()-mystate.my_position(),Vector2D(angle=3.14,norm=55))
#         #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 
#          #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))

    
#         return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 
#         #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
    
         #on definit deux Variables de class 
          
                 

class DefenderStrategy(Strategy): #defenseur        
	def __init__(self):
		Strategy.__init__(self,"Defender")
  
	def compute_strategy(self,state,id_team,id_player):

          mystate = MyState(state,id_team,id_player)
          act = Action(state, id_team, id_player)
          pos = Position(state,id_team,id_player)
          #distance avec la balle
          distance = mystate.distance_ball_player()
          
          #distance entre la balle et le but 
          distance_but =mystate.distance_but_ball()
          
          #position_defaut-(state.player_state(id_team,id_player).position),Vector2D(3.14,20)
          #pos.pos_goal()
          if distance_but < 40: 
             return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
           
          if distance < 75:
             if distance < tools.PLAYER_RADIUS + tools.BALL_RADIUS:
                return SoccerAction(mystate.ball_position()-mystate.my_position(),Vector2D(angle=3.14,norm=10)) 
          
#	       #return SoccerAction((state.player_state(id_team,id_player).position)-(state.player_state(self.id_team,self.id_player).position),Vector2D.create_random())

#         if distance <40 :
#                #position_defaut = POS_DEFAUT
#             position_defaut = Vector2D(6,45)
#             if distance < PLAYER_RADIUS + BALL_RADIUS:
#                    return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
##             if id_team == 1: 
##                return SoccerAction(position_defaut-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))+SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 
##            
##             if diastance
##                 return  act.aller_vers_but(self,state,id_team,id_player) +act.aller_vers_balle(self,state,id_team,id_player)
##    

         #if distance_but_ball<15:
            #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 

         
   
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
                return act.aller_vers_but() +SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=1))
                      
        if distance < 40 and distance_but < 20 and distance < PLAYER_RADIUS + BALL_RADIUS:
                return act.aller_vers_but() #+ shoot(self,p)
               # return aller_vers_balle
                #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
           

#    def compute_strategy(self,state,id_team,id_player):
#        mystate = MyState(state,id_team,id_player)
#        pos     = Position(state,id_team,id_player)
#        act     = Action(state,id_team,id_player)
#        
#        distance  = state.ball.position.distance(state.player_state(id_team,id_player).position) #distance avec la balle
#        #distance = mystate.distance_ball_player() #ne fonctionne pas avec 4 joueurs       #distance avec la balle
#        distance_but = state.ball.position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
#        #distance  = mystate.distance_but_ball()      #ne fonctionne pas avec 4 joueurs    
#        distance_but_ball  =mystate.distance_but_ball()
#           
#        act.aller_vers_but()
#        #act.shoot_goal(state,id_team,id_player)
##        (mystate.my_position()).x = 6
##        (mystate.my_position()).y = 45
#        #mystate.my_position() =  pos.position_defaut_goal()
#        
#        if distance_but < 60: #distance avec les cages :
#            #position_defaut = pos.position_defaut()#pos. se_placer_goal(self)
#            if distance < PLAYER_RADIUS + BALL_RADIUS:
#                return SoccerAction((mystate.ball_position()-mystate.my_position()) + distance_but , (Vector2D(angle=3.14,norm=35))+ mystate.my_position())
#  
#        if distance_but_ball < 15:
#            return SoccerAction(mystate.ball_position()-mystate.my_position(),Vector2D(angle=3.14,norm=55)) #+ act.passe(state,id_team,id_player) 
#         
#        act.aller_vers_but()
#        #if distance < 40 and distance_but < 20 and distance < PLAYER_RADIUS + BALL_RADIUS:
#         #       return act.aller_vers_but() #+ shoot(self,p)
#               # return aller_vers_balle
#                #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
#           
#

