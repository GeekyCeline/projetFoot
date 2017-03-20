# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:59:43 2017

@author: 3407073
"""
from StrategiesCreees import RandomStrategy,StrikerStrategy_de_base, DefenderStrategy_de_base, GoalKeeperStrategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from __init__ import *
#Creation d'une partie
import logging
from arbres_dec import * 
logging.basicConfig(level=logging.DEBUG)


i=input("Cliquez sur 1 pour un match en 1 vs 1, sur 2 pour un match en 2 vs 2 et sur 4 pour un match ")
simu = Simulation(get_team(i),get_team_adv(i))

#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()

# recuperation de tous les etats
#training_states = strat_j1.states
    # sauvegarde dans un fichier
#dump_jsonz(training_states,fn)

#def entrainement(fn):
#    simu = Simulation(team1,team2)
#    show_simu(simu)
#    # recuperation de tous les etats
#    training_states = strat_j1.states
#    # sauvegarde dans un fichier
#    dump_jsonz(training_states,fn)