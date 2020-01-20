# -*- coding: utf-8 -*-
"""
Created on Saturday Jan 18 ‏‎2:07:18 2020

@author: Eugene Yong
"""

import Dominion
import testUtility

#Get player names
player_names = testUtility.default_player()

#Get number of victory cards and curse cards
nV, nC = testUtility.get_nCards(player_names)

#Initialize and construct box
box = testUtility.get_boxes(nV)

#Initialize and construct supply order
supply_order = testUtility.get_supply_order()

#Initialize and construct supply from box
supply = testUtility.get_rand_supply(box, nV, nC, nPlayer=len(player_names))

#initialize the trash
trash = []

#Initialize and costruct the Player objects
players = testUtility.get_players(player_names)

#TEST SCENERIO: Replace Treasures in supply with a typo lowercase treasure
del supply["Silver"]
supply["silver"] = [Dominion.Silver()] * 40
del supply["Copper"]
supply["copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
del supply["Gold"]
supply["gold"] = [Dominion.Gold()] * 30


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