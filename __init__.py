# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:40 2017

@author: 3407073
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from StrategiesCreees import RandomStrategy,Striker2,passeur_aller_vers,Striker1,Striker4,GoalKeeperStrategy,DefenderStrategy

#import simple_exemple_commun
#ou from teams import team1, team2
## Creation d'une equipe

serpentar= SoccerTeam(name="team1",login="etu1")
gryfondor= SoccerTeam(name="team2",login="etu2")


def get_team(i):
    if i ==1:
        g= SoccerTeam(name="Gryffondor")
        g.add("Saitama",Striker1())

        return g
    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("Ken Kanegi",GoalKeeperStrategy())
        g.add("Light Yagami",Striker2())
        return g
    if i ==4:
        g= SoccerTeam(name="Gryffondor")
        g.add("Oroshimaru",Striker2())
        g.add("Itachi",GoalKeeperStrategy())
        g.add("Potter",Striker1())
        g.add("Kurosaki Ichigo",DefenderStrategy())
        return g

def get_team_adv(i):
    if i ==1:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",Striker1()) 
        return s
    if i ==2:
        s= SoccerTeam(name="Serpentard")
        s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",Striker2())
        return s
    if i ==4:
        s= SoccerTeam(name="Serpentard")
        s.add("Potter",Striker2())#GoalKeeperStrategy())
        s.add("Crabe",GoalKeeperStrategy())
        s.add("Goyle",Striker1())
        s.add("Voldemort",DefenderStrategy())
        return s


