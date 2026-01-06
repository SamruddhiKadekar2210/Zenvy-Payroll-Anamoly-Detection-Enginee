from scipy.stats import ks_2samp

def detect_concept_drift(old_scores, new_scores, alpha=0.05):
    stat, p_value = ks_2samp(old_scores, new_scores)
    return p_value < alpha
