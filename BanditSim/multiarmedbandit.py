import random
from copy import deepcopy
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from .record import Record

TABCOLORS = mcolors.TABLEAU_COLORS


class MultiArmedBandit(ABC):
    def __init__(self, levers, initial_values, seed=6):
        self.levers  = levers
        self.Qs      = deepcopy(initial_values)
        self._init_Q = deepcopy(initial_values)

        ## It's cool b/c record is a noun and a verb
        self.record  = Record(levers.keys())

        self.seed    = seed
        self.randgen = random.Random(seed)

    @staticmethod
    def dictmax(d):
        """ returns key with maximum value in dictionary """
        return max(d.keys(), key = lambda x: d[x])

    @abstractmethod
    def _update_rule(self, q, r, a):
        pass

    @abstractmethod
    def _action_selection(self):
        pass

    def reset(self):
        """ Resets environment """
        self.record.reset()
        self.Qs = deepcopy(self._init_Q)

    def _get_reward(self, action):
        return float(self.randgen.random() < self.levers[action])

    def run(self, n_iters, cold_start=True):
        if cold_start:
            self.reset()
        for _ in range(n_iters):
            A = self._action_selection()
            R = self._get_reward(A)
            self.Qs[A] = self._update_rule(self.Qs[A], R, A)

            self.record(self.Qs, A, R)

    def plot_record(self):
        fig, ax = plt.subplots(1, 1, figsize=(14, 8))

        for k, col in zip(self.levers.keys(), TABCOLORS.keys()):
            ax.plot(
                range(len(self.record.history)),
                [Q[k] for Q in self.record.history],
                color=col, linewidth=0.5)

            ax.axhline(self.levers[k], color=col, linestyle="dashed")

        return fig

