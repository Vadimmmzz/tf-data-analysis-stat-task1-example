import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x=x+21
    y=np.exp(x)
    return y.mean() # Ваш ответ
