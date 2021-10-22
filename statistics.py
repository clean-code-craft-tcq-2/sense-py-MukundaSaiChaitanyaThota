
def calculateStats(numbers):
    if len(numbers) != 0:
        avg = round(sum(numbers)/len(numbers),3)
        max1 = max(numbers)
        min1 = min(numbers)
        stats = {"avg":avg,"max":max1,"min":min1}
    
    else:
        stats = {"avg":float("NaN"),"max":float("NaN"),"min":float("NaN")}
        
    return stats

class EmailAlert():
    def __init__(self):
        self.emailSent = 0

class LEDAlert():
    def __init__(self):
        self.ledGlows = 0
        
class StatsAlerter():
    def __init__(self, maxThreshold, Alerts):
        self.maxThreshold = maxThreshold
        self.Alerts = Alerts
    def checkAndAlert(self, numbers):
        if max(numbers) > self.maxThreshold:
            self.Alerts[0].emailSent = 1
            self.Alerts[1].ledGlows = 1
        else:
            self.Alerts[0].emailSent = 0
            self.Alerts[1].ledGlows = 0
