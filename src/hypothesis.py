from scipy.stats import ttest_1samp

def one_sample_test(data, value):

    return ttest_1samp(data, value)
