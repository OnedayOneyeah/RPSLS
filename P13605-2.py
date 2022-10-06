# Initial Settings
import random
import pandas as pd
import numpy as np
from RPSLS_player import RPSLS_player
from Queue import Queue

# Player
class P13605(RPSLS_player):
    def __init__(self):
        self._shootings =["rock", "paper", "scissors", "lizard", "spock"]
        self._whats_next = {"rock": {"rock":0.2, "paper":0.2, "scissors":0.2, "lizard":0.2, "spock":0.2},
                           "paper": {"rock":0.2, "paper":0.2, "scissors":0.2, "lizard":0.2, "spock":0.2},
                           "scissors": {"rock":0.2, "paper":0.2, "scissors":0.2, "lizard":0.2, "spock":0.2},
                           "lizard": {"rock":0.2, "paper":0.2,"scissors":0.2, "lizard":0.2, "spock":0.2},
                           "spock": {"rock":0.2, "paper":0.2, "scissors":0.2, "lizard":0.2, "spock":0.2}}
        self._whats_next = pd.DataFrame(self._whats_next)
        self._last = "None"
        self._last_ten = Queue()
        self._whats_next_percentage = np.array([0,0,0,0,0])
        self._expectation = "None"

    def shoot(self):
        if self._last == "None":
            self._shoot = random.choice(self._shootings)
        else:
            self._expectation = self._whats_next.loc[:, self._last].idxmax()
            if self._expectation == "scissors":
                self._shoot = random.choice(["rock", "spock"])
            elif self._expectation == "paper":
                self._shoot = random.choice(["scissors", "lizard"])
            elif self._expectation == "rock":
                self._shoot = random.choice(["paper", "spock"])
            elif self._expectation == "lizard":
                self._shoot = random.choice(["rock", "scissors"])
            elif self._expectation == "spock":
                self._shoot = random.choice(["paper", "lizard"])                                    
        return self._shoot
    

    def update(self, result: str, competitor_shot: str):
        self._last_ten.update(competitor_shot)
        self._last = self._last_ten.rtnqueue()[9]

        for i in range(9):
            if self._last_ten.rtnqueue()[i] == self._last:
                if self._last_ten.rtnqueue()[i+1] == "rock":
                    self._whats_next_percentage[0] += 1
                elif self._last_ten.rtnqueue()[i+1] == "paper":
                    self._whats_next_percentage[1] += 1
                elif self._last_ten.rtnqueue()[i+1] == "scissors":
                    self._whats_next_percentage[2] += 1
                elif self._last_ten.rtnqueue()[i+1] == "lizard":
                    self._whats_next_percentage[3] += 1
                elif self._last_ten.rtnqueue()[i+1] == "spock":
                    self._whats_next_percentage[4] += 1
            
        if not self._last_ten.rtnqueue().count('None') != 10:
            self._whats_next_percentage = self._whats_next_percentage/self._whats_next_percentage.sum()
        self._whats_next.loc[:,[self._last]] = self._whats_next_percentage[1]

        
