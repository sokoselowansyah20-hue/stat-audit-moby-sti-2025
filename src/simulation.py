import numpy as np

def monte_carlo(lam, size=10000):

    return np.random.poisson(
        lam=lam,
        size=size
    )
