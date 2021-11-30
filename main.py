import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def predict_salary(years_of_experience):
    # Data
    raw_data = {
        'years_worked': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'salary': [60, 100, 130, 150, 180, 230, 260, 270, 290, 330]
    }

    df = pd.DataFrame(raw_data)
    print(df)


predict_salary(12)
