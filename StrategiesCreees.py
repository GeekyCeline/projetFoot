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
import tools 

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
        # act.shoot(self)
         balle_proche = tools.PLAYER_RADIUS + tools.BALL_RADIUS
         shoot = Vector2D(0,0)
         if mystate.est_team1(): 
             V =  Vector2D(angle=6.18,norm=10)
         else:
             V = Vector2D(angle=3.14,norm=1.8)
         return SoccerAction(mystate.ball_position()-mystate.my_position() ,V)

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

class DefenderStrategy_de_base(Strategy): #defenseur     
    def __init__(self):
        Strategy.__init__(self,"Defender")   
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        V = Vector2D(angle=3.14,norm=10)
        return SoccerAction(mystate.ball_position()-mystate.my_position(),V)         
#pour 4 vs 4   si il y a un goal
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
          else:
              V = Vector2D(angle=3.14,norm=10)  
          if distance >20 : 
              if (mystate.adv()==2) :
                  position = V+Vector2D((0.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
              else: 
                  position = V+Vector2D((3.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position()
          else: 
              position= state.ball.position-mystate.my_position()
          return SoccerAction(position,V-mystate.my_position())
'''
#==============================================================================
         
 le goal 
'''
'''       
class GoalKeeperStrategy(Strategy):
        def __init__(self,name="ma strategie"):
            Strategy.__init__(self,"Goal")
        def compute_strategy(self,state,idteam,idplayer):
                p = state.player_state(idteam, idplayer)
               
                if state.ball.position.x<40:
                        return SoccerAction(state.ball.position - p.position, Vector2D(GAME_WIDTH-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if state.ball.position.x>110:
                        return SoccerAction(state.ball.position - p.position, Vector2D(0-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if idteam==2:
                        p.position=Vector2D(0,GAME_HEIGHT/2)
                        p = state.player_state(idteam, idplayer)
                        if((p.position.x>5) and (p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT) or (p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
                                p.position = Vector2D(0,GAME_HEIGHT/2)
                                return p.position
                if idteam==1:
                        p.position=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
                        p = state.player_state(idteam, idplayer)
                        if((p.position.x<95)and(p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT)or(p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
                                p.position = Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
                                return p.position
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
        posi= (state.ball.position+mystate.but(id_team))
        posi.x= posi.x/2
        posi.y= posi.y/2
        posi= posi-mystate.my_position() 
        posi= pos.se_placer_goal()   
        if distance<= PLAYER_RADIUS-BALL_RADIUS and distance_but < 30:
            #return SoccerAction(mystate.distance_ball_player(),Vector2D(10,40))
            return SoccerAction(mystate.ball_position()-mystate.my_position(),mystate.shoot())#+ act.passe(state, id_team, id_player)    
#            aller= distance - mystate.my_position()
        #return SoccerAction(posi +pos.se_placer_goal() ,Vector2D(6,(id_team-1.5)*20) +mystate.but(mystate.adv())- mystate.my_position())
        
        return SoccerAction(act.passe(state,id_team,id_player))
