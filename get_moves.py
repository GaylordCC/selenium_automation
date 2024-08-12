import numpy as np

def GetMoves(self):
    """ Get all possible moves from this state.
    """
    pos_max = {"QB": 2, "WR": 6, "RB": 6, "TE": 2, "D": 1, "K": 1}

    if len(self.turns) == 0: return []

    roster_positions = np.array([p.position for p in self.rosters[self.turns[0]]], dtype=str)
    moves = [pos for pos, max_ in pos_max.items() if np.sum(roster_positions == pos) < max_]
    return moves