from .multiarmedbandit import MultiArmedBandit
from .update_rules import bayesian_update_rule
from .action_selections import epsilon_greedy_action


class EpsilonGreedyBayesianUpdate(MultiArmedBandit):
    def __init__(self, levers, initial_values, epsilon, smoothing, seed=6):
        super().__init__(levers, initial_values, seed)
        self.epsilon   = epsilon
        self.smoothing = smoothing

    def _update_rule(self, q, r, a):
        return bayesian_update_rule(self, q, r, a)

    def _action_selection(self):
        return epsilon_greedy_action(self)

