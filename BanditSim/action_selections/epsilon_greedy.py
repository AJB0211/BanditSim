from BanditSim.util import dictmax


def epsilon_greedy_action(self):
    if self.randgen.random() > self.epsilon:
        return dictmax(self.Qs)
    return self.randgen.choice(list(self.levers.keys()))