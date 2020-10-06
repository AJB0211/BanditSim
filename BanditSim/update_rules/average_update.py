def average_update_rule(self, q, r, a):
    return q + (r - q) / (self.record.counts[a] + 1)
