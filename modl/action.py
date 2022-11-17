import random

class dealer:
    def __init__(self, cards, dir):
        self.cards = cards
        self.dir = dir + '/'

    def shuffle(self, deck):
        buffer_one = []
        buffer_two = []

        for x,y in enumerate(deck):
            if x < len(deck) / 2:
                buffer_one.append(y)
                deck[x] = None
            else:
                buffer_two.append(y)
                deck[x] = None
        
        c_one = 0
        c_two = 0

        for x,y in enumerate(deck):
            if x % 2 == 0:
                deck[x] = buffer_two[c_two]
                c_two += 1
            else:
                deck[x] = buffer_one[c_one]
                c_one += 1

        random.shuffle(deck)   
        return deck
        
    def deal(self, deck, amount_players):
        p = 0
        hands = []
        
        while p <= amount_players:
            hands.append([deck.pop()])
            p += 1

        p = 0
        while p <= amount_players:
            hands[p].append(deck.pop())
            p += 1
        
        return (hands, deck)

    def hit(self, deck):
        card = deck.pop()

        return card, deck

    def calculate_weight(self, hand, card_data) -> int:
        val = 0
        
        for i in hand:
            if 'a' in i:
                if val + 11 <= 21:
                    val += 11
                else:
                    val += 1
            else:
                val += card_data[i][1]

        return val
    
    def win_condition(self, a: int, b: int):
        if a > b:
            return True
        else:
            return False
    
    def write_out(self, fn, time, money):
        with open(self.dir + fn, 'r') as f:
            cont = f.read()

        with open(self.dir + fn, "w") as f:
            try:
                f.write(cont + f"\nUser @ {time} - - {['Lost', 'Won'][money > 0]} {[money, money*-1][money < 0]}")
            except:
                pass

            f.close()