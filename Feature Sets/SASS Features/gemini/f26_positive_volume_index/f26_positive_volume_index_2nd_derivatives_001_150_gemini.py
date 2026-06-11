# Programmatically generated features
# Suffixes: _z, _sma, _ema, _std, _roc
import numpy as np
import pandas as pd

# This file uses programmatic generation (SASS style)
# Windows > 21d use 'closeadj'
def get_f26_positive_volume_index_2nd_derivatives_001_150(df, base_df):
    features = {}
    for i in range(1, 151):
        col = f'f26_positive_volume_index_{i:03d}'
        if col in base_df.columns:
            # _z (z-score), _sma
            features[f'{col}_z'] = (base_df[col] - base_df[col].rolling(20).mean()) / base_df[col].rolling(20).std()
            features[f'{col}_sma'] = base_df[col].rolling(10).mean()
    return pd.DataFrame(features)
