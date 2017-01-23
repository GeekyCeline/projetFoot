# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:01:06 2017

@author: 3407073
"""

from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D

PLAYER_RADIUS= 1.
BALL_RADIUS= 0.65
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

class DefenderStrategy(Strategy): #defenseur        
	def __init__(self):
		Strategy.__init__(self,"Defender")
	def compute_strategy(self,state,id_team,id_player):
		return SoccerAction((state.player_state(id_team,id_player).position)-(state.player_state(id_team,id_player).position),Vector2D.create_random())

class GoalKeeperStrategy(Strategy): 
    def __init__(self): 
        Strategy.__init__(self,"GoalKeeper")
    def compute_strategy(self,state,id_team,id_player):
       # state.player_state(id_team,id_player).positon 
        distance = state.ball.position.distance(state.player_state(id_team,id_player).positon) #distance avec la balle
       # if distance <10:
        position_defaut = Vector2D(6,45)
        if distance == PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
        return SoccerAction(position_defaut-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
      
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

team1.add("John",StrikerStrategy()) #Strategie qui defend
team2.add("Paul",StrikerStrategy())   #Strategie attaque
#team1.add("A",DefenderStrategy())
#team1.add("B",GoalKeeperStrategy())
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
