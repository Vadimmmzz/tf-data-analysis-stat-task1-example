import pandas as pd
import numpy as np

chat_id = 230865321 

def solution(x: np.array) -> float:
    l = len(x)
    mist = np.random.normal(-21, np.exp(1), l)
    y = (x + mist)/10
    return y.mean()
