from BanditSim.util import dictmax


def greedy_action(self):
    return dictmax(self.Qs)
