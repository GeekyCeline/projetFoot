# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:40 2017

@author: 3407073
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from StrategiesCreees import RandomStrategy, StrikerStrategy, DefenderStrategy, GoalKeeperStrategy

#import simple_exemple_commun
#ou from teams import team1, team2
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

#team 1

team1.add("Helmut",StrikerStrategy())
#team1.add("Joe",GoalKeeperStrategy())
#team1.add("John",DefenderStrategy()) 

#team 2

team2.add("Patrick",GoalKeeperStrategy())
team2.add("John",StrikerStrategy()) #Strategie qui defend
#team2.add("Paul",DefenderStrategy())   #Strategie attaque

#team2.add("A",GoalKeeperStrategy())