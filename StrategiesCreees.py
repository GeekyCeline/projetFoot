
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
#import math
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

  # def compute_strategy(self,state,id_team,id_player):
  #   mystate = MyState(state,id_team,id_player)
  #   act = Action(state,id_team,id_player)
  #   if mystate.est_team1:
  #     if mystate.my_position().y <= GAME_HEIGHT/2:
  #       adj=mystate.my_position().x
  #       opp=(GAME_HEIGHT/2)-mystate.my_position().y
  #       tanAlpha=math.tan(opp/adj)
  #       alpha= math.atan(tanAlpha)

  #     if mystate.my_position().y > GAME_HEIGHT/2:
  #       opp=mystate.my_position().x
  #       adj=(GAME_HEIGHT/2)-mystate.my_position().y
  #       tanTeta=math.tan(opp/adj)
  #       teta=math.atan(tanTeta)
  #       alpha=180-90-teta
  #     return SoccerAction(alpha,50) 



  def compute_strategy(self,state,id_team,id_player):
    mystate = MyState(state,id_team,id_player)
    if mystate.est_team1():
      return SoccerAction((mystate.ball_position()-mystate.my_position()),Vector2D(angle=3.14,norm=55))
    else:
      return SoccerAction((mystate.ball_position()-mystate.my_position()),Vector2D(angle=6.18,norm=55))


#==============================================================================
 
'''
  autre type d'attaquant 
'''
 
class StrikerStrategy(Strategy): #attaquant qui fait une passe 
 	def __init__(self): 
		Strategy.__init__(self,"Striker")

	def compute_strategy(self,state,id_team,id_player):
          mystate = MyState(state,id_team,id_player)
          act = Action(state,id_team,id_player)
          balle_proche = tools.PLAYER_RADIUS + tools.BALL_RADIUS
          if mystate.est_team1(): 
              V =  Vector2D(angle=6.18,norm=10)
          else: 
              V = Vector2D(angle=3.14,norm=1.8)
          
          return SoccerAction(  mystate.en_attente())
 
 #==============================================================================
'''
  les defenseurs 
'''
 
'''1 vs 1'''
 


''' 2 vs 2'''

class DefenderStrategy_de_base(Strategy): #defenseur     
    def __init__(self):
        Strategy.__init__(self,"Defender")   

    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        V = Vector2D(angle=3.14,norm=10)
        return SoccerAction(mystate.ball_position()-mystate.my_position(),V)         
     
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
          if mystate.est_team1(): 
              V =  Vector2D(angle=6.18,norm=10)
              print('but2')
          else:
              print('but1')
              V = Vector2D(angle=3.14,norm=10)  
          if distance >20 : 
              if (mystate.adv()==2) :

                  position = V+Vector2D((0.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
              else: 
                  position = V+Vector2D((3.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
          else: 
              position= state.ball.position-mystate.my_position()
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
        distance = mystate.distance_ball_player()
        distance_but =mystate.distance_but_ball()
        posi= (mystate.ball_position+mystate.but(id_team))
        posi.x= posi.x/2
        posi.y= posi.y/2
        posi= posi-mystate.my_position() 
        posi= pos.se_placer_goal()   
        if distance<= PLAYER_RADIUS-BALL_RADIUS and distance_but < 30:
            #return SoccerAction(mystate.distance_ball_player(),Vector2D(10,40))
            return SoccerAction(mystate.ball_position()-mystate.my_position(),act.passe(state, id_team, id_player))      
#            aller= distance - mystate.my_position()
        #return SoccerAction(posi +pos.se_placer_goal() ,Vector2D(6,(id_team-1.5)*20) +mystate.but(mystate.adv())- mystate.my_position())
        
        return SoccerAction(mystate.ball_position()-mystate.my_position(),Vector2D(angle=3.18,norm=60))