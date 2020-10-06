## TODO: Fix this function
##       maybe look into Bayesian methods in RL?
def bayesian_update_rule(self, q, r, a):
    """
    q is the prior
    _alpha, _beta parameters of a beta binomial

    q := \frac{\alpha + \beta}{\alpha+\beta+n}\frac{\alpha}{\alpha+\beta} + \frac{1}{\alpha+\beta+n} * R
    = \frac{\alpha + \beta}{\alpha + \beta + n}q + \frac{R}{\alpha + \beta + n}

    :param self:
    :param q:
    :param r:
    :param a:
    :return:
    """
    alpha = q * self.smoothing
    beta = self.smoothing * (1 - q)
    abn = alpha + beta + self.record.counts[a]+1
    return (alpha + beta) * q / abn + r / abn
