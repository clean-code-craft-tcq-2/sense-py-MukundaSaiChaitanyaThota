import numpy as np

def calculateStats(numbers):
    if len(numbers) != 0:
        avg = round(sum(numbers)/len(numbers),3)
        max1 = max(numbers)
        min1 = min(numbers)
        stats = {"avg":avg,"max":max1,"min":min1}
    
    else:
        stats = {"avg":np.nan,"max":np.nan,"min":np.nan}
    return stats
