
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

'''
#==============================================================================

 attaquants
 
'''
class StrikerStrategy_de_base(Strategy): #attaquant de base
	def __init__(self): 
		Strategy.__init__(self,"Striker")

	def compute_strategy(self,state,id_team,id_player):
         mystate = MyState(state,id_team,id_player)
         act = Action(state,id_team,id_player)
         balle_proche = tools.PLAYER_RADIUS + tools.BALL_RADIUS
         shoot = Vector2D(0,0)
         if mystate.est_team1(): 
             V =  Vector2D(angle=6.18,norm=10)
             print('but2')
         else: 
             print('but1')
             V = Vector2D(angle=3.14,norm=1.8)
             
         return SoccerAction(mystate.ball_position()-mystate.my_position(),V)
         #return SoccerAction(mystate.but(mystate.adv(id_team)) - mystate.my_position(), V)
         #return SoccerAction(mystate.ball_position()-mystate.my_position(),act.tirer_vers_but(state,id_team,id_player))
          #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
#==============================================================================
# 
# '''
#  autre type d'attaquant 
# '''
# 
# class StrikerStrategy(Strategy): #attaquant qui fait une passe 
# 	def __init__(self): 
# 		Strategy.__init__(self,"Striker")
#       def compute_strategy(self,state,id_team,id_player):
#          mystate = MyState(state,id_team,id_player)
# 
# 
# #==============================================================================
# '''
#  les defenseurs 
# '''
# 
# '''1 vs 1'''
# 
# class DefenderStrategy(Strategy,self): #defenseur    
#      self.defenseurstrategy = ComposeStrategy(PlacementDefenseur(), #Degager_la_balle() # + passer_la_sballe()
#      def compute_strategy_utilitaire (self, u) :
#         return self.defenseurstrategy.compute_strategy_utilitaire(u)
#==============================================================================

''' 2 vs 2'''

class DefenderStrategy_de_base(Strategy): #defenseur        
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
#==============================================================================
#           if distance_but < 40:     
#              return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position)  +  mystate.ball_position() -(2*(mystate.ball_position()).x) - mystate.my_position(),Vector2D(angle=3.14,norm=5))
#              
#              #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
#            
#           if distance < 75:
#              if distance < tools.PLAYER_RADIUS + tools.BALL_RADIUS:
#                 return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position)  +  mystate.ball_position() -(2*(mystate.ball_position()).x) - mystate.my_position(),Vector2D(angle=3.14,norm=5))
#==============================================================================
          if mystate.est_team1(): 
              V =  Vector2D(angle=6.18,norm=10)
              print('but2')
          else: 
              
              print('but1')
              V = Vector2D(angle=3.14,norm=10)  
             
          if distance >20 : 
              if (mystate.adv()==2) :
                  position = V+Vector2D((1.3/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
              else: 
                  position = V+Vector2D((3.7/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
          else: 
              position= state.ball.position-mystate.my_position()
              #position = state.ball.position -(state.player_state(id_team,id_player).position)  +  mystate.ball_position() -(2*(mystate.ball_position()).x) - mystate.my_position()
          return SoccerAction(position   ,V-mystate.my_position())
'''
#==============================================================================
         
 le goal 
'''


   
class GoalKeeperStrategy(Strategy): 
    def __init__(self): 
        Strategy.__init__(self,"GoalKeeper")
    
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state,id_team,id_player)
        act = Action(state, id_team, id_player)
        pos = Position(state,id_team, id_player)        
        #distance avec la balle
        distance = mystate.distance_ball_player()
         #est_team1(self,state,id_team,id_player):
        distance_but =mystate.distance_but_ball()
         #return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
#==============================================================================
#         if distance > 5 : 
#             vitesse = state.ball.position + mystate.but(self) - mystate.my_position() 
#             shoot = mystate.but(mystate.adv())- mystate.my_position()
#         else: 
#             vitesse = state.ball.position - mystate.my_position() - mystate.my_position()
#             shoot = mystate.but(mystate.adv())- mystate.my_position()
#         return SoccerAction(vitesse,shoot)
#==============================================================================
       
            
        
        #if distance<= PLAYER_RADIUS-BALL_RADIUS or distance_but < 30:
        
        posi= (state.ball.position+mystate.but(id_team))
        posi.x= posi.x/2
        posi.y= posi.y/2
        posi= posi-mystate.my_position()
#        else: 
#            posi= pos.se_placer_goal()
            
        if distance<= PLAYER_RADIUS-BALL_RADIUS and distance_but < 30:
            #return SoccerAction(mystate.distance_ball_player(),Vector2D(10,40))
            return SoccerAction(mystate.ball_position()-mystate.my_position(),mystate.shoot())

        
#            aller= distance - mystate.my_position()
        return SoccerAction(posi +pos.se_placer_goal() ,Vector2D(6,(id_team-1.5)*20) +mystate.but(mystate.adv())- mystate.my_position())
        #return SoccerAction(posi,Vector2D(6,(id_team-1.5)*20))
        