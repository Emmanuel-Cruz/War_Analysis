# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:39:39 2018

@author: Emmanuel Cruz
"""

class Card:
    def __init__(self, color, number, suit):
        self.color = color
        self.suit = suit
        self.number = number
    def get_color(self):
        return self.color
    def get_number(self):
        return self.number
    def get_suit(self):
        return self.suit
    def get_all(self):
        temp = self.number
        letters = ['Jack', 'Queen', 'King', 'Ace']
        if temp > 10:
            temp = letters[self.number-11]
        return self.color, temp, 'of', self.suit
class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name
    def add_hand(self, add):
        self.hand.append(add)
        return self.hand
    def get_hand(self):
        return self.hand   
    def get_hand_length(self):
        return len(self.hand)
    def get_name(self):
        return self.name
    
    def play_card(self):
        try:
            play_card = self.hand[0]
            self.hand.remove(self.hand[0])
            return play_card
        except:
            lost = True
            return lost
    def win(self, won):
        '''
        may have an issue with tie cases***
        '''
        for card in won:
            #print('Getting card...' + str(card.get_all()))
            self.hand.append(card)
        return self.hand
        
    
def deck_generator():
    J, Q, K, A = 11, 12, 13, 14
    numbers = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    suits = ['Clubs', 'Hearts', 'Spades' , 'Diamonds']
    colors = ['black', 'red']
    deck = []
    other = 0
    for card in numbers:
        for suit in suits:
            if other % 2 == 0:
                new_card = Card(colors[0], card, suit)
            else:
                new_card = Card(colors[1], card, suit)
            other += 1
            deck.append(new_card)
#            print(card, suit)
    return deck
    
deck = deck_generator()

import random

'''
seed 8 allows for tie generation
'''
def shuffle(deck):
    shuf_deck = []
    for card in range(52):
        num = random.randrange(0, len(deck))
        shuf_deck.append(deck[num])
        deck.remove(deck[num])
    return shuf_deck

shuf_deck = shuffle(deck)
#
#for card in shuf_deck:
#    print(card.get_number(), card.get_color(), card.get_suit())
#

def deal(players, shuf_deck):
    print('Welcome to War')
    if players <= 1:
        new_players = input("Please input players > 1")
        return deal(new_players, shuf_deck)
    people = []
    pnum = 1
    for player in range(players):
        people.append(Player([], 'Player' + str(pnum)))
        pnum += 1
    cards = 52
    while cards > 0:
#        print("len of shuf_deck = " + str(len(shuf_deck)))
        for player in range(players):
#            print(player, cards)
            try:
                people[player].add_hand(shuf_deck[52-cards])
            except:
                break
            cards -= 1
#    print(people[0].get_hand_length(), people[1].get_hand_length(), people[2].get_hand_length())
    return people
'''
08/20 TODO:::
    Need to implement playing mechanism where players each draw a card
    and the winner (highest card) wins the pot
    Need to add the tie mechansim for when the two players tie, maybe a 
    failsafe for a 3 way tie
    Need to add statistic analysis and data vizualization. 

'''

random.seed()  


def play_war(people):
    '''
    play_war, pt1: cards are dealt equally among players
                   cards are played equally among players
                   player with highest card wins, if tie, 
                   (pt2)
    '''
    def play_tie(tied_players, pot = []):
        '''
        Variables are currently disconnected
        Each tied player plays three cards, 
        then a new trial is played in dict format and the max
        card is returned. If another tie occurs, the 
        function will be called again. 
        '''   
        ######################################################################################
        ######################################################################################
        player_values = {}
        player_lost = False
        print(tied_players)
        for player in tied_players:
            for three in range(3):
                pot.append(player.play_card())
                #print('Appended ', (pot[-1].get_all()))
                if player_lost:
                    tied_players.remove(player)
            try:
                pot.append(player.play_card())
                player_values[pot[-1].get_number()] = player
                #print('Card being played =', pot[-1].get_all())

                
            except:
                if player_lost:
                    tied_players.remove(player)
        #print('Player values == %s'%(player_values))
        winner = player_values[max(player_values)], max(player_values)
        del player_values[max(player_values)]
        checking = player_values
        
        if winner[1] in checking.values():
            print('DOUBLE TIEEEEEEEEEEEEE!!!!!!!!!!')
            tied_players = [winner[0], player_values.keys()[player_values.values().index(max(checking.values()))]]
            return play_tie(tied_players, pot)
        winner[0].win(pot)
        print('winner[0].win(pot) check for hand length winner = ' + str(winner[0].get_hand_length()))
        print('The tied pot is = %s'%(pot))
        print(winner[0])
        return winner[0]
    ######################################################################################
    ######################################################################################
    player_hand_lengths = []
    player_hand_lengths.append([player.get_hand_length() for player in people])
    turn = 1
    playing = True
    while playing:
#        if input('Continue? Y or N') == 'n':
#            playing = False
        print('Round %d' %(turn))
        turn += 1
        cards_played = []
        sum_of_cards = 0
        for person in people:
            try:
                print(person.get_name(), person.get_hand_length())
                sum_of_cards += person.get_hand_length()
                cards_played.append((person, person.play_card()))
            except:
                print('player has run out of cards')
                people.remove(person)
        print('Total Card Amount = %d'%(sum_of_cards))
        winner = 0
        counter = 0
        losing_cards = []
        tied_players = []
        for cards in cards_played:
            try:
                print(cards[1].get_all())
                losing_cards.append(cards[1])
                tied_players.append(cards[0])
            except:
                print('player lost')
                people.remove(person)
                
            if type(cards[1]) == bool:
                print('PLAYER %s LOST'%(cards[0].get_name()))
                people.remove(person)
                break
            if cards[1].get_number() > winner:
                winner = cards[1].get_number()
                winner_card = cards
                tie = False
                tied_players = []
            elif cards[1].get_number() == winner:
                print('Tie!')
                tied_players.append(cards_played[counter-1][0])
                tie = True
                counter += 1
        if tie:
            #print('Tie game excecuted')

            winner = play_tie(tied_players, [])
            winner_card = (winner, winner_card[1])
            #print('Winner of tie game hand length is equal to: %d ' % winner.get_hand_length())
            #print('Losing Cards = ', losing_cards)    
        winner_card[0].win(losing_cards)
        print("The winner is %s with a(n) %s and has hand length of %s" %(winner_card[0].get_name(), winner_card[1].get_all(), winner_card[0].get_hand_length()))
#        print("The loser has a hand length of")
        turn += 1
        if len(people) == 1:
            
            playing = False
    return 'THE WINNER OF THE %d ROUND LONG MATCH IS %s!!' %(turn, people[0].get_name())
    '''
    play_war, pt2: all cards are given to winner
                   in case of tie, 3 cards are put into a 'pot' and
                   the winner of the 4th card is then granted the 'pot'
    '''
        
    
#players = int(input("how many players?"))
players = 24
people = deal(players, shuf_deck)
#print(deal(3, shuf_deck))    
print(play_war(people))
    


'''
08/21 TODO:::
    Need to work on tie mechanism, how to capture 3+ way ties
    Need to work on adding card wins pot mechanism
    Need to work on Statistic Analysis
'''

'''
08/23 TODO:::
    Need to work on tie mechanism...
        1) 3+ way ties
        2) Simple ties
        3) Double tie on tie
    Add Stat Analysis
'''

'''
09/12 TODO:::
    Need to smooth out when a player loses all her/his cards
    Need to consider returning function with less players (cards are retained) when playerX loses
    Need to plot num cards by turn number per player!
    Bug where card amount will increase in games of 3+ people of odd and even numbered variants

'''










































    
    
