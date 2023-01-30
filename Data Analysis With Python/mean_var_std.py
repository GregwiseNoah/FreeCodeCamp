import numpy as np

def calculate(list):

  if len(list)<9:
     raise ValueError("List must contain nine numbers.")
  list = [int(i) for i in list]
  arr = np.array([list]).reshape((3,3))
  
  meanl = [np.mean(arr, 0).tolist(),np.mean(arr, 1).tolist(), np.mean(arr)]
  stdl = [np.std(arr, 0).tolist(), np.std(arr, 1).tolist(), np.std(arr)]
  varl = [np.var(arr, 0).tolist(), np.var(arr, 1).tolist(), np.var(arr)]
  maxl = [np.max(arr, 0).tolist(), np.max(arr, 1).tolist(), np.max(arr)]
  minl = [np.min(arr, 0).tolist(), np.min(arr, 1).tolist(), np.min(arr)]
  suml = [np.sum(arr, 0).tolist(), np.sum(arr, 1).tolist(), np.sum(arr)]

  calculations = {"mean": meanl, "variance": varl, "standard deviation": stdl,                           "max": maxl, "min": minl, "sum": suml}

  return calculations