import os
import time
from bs4 import BeautifulSoup
import pandas as pd

from bs4_method import Bs4
from nfl_player import NflPlayer
from draft_state import DraftState
from uct import UCT
from main_draft import current_url

import copy

browser = current_url()
breakpoint()

nfl_players = Bs4().bs4_method(browser)[['PLAYER', 'team', 'position', "FPTS"]].copy()
nfl_players['FPTS'] = nfl_players['FPTS'].astype(float)
freeagents = [NflPlayer(*p) for p in nfl_players.itertuples(index=False, name=None)]

num_competitors = 12
rosters = [[] for _ in range(num_competitors)] # empty rosters to start with

num_rounds = 16
turns = []
# generate turns by snake order
for i in range(num_rounds):
    turns += reversed(range(num_competitors)) if i % 2 else range(num_competitors)
state = DraftState(rosters, turns, freeagents)
iterations = 1000

my_draft_spot = 12

pick_nbr = 0
while state.GetMoves() != []:
    pick_nbr += 1
    # print(pick_nbr)
    # move = UCT(state, iterations)
    # print(move)
    # print("Team", state.turns[0], ":", move, next(p for p in state.freeagents if p.position == move))
    # state.DoMove(move)
    if my_draft_spot == state.turns[0] + 1:
        start_time = time.time()
        move = UCT(state, iterations)
        print("Timing:", round(time.time() - start_time), "seconds")
        print("This is your best pick!", move, next(p for p in state.freeagents if p.position == move))
        os.system('say "Its your pick!"')
        os.system(f'say "{move}, {next(p for p in state.freeagents if p.position == move)}"')
    
    waiting_for_pick = True

    while waiting_for_pick:
        html=browser.page_source
        soup=BeautifulSoup(html,'html.parser')
        div = soup.find_all("div", "jsx-553213854 overflow-hidden w-100")
        data = []
        for i in range(0, len(div[0].find_all("li", {'class':"jsx-2093861861 b--solid bw1 bg-clr-white pick-message__container flex items-end truncate message"}))):
            row = {}
            t = div[0].find_all("li", {'class':"jsx-2093861861 b--solid bw1 bg-clr-white pick-message__container flex items-end truncate message"})[i].text
            row['name'] = t.split(" /")[0]
            row['pick'] = i + 1
            data.append(copy.deepcopy(row))
        picks = pd.DataFrame(data)
        if data:
            if pick_nbr in picks['pick'].to_list():
                temp = picks[picks['pick'] == pick_nbr]
                # print(temp['name'].values[0])
                player_selected = temp['name'].values[0]
                turn = state.turns[0]
                try:
                    state.DoMove("manual", player_selected = player_selected)
                    print(f"Team {turn + 1 if my_draft_spot != turn + 1 else 'Stassen'}: ", player_selected)
                except:
                    try:
                        print(f"{player_selected} Not found, try again")
                        player_manually_selected = input(f"Team {state.turns[0]}")
                        state.DoMove("manual", player_selected = player_manually_selected)
                        print(f"Team {turn + 1 if my_draft_spot != turn + 1 else 'Stassen'}: ", player_manually_selected)
                    except:
                        print(f"{player_selected} Not found, adding manually")
                        print(f"Team {turn + 1 if my_draft_spot != turn + 1 else 'Stassen'}: ", player_selected)
                        state.DoMove("manual", player_selected = player_selected, available="N")
                waiting_for_pick = False
            else:
                time.sleep(1)
        else:
            time.sleep(1)