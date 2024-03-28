import numpy as np
class MCP:
    def __init__(self) -> None:
        pass

    def run(X, w, theta):
        return np.where(w.T.dot(X)-theta <= 0, 0, 1)
        
