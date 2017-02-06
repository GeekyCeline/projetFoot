# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:59:43 2017

@author: 3407073
"""
from StrategiesCreees import RandomStrategy, StrikerStrategy, DefenderStrategy, GoalKeeperStrategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from __init__ import *
#from __init__ import get_team

#Creation d'une partie
i=input("entrer un 1 ou 2 ou 4: ")
simu = Simulation(get_team(i),get_team(i))
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
#