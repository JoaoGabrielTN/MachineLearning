import numpy as np
class MCP:
    def __init__(self) -> None:
        pass

    def run(X, w, theta):
        """Return a numpy array with the predictions from the MCP neuron.

        Keyword arguments:
        X -- a matrix containing the feature vectors 
        w -- the parameters vector
        theta -- the threshold for the MCP
        """
        return np.where(w.T.dot(X)-theta <= 0, 0, 1)
        
