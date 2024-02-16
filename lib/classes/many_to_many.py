import re

class Game:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
    
    def get_title(self):
        return self._title

    def set_title(self, title):
            if not hasattr(self, "title"):
                self._title = title
    
    title = property(get_title, set_title)

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        players_list = [result.player for result in Result.all if result.game == self]
        player_set = set(players_list)
        return [player for player in player_set]
        
    def average_score(self, player):
        players_games = [result for result in Result.all if result.game == self and result.player == player]
        sum = 0
        for game in players_games:
            sum += game.score
        return sum / len(players_games)
            

class Player:
    all = []

    def __init__(self, username):
            if isinstance(username, str):
                self.username = username
                Player.all.append(self)

    def get_username(self):
        return self._username

    def set_username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
    
    username = property(get_username, set_username)

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games = [result.game for result in Result.all if result.player == self]
        games_set = set(games)
        return [game for game in games_set]

    def played_game(self, game):
        games_played = [result.game for result in Result.all if result.game == game and result.player == self]
        if game in games_played:
            return True
        else: return False
        pass

    def num_times_played(self, game):
        results = [result for result in Result.all if result.player == self and result.game == game]
        return len(results)

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def get_score(self):
        return self._score

    def set_score(self, score):
            if not hasattr(self, "score"):
                self._score = score
    
    score = property(get_score, set_score)