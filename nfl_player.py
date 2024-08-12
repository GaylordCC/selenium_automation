class NflPlayer:
    def __init__(self, name, team, position, points):
        self.name = name
        self.team = team
        self.position = position
        self.points = points
        
    def __repr__(self):
        return "|".join([self.name, self.team, self.position, str(self.points)])