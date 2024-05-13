import numpy as np
class MCP:
    def __init__(self) -> None:
        self.w = None
        self.theta = None

    def run(X, w, theta):
        """Return a numpy array with the predictions from the MCP neuron.

        Keyword arguments:
        X -- a matrix containing the feature vectors 
        w -- the parameters vector
        theta -- the threshold for the MCP
        """
            
        w = np.c_[np.zeros(w.shape[0]) + theta, w]
        return np.where(w.dot(X.T) <= 0, 0, 1)
    
    def fit(self, data, labels):
        data = np.c_[np.ones(data.shape[0]).T, data].T
        self.w = np.random.uniform(size=data.shape[0]).reshape(-1, 1)
        z = np.where(self.w.T.dot(data) <= 0, 0, 1)
        print(data.shape)
        print(self.w.shape)


perceptron = MCP()
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
X_labels = [1, 1, 1, 0]
perceptron.fit(X, X_labels)
        
