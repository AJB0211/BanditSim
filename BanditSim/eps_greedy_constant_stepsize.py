from .multiarmedbandit import MultiArmedBandit


class EpsilonGreedyConstantStepsize(MultiArmedBandit):
    def __init__(self, levers, initial_values, alpha, epsilon, seed = 6):
        super().__init__(levers, initial_values, seed)
        self.alpha   = alpha
        self.epsilon = epsilon

    def _update_rule(self, q, r, a):
        return q + self.alpha * (r - q)

    def _action_selection(self):
        if self.randgen.random() > self.epsilon:
            return self.dictmax(self.Qs)
        return self.randgen.choice(list(self.levers.keys()))
