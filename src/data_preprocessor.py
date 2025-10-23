import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_logs(data_frame):
    # Clean missing and non-numeric values
    data_frame = data_frame.dropna()
    num_cols = data_frame.select_dtypes(include=['float64','int64']).columns
    scaler = StandardScaler()
    data_frame[num_cols] = scaler.fit_transform(data_frame[num_cols])
    return data_frame, scaler
