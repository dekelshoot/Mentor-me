import numpy as np
from scipy.linalg import eig

class AHP:
    def __init__(self, criteria_matrix, alternative_matrices):
        self.criteria_matrix = criteria_matrix
        self.alternative_matrices = alternative_matrices
        self.criteria_weights = None
        self.alternative_weights = {}
        self.scores = None

    def calculate_weights(self, matrix):
        eigvals, eigvecs = eig(matrix)
        max_eigval = np.max(np.real(eigvals))
        eigvec = np.real(eigvecs[:, np.argmax(np.real(eigvals))])
        weights = eigvec / np.sum(eigvec)
        
        # Consistency calculations
        n = matrix.shape[0]
        CI = (max_eigval - n) / (n - 1)
        RI = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}.get(n, 1.49)  # Random Index
        CR = CI / RI
        
        return weights, CI, CR

    def calculate_criteria_weights(self):
        self.criteria_weights, CI, CR = self.calculate_weights(self.criteria_matrix)
        if CR >= 0.10:
            raise ValueError("The criteria pairwise comparison matrix is not consistent.")
        return self.criteria_weights

    def calculate_alternative_weights(self):
        for crit in self.alternative_matrices:
            weights, CI, CR = self.calculate_weights(self.alternative_matrices[crit])
            if CR >= 0.10:
                raise ValueError(f"The pairwise comparison matrix for {crit} is not consistent.")
            self.alternative_weights[crit] = weights
        return self.alternative_weights

    def calculate_scores(self):
        if self.criteria_weights is None or not self.alternative_weights:
            raise ValueError("Criteria weights or alternative weights are not calculated.")
        
        self.scores = np.zeros(len(next(iter(self.alternative_matrices.values()))))
        for i in range(len(self.scores)):
            for j, crit in enumerate(self.alternative_matrices.keys()):
                self.scores[i] += self.criteria_weights[j] * self.alternative_weights[crit][i]
        return self.scores

    def get_best_alternative(self):
        if self.scores is None:
            raise ValueError("Scores are not calculated.")
        return np.argmax(self.scores)

    def run_ahp(self):
        self.calculate_criteria_weights()
        self.calculate_alternative_weights()
        self.calculate_scores()
        best_alternative_index = self.get_best_alternative()
        return best_alternative_index, self.scores

# Example usage
criteria_matrix = np.array([
    [1, 1/5, 1/4, 1/7],
    [5, 1, 1/2, 1/3],
    [4, 2, 1, 1/3],
    [7, 3, 3, 1]
])

alternative_matrices = {
    "Price": np.array([
        [1, 3, 1/2],
        [1/3, 1, 1/7],
        [2, 7, 1]
    ]),
    "Storage": np.array([
        [1, 1/5, 3],
        [5, 1, 9],
        [1/3, 1/9, 1]
    ]),
    "Processor Speed": np.array([
        [1, 1/2, 1/3],
        [2, 1, 1/2],
        [3, 2, 1]
    ]),
    "RAM Capacity": np.array([
        [1, 1/5, 1/2],
        [5, 1, 3],
        [2, 1/3, 1]
    ])
}

ahp = AHP(criteria_matrix, alternative_matrices)
best_alternative_index, scores = ahp.run_ahp()
alternatives = ["ASUS", "DELL", "LENOVO"]

print("Scores:", scores)
print("Best alternative:", alternatives[best_alternative_index])
# print("criterial weight", ahp.calculate_criteria_weights())