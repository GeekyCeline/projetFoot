# -*- coding: utf-8 -*-


from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from golf1 import GolfeurStragegy
from __init__ import *


i=input("Appuyez sur 1 pour le mode golf 1 joueur ou sur 2 pour le mode slalom 1 joueur")

if i==1:
	simu = Parcours1(get_golf_team(1),vitesse=GOLF)
	show_simu(simu)

if i==2:
	simu = Parcours3(get_golf_team(2),vitesse=SLALOM)
	show_simu(simu)		



