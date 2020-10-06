from copy import deepcopy


class Record(object):
    def __init__(self, states):
        self.actions = []
        self.history = []
        self.rewards = []
        ## TODO: Change implementation to default dict
        self.counts = {k: 0 for k in states}

    def _update(self, q, a, r):
        self.actions.append(a)
        self.rewards.append(r)
        self.history.append(deepcopy(q))
        self.counts[a] += 1

    def reset(self):
        self.actions = []
        self.rewards = []
        self.history = []
        self.counts = {k: 0 for k in self.counts.keys()}

    def __call__(self, q, a, r):
        self._update(q, a, r)

