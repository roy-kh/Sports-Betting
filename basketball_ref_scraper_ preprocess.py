from basketball_ref_scraper.constants import TEAM_TO_TEAM_ABBR
from basketball_ref_scraper.constants import CURR_NBA_TEAMS

from basketball_ref_scraper.teams import get_roster
from basketball_ref_scraper.games import get_games
from basketball_ref_scraper.players import get_game_logs
from basketball_ref_scraper.games import get_games_playoffs
from basketball_ref_scraper.teams import get_team_stats
from basketball_ref_scraper.teams import get_playoff_wins


import numpy as np
import pandas as pd
import os
import requests
import time

# Adjusting basketball_ref_scraper variables to make the dataset easier to work with.

class Dataset:
    def __init__(self, team, year):
        self.team = team
        self.year = year
        self.roster = get_roster(team, year)
        self.team_logs = get_games(team, year)
        self.player_logs = {}
        for player in self.roster["PLAYER"]:
            self.player_logs[player] = get_game_logs(player, year)
        # for player in self.roster["PLAYER"]:
        #     self.player_logs[player] = get_games_playoffs(player, year)
        self.save_data()
        
    def save_data(self):
        save_path = 'data/NBA_{}/{}_{}'.format(self.year, self.team, self.year)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        self.team_logs.to_csv(save_path + '/team_logs.csv')
        self.roster.to_csv(save_path + '/roster.csv')
        for player in self.roster["PLAYER"]:
            if self.player_logs[player] is not None:
                if not isinstance(self.player_logs[player], str):
                    self.player_logs[player].to_csv(save_path + '/{}.csv'.format(player))
                
class PlayoffSet:
    def __init__(self, team, year):
        self.team = team
        self.year = year
        self.team_logs = get_games_playoffs(team, year)
        if self.team_logs is not None:
            save_path = 'data/NBA_playoffs_{}/{}_{}'.format(self.year, self.team, self.year)
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            self.team_logs.to_csv(save_path + '/team_logs.csv')

class TeamSet:
    def __init__(self, year):
        self.year = year
        self.team_stats = get_team_stats(year)
        self.playoff_wins = get_playoff_wins(year)
        if self.team_stats is not None:
            save_path = 'data/NBA_team_stats/{}'.format(self.year)
            os.makedirs(save_path, exist_ok=True)
            self.team_stats.to_csv(save_path + '/team_stats.csv')
        if self.playoff_wins is not None:
            save_path = 'data/NBA_playoff_wins/{}'.format(self.year)
            os.makedirs(save_path, exist_ok=True)
            self.playoff_wins.to_csv(save_path + '/playoff_wins.csv')
        else:
            print("failed")

if __name__ == "__main__":
    for year in range(2013, 2024):
        print(year)
        TeamSet(year)
        

"""
if __name__ == "__main__":
    # team = "New York Knicks"
    # team_abbr = TEAM_TO_TEAM_ABBR[team.upper()]
    # year = 2022
    # Dataset(team_abbr, year)
    counter = 10
    
    while True:
        team = CURR_NBA_TEAMS[counter]
        team_abbr = TEAM_TO_TEAM_ABBR[team.upper()]
        year = 2022
        Dataset(team_abbr, year)
        counter = (counter + 1)%30
        if(team == "Washington Wizards"):
            break
        time.sleep(1 * 30 * 60)  # 1 hours in seconds
    # for team in CURR_NBA_TEAMS:
    #     team_abbr = TEAM_TO_TEAM_ABBR[team.upper()]
    #     Dataset(team_abbr, year)
"""        
