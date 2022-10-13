import requests as req

card = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
suite = ["c", "d", "h", "s"]

for x in suite:
    for y in card:
        res = req.get(f"https://digisoln.com/resources/cards/{y}{x}.gif")
        f = open(f"{y}{x}.gif", "wb")
        f.write(res.content)
        f.close()

#extra stuff
res = req.get(f"https://digisoln.com/resources/cards/cardback.gif")
f = open("cardback.gif", "wb")
f.write(res.content)
f.close()

