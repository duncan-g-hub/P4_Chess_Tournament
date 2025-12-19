from models.match import Match


class Turn:
    def __init__(self, matchs:list(Match), current_turn=0, start_datetime=None, end_datetime=None):
        self.matchs = matchs
        self.current_turn = current_turn
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime



    def mix_players_randomly(self):
        pass

    def sort_players(self):
        pass

    def create_turn(self):
        pass

    def finish_turn(self):
        pass


