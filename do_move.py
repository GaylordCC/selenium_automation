from nfl_player import NflPlayer

def DoMove(self, move, player_selected = "", available = "Y"):
    """ Update a state by carrying out the given move.
        Must update playerJustMoved.
    """
    # print(move)
    if move != "manual":
        player = next(p for p in self.freeagents if p.position == move)
    elif available == "Y":
        # player = next(x for x in state.freeagents if x.name == player_selected )
        player = next(x for x in self.freeagents if x.name == player_selected )
    # print(player)
    rosterId = self.turns.pop(0)
    if available == "Y":
        self.freeagents.remove(player)
        self.rosters[rosterId].append(player)
    else:
        team = input(f"{player_selected}'s team")
        position = input(f"{player_selected}'s postion")
        player_selected = NflPlayer(player_selected, team, position, 0)

        self.rosters[rosterId].append(player_selected)
    
    self.playerJustMoved = rosterId