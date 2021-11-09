class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False
        with open("high_score.txt") as hd:
            con = hd.read()
        self.high_score = int(con)

    def reset_stats(self):
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1
