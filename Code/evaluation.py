class evalMetrics():
    
    """
    Returns various methods of common evaluation metrics used to measure the performance of binary classification models.
    
    Arguments:
    conMat: An sklearn confusion matrix object. 
    """
    
    def __init__(self, conMat):
        
        self.tp = conMat[0][0]
        self.tn = conMat[1][1]
        self.fp = conMat[1][0]
        self.fn = conMat[0][1]
    
    def accuracy(self):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fn + self.fp)

    def precision(self):
        return self.tp / (self.tp + self.fp)

    def recall(self):
        return self.tp / (self.tp + self.fn)
    
    def fScore(self):
        return (2 * self.recall() * self.precision()) / (self.precision() + self.recall())
    
    def negativePredictiveValue(self):
        return self.tn / (self.tn + self.fn)
    
    def positivePredictiveValue(self):
        return self.tp / (self.tp + self.fp)