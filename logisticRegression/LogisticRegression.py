import numpy as np
from nptyping import NDArray

class LogisticRegression:
    def __init__(self, input = None) -> None:
        if input is None:
            self.weight = None
            self.bias = None
        else:
            self.weight = np.random.rand(1, input)
            self.bias = 1
    
    def fit(self, x, y, epochs = 1):
        for _ in range(epochs):
            z = np.dot(self.weight.T, x)+b
            

    def BinaryCrossEntropy(self, y, y_hat, e = 1e-15) -> float:
        y_hat = np.clip(y_hat, e, 1 - e)
        term_0 = (1 - y) * np.log(1 - y_hat + e)  
        term_1 = y * np.log(y_hat + e)  
        return -np.mean(term_0 + term_1)
    
    def _sigmoid(self, x: NDArray[float]) -> NDArray[float]:
        return np.array([self._sigmoid_function(value) for value in x])
    
    def _sigmoid_function(self, x: float) -> float:
        if x >= 0:
            z = np.exp(-x)
            return 1 / (1 + z)
        else:
            z = np.exp(x)
            return z / (1 + z)
    
    def update_model_parameters(self, grad_w, grad_b):
        self.weights = self.weights - 0.1 * grad_w
        self.bias = self.bias - 0.1 * grad_b