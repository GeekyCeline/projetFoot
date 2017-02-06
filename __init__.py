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


#team 1

#team1.add("Helmut",StrikerStrategy())
#team1.add("Joe",GoalKeeperStrategy())
#team1.add("John",DefenderStrategy()) 

#team 2

#team2.add("Patrick",GoalKeeperStrategy())
#team2.add("John",StrikerStrategy()) #Strategie qui defend
#team2.add("Paul",DefenderStrategy())   #Strategie attaque

#team2.add("A",GoalKeeperStrategy())

def get_team(i):
    
    if i ==1:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy()) 
        return g

    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy())
        g.add("Weasley",GoalKeeperStrategy())
        return g

    if i ==4:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy())
        g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy())
        g.add("Dumbledore",StrikerStrategy())

def get_team_adv(i):
     
    if i ==1:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy()) 
        return s

    if i ==2:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy())
        s.add("Crabe",GoalKeeperStrategy())
        return g

    if i ==4:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy())
        s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",DefenderStrategy())
        s.add("Voldemort",StrikerStrategy())


