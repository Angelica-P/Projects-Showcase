# Student added code by Angelica Paynter
# DocStrings and Assigment by Vida Dujmovic
# Assignment 3 Game

import random

# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    deck = []
    for i in range(1,num+1):
        for suit in [100,200,300,400]:
            deck.append(suit+i)
    return deck

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    random.shuffle(deck)
    return

def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''
     player_deck = []
     for i in range(7):
         player_deck.append(deck.pop())
     return player_deck


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    if len(deck) < num:
        for i in range(len(deck)):
            player.append(deck.pop())
    else:
        for i in range(num):
            player.append(deck.pop())
    return 


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    one_way = hand[:]
    one_way.sort()
    print()
    for i in range(len(one_way)):
        print(one_way[i], end=" ")
    other_way = []
    i = 1
    while len(one_way) != len(other_way):
        for k in range(len(one_way)):
            if one_way[k]%100 == i:
                other_way.append(one_way[k])
                one_way[k]= 0
        i += 1
    print("\n")
    for i in range(len(other_way)):
        print(other_way[i], end=" ")
    print()
    return
            
    
        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for i in range(len(cards)):
        if cards[i] not in player:
            print(str(cards[i])+ " not in your hand. Invalid input")
            return False
    return True

def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    if len(cards) < 2:
        print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
    for i in range(len(cards)-1):
        if cards[i]%100 != cards[i+1]%100:
            return False
    return True
    


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    sorted_cards = cards[:]
    sorted_cards.sort()
    if len(sorted_cards) < 3:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False
    for i in range(len(sorted_cards)-1):
        if sorted_cards[i]//100 != sorted_cards[i+1]//100:
            print("Invalid sequence. Cards are not of same suit.")
            return False
        elif sorted_cards[i]+1 != sorted_cards[i+1]:
            print("Invaild sequence. While the cards are of the same suit the ranks are not consecutive integers.")
            return False
    return True

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    print("Discard any card of your choosing.")
    card = int(input("Which card would you like to discard? "))
    while card not in player:
        print(card)
        print("No such card in your hand. Try again.")
        card = int(input("Which card would you like to discard? "))
    print("\nHere is your new hand printed in two ways:")
    player.remove(card)
    print_deck_twice(player)
    return
    

def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    answer = ""
    while answer != "no":
        answer = input("Yes or no, do you have a sequences of three or more of the same suit or two or more of a kind? ").strip().lower()
        if answer == "yes":
            cards = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ").split()
            for i in range(len(cards)):
                cards[i] = int(cards[i])
            if is_valid(cards, player) == True:
                if is_discardable_kind(cards) == True:
                    for i in range(len(cards)):
                        player.remove(cards[i])
                    print("\nHere is your new hand printed in two ways:")
                    print_deck_twice(player)
                elif is_discardable_seq(cards) == True:
                    for i in range(len(cards)):
                        player.remove(cards[i])
                    print("\nHere is your new hand printed in two ways:")
                    print_deck_twice(player)
    return


# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

# YOUR CODE GOES HERE and in all of the above functions instead of keyword pass
if size_change == "yes":
    size = 0
    while size < 3 or size > 99:
        size = int(input("Enter a number between 3 and 99, for the number of ranks: "))
else:
    size = 13
deck = make_deck(size)
print("You are playing with a deck of "+str(size*4)+" cards")
shuffle_deck(deck)
hand = deal_cards_start(deck)
print("Here is your starting hand printed in two ways:")
print_deck_twice(hand)
round_num = 1
while len(hand) != 0:
    print("Welcome to round "+str(round_num)+".")
    if len(deck) == 0:
        print("The game is in empty deck phase.")
        rolled_one_round(hand)
    else:
        print("Please roll the dice.")
        dice = random.randint(1,6)
        print("You rolled the dice and it shows: "+str(dice))
        if dice == 1:
            rolled_one_round(hand)
        else:
            print("Since you rolled "+str(dice)+", the following "+str(dice)+" or "+str(len(deck))+" (if the deck has less than "+str(dice)+" cards) will be added to your hand from the top of the deck.")
            deal_new_cards(deck,hand,dice)
            print("\nHere is your new hand printed in two ways:")
            print_deck_twice(hand)
            rolled_nonone_round(hand)
    print("Round "+str(round_num)+" completed.")
    round_num += 1
print("Congradulations, you completed the game in "+str(round_num-1)+" rounds.")

  
