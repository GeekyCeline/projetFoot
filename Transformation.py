# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:37:01 2017

@author: 3407073

Creation de fichier 
"""
from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path

from StrategiesCreees import RandomStrategy,StrikerStrategy_de_base, DefenderStrategy_de_base, GoalKeeperStrategy
from tools import *
from arbres_dec import *

### Transformation d'un etat en features : state,idt,idp -> R^d
def my_get_features(state,idt,idp):
    """ extraction du vecteur de features d'un etat, ici distance a la balle, distance au but, distance balle but """
#    p_pos= state.player_state(idt,idp).position
#    f1 = p_pos.distance(state.ball.position)
#    f2= p_pos.distance( Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
#    f3 = state.ball.position.distance(Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
#    return [f1,f2,f3]
    mystate=MyState(self.state,self.idt,self.idp)
    p_pos= mystate.my_position()
    f1 = mystate.distance_ball_player
    f2 = p_pos.distance( Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
    f3 = state.ball.position.distance(Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
    f4 = mystate.a_la_balle
    return [f1,f2,f3,f4]