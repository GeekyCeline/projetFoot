# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:09:56 2017

@author: eleve
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
from tools import MyState,Position,Action
from soccersimulator.settings import *

class Observer(object): 
        MAX_STEP(self,simu)
    def __init__(self, simu): 
        self.simu= simu
        self.simu.listeners+=self #ajout de l'observer
    def begin_match(self,team1,team2,state):
        
        self.last,self.cpt,self.cpt_tot = 0,0,0
    def begin_round(self,team1,team2,state):
        self.simu.state.states[(1,0)].position =
        #ou self.simu.set_state(state)
        self.strat.shoot =
        self.last =self.simu.step
    def update_round(self,team1,team2,state):
        if state.step>self.last+self.MAX_STEP:
            self.simu.end_round()
    def end_round(self, team1,team2,state):
        if state.goal>0:self.cot+=1
        self.cpt_tot+=1
        self.res[...] = self.cpt*1./self.cpt_tot.
        if ...:#fin de la simu 
            self.simu.end_match()