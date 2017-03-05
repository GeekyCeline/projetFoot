# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:40 2017

@author: 3407073
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from StrategiesCreees import RandomStrategy, StrikerStrategy_de_base, DefenderStrategy_de_base, GoalKeeperStrategy,DefenderStrategy

#import simple_exemple_commun
#ou from teams import team1, team2
## Creation d'une equipe

serpentar= SoccerTeam(name="team1",login="etu1")
gryfondor= SoccerTeam(name="team2",login="etu2")


def get_team(i):
    if i ==1:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy_de_base())#+DefenderStrategy()) 
        return g
    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("Weasley",DefenderStrategy())
        g.add("Granger",StrikerStrategy_de_base())
        return g
    if i ==4:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",StrikerStrategy_de_base())
        g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy_de_base())
        g.add("Dumbledore",StrikerStrategy_de_base())
        return g

def get_team_adv(i):
    if i ==1:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy_de_base()) 
        return s
    if i ==2:
        s= SoccerTeam(name="Serpentard")
        s.add("Crabe",DefenderStrategy())
        s.add("Goyle",StrikerStrategy_de_base())
        return s
    if i ==4:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy_de_base())
        s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",DefenderStrategy_de_base())
        s.add("Voldemort",StrikerStrategy_de_base())
        return s


