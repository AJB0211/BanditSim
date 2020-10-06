from .multiarmedbandit import MultiArmedBandit
from .action_selections import greedy_action
from .update_rules import average_update_rule


class GreedyAverageStep(MultiArmedBandit):
    def __init__(self, levers, initial_values, seed=6):
        super().__init__(levers, initial_values, seed)

    def _update_rule(self, q, r, a):
        return average_update_rule(self, q, r, a)

    def _action_selection(self):
        return greedy_action(self)

