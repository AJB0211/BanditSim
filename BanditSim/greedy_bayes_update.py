from .multiarmedbandit import MultiArmedBandit
from .update_rules import bayesian_update_rule
from .action_selections import greedy_action


class GreedyBayesianUpdate(MultiArmedBandit):
    def __init__(self, levers, initial_values, smoothing, seed = 6):
        super().__init__(levers, initial_values, seed)
        self.smoothing = smoothing

    def _update_rule(self, q, r, a):
        return bayesian_update_rule(self, q, r, a)

    def _action_selection(self):
        return greedy_action(self)