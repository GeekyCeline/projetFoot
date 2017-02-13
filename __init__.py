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

serpentar= SoccerTeam(name="team1",login="etu1")
gryfondor= SoccerTeam(name="team2",login="etu2")



#def get_team2(i): 
#   # s = SoccerSimulator("") 
#    conoha= SoccerTeam(name="conoha",login="etu1")
#    if i== 1: 
#        conoha.add("I", StrikerStrategy())
#        return serpentar
#    if i ==4: 
#        conoha.add("Itachi",StrikerStrategy())
#        conoha.add("Orochimaru",GoalKeeperStrategy())
#        conoha.add("Hel",StrikerStrategy())
#        conoha.add("azaikcez",StrikerStrategy())
#        return conoha
#    if i == 2: 
#        conoha.add("Joe",GoalKeeperStrategy())
#        conoha.add("Pecvze",StrikerStrategy())
#        
#        return conoha

def get_team(i):
    
    if i ==1:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy())#+DefenderStrategy()) 
        return g

    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy())
        #g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy())#+GoalKeeperStrategy())
        return g

    if i ==4:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy())
        g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy())
        g.add("Dumbledore",StrikerStrategy())
        return g

def get_team_adv(i):
     
    if i ==1:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy()) 
        return s

    if i ==2:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy())
        #s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",DefenderStrategy())
        return s

    if i ==4:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy())
        s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",DefenderStrategy())
        s.add("Voldemort",StrikerStrategy())
        return s


