import random

players = []
cards = []
hand = []
value = {} #dictionary that has the player names as the key and the hand as the value
START = 0
new_card = ()


#creates a 52 card deck
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in numbers:
    if num == 10:
        for i in range(1, 17):
            cards.append(num)
    else:
        for i in range(1, 5):
            cards.append(num)

num_players = int(input("How many Players?: "))


# creates number of players
def player(number):
    for i in range(1, number+2):
        players.append(f"player {i}")
    players[-1] = "Dealer"


#deals the starting hands for each player
def deal():
    for j in range(1, 3):
        for i in range(1, num_players+2):
            card_1 = random.choice(cards)
            hand.append(card_1)
            cards.remove(card_1)
            if j ==2:
                value[players[i-1]] = (hand[i-1], hand[i+num_players])
    print(f"{players[-1]}: ({value[players[-1]][0]}, ?)")


#hit card, also removes card from deck
def hit():
    hit_card = random.choice(cards)
    hand.append(hit_card)
    cards.remove(hit_card)
    return hit_card


#displayes the current players hand and the sum of the hand
def intro(start):
    turn = list(value)[start]
    print(f"\n{turn} cards:{value[turn]}, value is {sum(value[turn])}")
    return turn


#if player has 3 cards and wants to hit again
def next(new_card, START):
    new_card += (hit(),)
    value[turn] += new_card
    if sum(value[turn]) > 21:
        print(f"{turn} cards:{value[turn]}, value is {sum(value[turn])} you Busted!")
        START += 1
        new_card = ()
        return START
    else:
        START = START
        new_card = ()
        return START


#prints final hand of all players
def result():
    print(f"\nALL CARDS: {value}")
    print("\nRESULTS:")
    for i in value:
        if i != "Dealer":
            if sum(list(value[i])) <= 21:
                if sum(list(value[i])) < sum(list(value[turn])):
                    print(f"{i} has {sum(list(value[i]))}, Dealer has {sum(list(value[turn]))} you loose")
                if sum(list(value[i])) > sum(list(value[turn])):
                    print(f"{i} has {sum(list(value[i]))}, Dealer has {sum(list(value[turn]))} you win!")
                if sum(list(value[i])) == sum(list(value[turn])):
                    print(f"{i} has {sum(list(value[i]))}, Dealer has {sum(list(value[turn]))} you push")
            else:
                print(f"{i} has {sum(list(value[i]))}, you busted!")


player(num_players)
deal()

game_is_on = True
while game_is_on:

    turn = intro(START)

    if turn != "Dealer":

        move = input("\ndo you want to hit, stay, or double down?:")
        if move == "stay":
            START += 1 #indexes to next player
            new_card = ()
        if move == "hit":
            START = int(next(new_card, START))
        if move == "dd":
            value[turn] += new_card
            if len(value[turn]) >= 3:
                print("can't double down")
            else:
                START = int(next(new_card, START))
                if sum(value[turn]) <= 21:
                    print(f"{turn} cards:{value[turn]}, value is {sum(value[turn])}")
                    START += 1

    if turn == "Dealer":
        if 16 <= sum(value[turn]) <= 21:
            print(result())
            game_is_on = False
        else:
            new_card += (hit(),)
            value[turn] += new_card
            if sum(value[turn]) > 21:
                print(f"{turn} cards:{value[turn]}, value is {sum(value[turn])} everyone wins!")
                new_card = ()
                game_is_on = False
            else:
                if 16 <= sum(value[turn]) <= 21:
                    print(result())
                    game_is_on = False
                else:
                    new_card = ()
