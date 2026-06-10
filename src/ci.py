import numpy as np
from scipy import stats

def confidence_interval(data, level=0.95):

    mean = np.mean(data)

    std = np.std(data, ddof=1)

    n = len(data)

    return stats.t.interval(
        confidence=level,
        df=n-1,
        loc=mean,
        scale=std/np.sqrt(n)
    )
