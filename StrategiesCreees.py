# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:01:06 2017
@author: 3407073
"""
from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D


from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from tools import MyState,Position,Action,versOu,Qui_a_la_balle
from soccersimulator.settings import *
import tools 
from soccersimulator import settings
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

class Striker1(Strategy): #1 vs 1
      def __init__(self): 
		Strategy.__init__(self,"Striker1")
      def compute_strategy(self,state,id_team,id_player):
         mystate = MyState(state,id_team,id_player)
         act = Action(state,id_team,id_player)
         pos = Position(state,id_team,id_player)
         mystate.pos_attaquant
         if mystate.distance_ball_player< mystate.PR_BR and mystate.my_position<mystate.ball_position.x: 
             return SoccerAction((mystate.ball_position -mystate.my_position),(Vector2D(x=GAME_WIDTH,y=MEDIUM_HEIGHT)).nor_max(5))
         elif mystate.distance_ball_player< mystate.PR_BR and mystate.my_position<mystate.ball_position.x: 
             return SoccerAction(mystate.ball_position-mystate.my_position ,V)# + act.passe_test(state,id_team,id_player)
             #return SoccerAction(mystate.ball_position-mystate.my_position ,V) + act.passe()
         #return act.dribbler(self)
         
class Attaquant1(Strategy): #STRICKER4  et STRICKER1 pour team 1 à 1vs1,2vs2 et 4vs4 mais 4vs 4 pour team 2
    def __init__(self):
        Strategy.__init__(self,"Attaquant1")
    def compute_strategy(self,state,id_team,id_player):
        qui=Qui_a_la_balle(state,id_team,id_player)
        act= Action(state,id_team,id_player)
        #if qui.j_ai_la_balle()==True: 
        p=act.passe_test(state,id_team,id_player)
        return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position ,\
               Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)  
        #return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
         #      Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position,20)         

         
class StrikerStrategy_de_base(Strategy): #STRICKER2 attaquant de base 2 vs 2
	def __init__(self): 
		Strategy.__init__(self,"Striker_de_base")
	def compute_strategy(self,state,id_team,id_player):
         mystate = MyState(state,id_team,id_player)
         act = Action(state,id_team,id_player)
         pos = Position(state,id_team,id_player)
         qui= Qui_a_la_balle(state,id_team,id_player)
         p=act.passe_test(state,id_team,id_player)
         balle_proche = tools.PLAYER_RADIUS + tools.BALL_RADIUS
         shoot = Vector2D(0,0)
         if mystate.est_team1(): 
             V =  Vector2D(angle=6.18,norm=10)
         else:
             V = Vector2D(angle=3.14,norm=1.8)
         #j=pos.position_tout_les_joueurs()
 	 if qui.mon_equipe_a_la_b() and mystate.distance_ball_player > 40 : 
             return mystate.en_attente
         else:
             if qui.j_ai_la_balle :
                 return SoccerAction(mystate.ball_position-mystate.my_position ,V) +p#+act.dribbler()#+ act.passe_test(state,id_team,id_player)

#==============================================================================
 
class StrikerStrategy(Strategy): # STRICKER4 4 vs 4 pour 1 joueur 
    def __init__(self):
        Strategy.__init__(self,"Striker")
    def compute_strategy(self,state,id_team,id_player):
        act = Action(state,id_team,id_player)
        mystate = MyState(state,id_team,id_player)
        qui= Qui_a_la_balle(state,id_team,id_player)
        distance = mystate.distance_ball_player
          #distance entre la balle et le but 
        distance_but =mystate.distance_but_ball
        
        if distance >20 : 
            if (mystate.adv()==2) :
                position = Vector2D((0.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position
            else: 
                position = Vector2D((3.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position
        else: 
            position= state.ball.position-mystate.my_position
            #return SoccerAction(position,V-mystate.my_position)
            if qui.mon_equipe_a_la_b(): 
                return mystate.en_attente
            else:
                return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position) 
     

class passeur(Strategy):
    def __init__(self):
        Strategy.__init__(self,"passeur")
    def compute_strategy(self,state,id_team,id_player):
        act = Action(state,id_team,id_player)
        return  act.passe_test(state,id_team,id_player)
        
class passeur_aller_vers(Strategy):
    def __init__(self):
        Strategy.__init__(self,"passe_aller")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state,id_team,id_player)
        act = Action(state,id_team,id_player)
        p=mystate.ball_position
        return mystate.aller(p) + act.passe_test(state,id_team,id_player)       

class attend(Strategy):
    def __init__(self):
        Strategy.__init__(self,"attend")
    def compute_strategy(self,state,id_team,id_player):
        mystate = MyState(state,id_team,id_player)
        return  mystate.en_attente

'''
  autre type d'attaquant 
'''
# 
#class StrikerStrategy(Strategy): #attaquant qui fait une passe 
# 	def __init__(self): 
#		Strategy.__init__(self,"Striker")
#	def compute_strategy(self,state,id_team,id_player):
#          mystate = MyState(state,id_team,id_player)
#          act = Action(state,id_team,id_player)
#          balle_proche = tools.PLAYER_RADIUS + tools.BALL_RADIUS
#          if mystate.est_team1(): 
#              V =  Vector2D(angle=6.18,norm=10)
#          else: 
#              V = Vector2D(angle=3.14,norm=1.8)
#          
#          return SoccerAction(  mystate.en_attente())
# 
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
        return SoccerAction(mystate.ball_position-mystate.my_position,V)         

#pour 4 vs 4   si il y a un goal

class DefenderStrategy(Strategy): #defenseur        
	def __init__(self):
		Strategy.__init__(self,"Defender")
	def compute_strategy(self,state,id_team,id_player):
          mystate = MyState(state,id_team,id_player)
          act = Action(state, id_team, id_player)
          pos = Position(state,id_team,id_player)
          angle = versOu(state,id_team,id_player)
          #distance avec la balle
          distance = mystate.distance_ball_player
          #distance entre la balle et le but 
          distance_but =mystate.distance_but_ball
          V = angle.vers_les_but_adv 
          if distance >20 : 
              if (mystate.adv()==2) :
                  position = V+Vector2D((0.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position
              else: 
                  position = V+Vector2D((3.5/5)*GAME_WIDTH,state.ball.position.y)-mystate.my_position
          else: 
              position= state.ball.position-mystate.my_position
          return SoccerAction(position,V-mystate.my_position)
'''
#==============================================================================
         
 le goal 
'''
   
class GoalKeeperStrategy(Strategy):
        def __init__(self,name="ma strategie"):
            Strategy.__init__(self,"Goal")
        def compute_strategy(self,state,id_team,id_player):
                p = state.player_state(id_team, id_player)
                mystate = MyState(state,id_team,id_player)
                if state.ball.position.x<20 and mystate.est_team1():
                        return SoccerAction(state.ball.position - p.position, Vector2D(GAME_WIDTH-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if state.ball.position.x>110 and not mystate.est_team1():
                        return SoccerAction(state.ball.position - p.position, Vector2D(0-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if not mystate.est_team1():
                        p.position=Vector2D(0,GAME_HEIGHT/2)
                        p = state.player_state(id_team, id_player)
                        if((p.position.x>5) and (p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT) or (p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
                                p.position = Vector2D(0,GAME_HEIGHT/2)
                                return p.position
                if mystate.est_team1():
                        p.position=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
                        p = state.player_state(id_team, id_player)
                        if((p.position.x<30)and(p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT)or(p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
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
        distance = mystate.distance_ball_player
        distance_but =mystate.distance_but_ball()
        posi= (state.ball.position+mystate.but(id_team))
        posi.x= posi.x/2
        posi.y= posi.y/2
        posi= posi-mystate.my_position
        posi= pos.se_placer_goal()   
        if distance<= PLAYER_RADIUS-BALL_RADIUS and distance_but < 30:
            #return SoccerAction(mystate.distance_ball_player(),Vector2D(10,40))
            return SoccerAction(mystate.ball_position-mystate.my_position,mystate.shoot())#+ act.passe(state, id_team, id_player)    
#            aller= distance - mystate.my_position()
        #return SoccerAction(posi +pos.se_placer_goal() ,Vector2D(6,(id_team-1.5)*20) +mystate.but(mystate.adv())- mystate.my_position())
        
        return SoccerAction(act.passe(state,id_team,id_player))
'''
