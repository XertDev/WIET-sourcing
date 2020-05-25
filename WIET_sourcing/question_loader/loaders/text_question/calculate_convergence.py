import numpy as np
from typing import List

def calculate_convergence(submitted_answers: List[int], total_answers_count: int) -> float:
    answers_arr = np.array(submitted_answers)
    means = answers_arr/total_answers_count
    variances = [(ans_count*(1-mean)**2 + (total_answers_count-ans_count)*mean**2)/total_answers_count
                 for ans_count, mean in zip(answers_arr, means)]
    variance = np.mean(variances)
    return np.exp(-variance)