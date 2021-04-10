import random
start=1
valor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
c = 0
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck=[]
if start == 1:
    naipe = 0
    while naipe < 4:
        c = 0
        while c < 13:
            decksuits = [f' _____\n|{(cards[c])}    |\n|(¨v¨)|\n| \ / |\n|  V  |\n|____{(cards[c])}|',
                         f" _____\n|{(cards[c])} _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____{(cards[c])}|",
                         f' _____\n|{(cards[c])} ^  |\n| / \ |\n| \ / |\n|  v  |\n|____{(cards[c])}|',
                         f' _____\n|{(cards[c])} .  | _____\n| /.\ |\n|(_._)|\n|  |  |\n|____{(cards[c])}|']
            deck.append(decksuits[naipe])
            c += 1
        naipe += 1
print(len(deck))
class Player:
    def __init__(self, name,hand,money):   #s
        self.name = name
        self.hand = hand
        self.money = money
    def see_Hand(self):
        print(f"==={self.name}'s Hand===")
        for e in self.hand:
            print(e)
    def bet_Money(self):
        bet = float(input('Quanto quieres apostar?:'))
        if bet > 0:
            self.money -= bet
    def buy_card(self):
        buy = deck.pop(0)
        self.hand.append(buy)

player1 = Player('Pierce', [], 500)
player2 = Player('Margaret',[], 500)
player3 = Player('Cubano', [], 500)
playerlist = [player1, player2, player3]

class Dealer:
    def embaralhar_Cartas(self):
        random.shuffle(deck)
    def deal_Cards(self):
        for n in playerlist:
            carta1 = deck.pop(0)
            carta2 = deck.pop(0)
            n.hand.append(carta1)
            n.hand.append(carta2)
dealer = Dealer()
dealer.embaralhar_Cartas()
dealer.deal_Cards()
player3.see_Hand()
player2.see_Hand()
player1.see_Hand()
print(len(deck))
#para o deck =
#         |A .  | _____
#         | /.\ ||A ^  | _____
#         |(_._)|| / \ ||A _  | _____
#         |  |  || \ / || ( ) ||A_ _ |
#         |____V||  .  ||(_'_)||( v )|
#                |____V||  |  || \ / |
#                       |____V||  .  |
#                              |____V|
