from .multiarmedbandit import MultiArmedBandit


class GreedyAverageStep(MultiArmedBandit):
    def __init__(self, levers, initial_values, seed=6):
        super().__init__(levers, initial_values, seed)

    def _update_rule(self, q, r, a):
        return q + (r-q)/self.record.counts[a]

    def _action_selection(self):
        return self.dictmax(self.Qs)

