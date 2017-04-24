# -*- coding: utf-8 -*-




### ajouter les imports ###

from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from golf1 import GolfeurStragegy


#Gryffondor= SoccerTeam(name="team1",login="etu1")


#def get_golf_team(i):

def get_golf_team(i):
    if i ==1:
        g= SoccerTeam(name="Gryffondor")

        g.add("Harry Potter",GolfeurStrategy())
        return g

    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("",Attaquant1())
        g.add("celine",StrikerStrategy_de_base())
        #g.add("Granger",GoalKeeperStrategy())
        return g
    if i ==4:
        g= SoccerTeam(name="Gryffondor")
        g.add("Potter",passeur())
        g.add("Weasley",passeur())
        g.add("Granger",passeur())
        g.add("Dumbledore",passeur_aller_vers())
        g.add("Potter",StrikerStrategy())
        g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy_de_base())
        g.add("Dumbledore",Attaquant1())
        return g
	####

