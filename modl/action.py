class dealer:
    def __init__(self, cards):
        self.cards = cards

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

    def hit(self, deck, hand):
        hand.append(deck.pop())

        return hand, deck
        

class server:
    def __init__(self, lock):
        self.lock = lock  

    def handle_connection(self, conn, hand, dealer_deck):
        while True:
                data = str(conn.recv(1024).decode(encoding="utf-8"))
                
                
                if data == "GET HAND":
                    out = ""    
                    for x in hand:
                        out += x + ' '
                    conn.send(out.encode())
                    conn.send(dealer_deck.encode())
                     
                self.lock.release()
                conn.close()
            


