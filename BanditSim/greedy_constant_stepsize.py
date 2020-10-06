from .multiarmedbandit import MultiArmedBandit


class GreedyConstantStepsize(MultiArmedBandit):
    def __init__(self, levers, initial_values, alpha, seed = 6):
        super().__init__(levers, initial_values, seed)
        self.alpha = alpha

    def _update_rule(self, q, r, a):
        return q + self.alpha * (r - q)

    def _action_selection(self):
        return self.dictmax(self.Qs)

