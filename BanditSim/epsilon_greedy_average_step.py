from .multiarmedbandit import MultiArmedBandit
from .action_selections import epsilon_greedy_action
from .update_rules import average_update_rule


class EpsilonGreedyAverageStep(MultiArmedBandit):
    def __init__(self, levers, initial_values, epsilon, seed=6):
        super().__init__(levers, initial_values, seed)
        self.epsilon = epsilon

    def _update_rule(self, q, r, a):
        return average_update_rule(self, q, r, a)

    def _action_selection(self):
        return epsilon_greedy_action(self)
