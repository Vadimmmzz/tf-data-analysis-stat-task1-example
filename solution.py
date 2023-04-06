import pandas as pd
import numpy as np


chat_id = 230865321 

def solution(x: np.array) -> float:
    x=x+21
    y=np.exp(x)
    return y.mean()/10
