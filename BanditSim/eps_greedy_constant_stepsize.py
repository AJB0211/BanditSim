from .multiarmedbandit import MultiArmedBandit
from .update_rules import constant_update_rule
from .action_selections import epsilon_greedy_action


class EpsilonGreedyConstantStepsize(MultiArmedBandit):
    def __init__(self, levers, initial_values, alpha, epsilon, seed = 6):
        super().__init__(levers, initial_values, seed)
        self.alpha   = alpha
        self.epsilon = epsilon

    def _update_rule(self, q, r, a):
        return constant_update_rule(self, q, r, a)

    def _action_selection(self):
        return epsilon_greedy_action(self)
