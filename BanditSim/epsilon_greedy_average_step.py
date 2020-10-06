from .multiarmedbandit import MultiArmedBandit


class EpsilonGreedyAverageStep(MultiArmedBandit):
    def __init__(self, levers, initial_values, epsilon, seed=6):
        super().__init__(levers, initial_values, seed)
        self.epsilon = epsilon

    def _update_rule(self, q, r, a):
        return q + (r-q)/self.record.counts[a]

    def _action_selection(self):
        if self.randgen.random() > self.epsilon:
            return self.dictmax(self.Qs)
        return self.randgen.choice(list(self.levers.keys()))

