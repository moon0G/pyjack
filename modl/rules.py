class cards:
    def __init__(self):
        self.cards = {}

    def new(self):
        self.cards = {
                        "2c": ["2c.gif", 2],
                        "2d": ["2d.gif", 2],
                        "2h": ["2h.gif", 2],
                        "2s": ["2s.gif", 2],
                        "3c": ["3c.gif", 3],
                        "3d": ["3d.gif", 3],
                        "3h": ["3h.gif", 3],
                        "3s": ["3s.gif", 3],
                        "4c": ["4c.gif", 4],
                        "4d": ["4d.gif", 4],
                        "4h": ["4h.gif", 4],
                        "4s": ["4s.gif", 4],
                        "5c": ["5c.gif", 5],
                        "5d": ["5d.gif", 5],
                        "5h": ["5h.gif", 5],
                        "5s": ["5s.gif", 5],
                        "6c": ["6c.gif", 6],
                        "6d": ["6d.gif", 6],
                        "6h": ["6h.gif", 6],
                        "6s": ["6s.gif", 6],
                        "7c": ["7c.gif", 7],
                        "7d": ["7d.gif", 7],
                        "7h": ["7h.gif", 7],
                        "7s": ["7s.gif", 7],
                        "8c": ["8c.gif", 8],
                        "8d": ["8d.gif", 8],
                        "8h": ["8h.gif", 8],
                        "8s": ["8s.gif", 8],
                        "9c": ["9c.gif", 9],
                        "9d": ["9d.gif", 9],
                        "9h": ["9h.gif", 9],
                        "9s": ["9s.gif", 9],
                        "ac": ["ac.gif", [1, 11]],
                        "ad": ["ad.gif", [1, 11]],
                        "ah": ["ah.gif", [1, 11]],
                        "as": ["as.gif", [1, 11]],
                        "cardback": ["cardback.gif"],
                        "jc": ["jc.gif", 10],
                        "jd": ["jd.gif", 10],
                        "jh": ["jh.gif", 10],
                        "js": ["js.gif", 10],
                        "kc": ["kc.gif", 10],
                        "kd": ["kd.gif", 10],
                        "kh": ["kh.gif", 10],
                        "ks": ["ks.gif", 10],
                        "qc": ["qc.gif", 10],
                        "qd": ["qd.gif", 10],
                        "qh": ["qh.gif", 10],
                        "qs": ["qs.gif", 10],
                        "tc": ["tc.gif", 10],
                        "td": ["td.gif", 10],
                        "th": ["th.gif", 10],
                        "ts": ["ts.gif", 10] 
                    }
        return self.cards