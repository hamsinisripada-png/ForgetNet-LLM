import math

def retention(age_days, decay_rate=0.05):
    return math.exp(-decay_rate * age_days)
