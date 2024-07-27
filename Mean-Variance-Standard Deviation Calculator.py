import numpy as np

def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr.flatten())]
    variance = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr.flatten())]
    std_dev = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr.flatten())]
    max_val = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr.flatten())]
    min_val = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr.flatten())]
    total = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr.flatten())]
    
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': total
    }
