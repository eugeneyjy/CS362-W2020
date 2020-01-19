# -*- coding: utf-8 -*-
"""
Created on Saturday Jan 18 2:06:16 2020

@author: Eugene Yong
"""

import Dominion
import testUtility

#Get player names
player_names = testUtility.default_player()

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Initialize box
box = testUtility.get_boxes(nV)

#Initialize supply order
supply_order = testUtility.get_supply_order()

#Initialize supply from box
supply = testUtility.get_rand_supply(box, nV, nC, nPlayer=len(player_names))

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.get_players(player_names)

#TEST SCENARIO: change the initialization of Province to Duchy in supply
supply["Province"] = [Dominion.Duchy()] * nV

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)