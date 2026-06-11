# Programmatically generated features
# Suffixes: _z, _sma, _ema, _std, _roc
import numpy as np
import pandas as pd

# This file uses programmatic generation (SASS style)
# Windows > 21d use 'closeadj'
def get_f12_skewness_drift_3rd_derivatives_001_150(df, base_df):
    features = {}
    for i in range(1, 151):
        col = f'f12_skewness_drift_{i:03d}'
        if col in base_df.columns:
            # _ema, _std, _roc
            features[f'{col}_ema'] = base_df[col].ewm(span=10).mean()
            features[f'{col}_std'] = base_df[col].rolling(20).std()
            features[f'{col}_roc'] = base_df[col].pct_change(5)
    return pd.DataFrame(features)
