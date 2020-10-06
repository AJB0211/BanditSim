def constant_update_rule(self, q, r, a):
    return q + self.alpha * (r - q)
