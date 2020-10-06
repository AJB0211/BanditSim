from .multiarmedbandit import MultiArmedBandit
from .update_rules import constant_update_rule
from .action_selections import greedy_action


class GreedyConstantStepsize(MultiArmedBandit):
    def __init__(self, levers, initial_values, alpha, seed = 6):
        super().__init__(levers, initial_values, seed)
        self.alpha = alpha

    def _update_rule(self, q, r, a):
        return constant_update_rule(self, q, r, a)

    def _action_selection(self):
        return greedy_action(self)

