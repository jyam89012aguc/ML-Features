import pandas as pd
import numpy as np
from typing import Dict, Any

def vdist_3rd_derivatives(df: pd.DataFrame) -> pd.DataFrame:
    """
    Domain 34: Volatility Distribution - 3rd Derivatives (Jerk/Acceleration)
    Acceleration of distributional shifts.
    """
    res = pd.DataFrame(index=df.index)
    
    log_ret = np.log(df['close'] / df['close'].shift(1))
    daily_vol = log_ret.rolling(window=5).std()
    
    horizons = [5, 21, 63, 126, 252]
    
    # Acceleration of Skewness
    for h in horizons:
        skew = daily_vol.rolling(window=h).skew()
        vel = skew.diff(periods=h // 2 if h > 2 else 1)
        res[f'vdist_a_001_{h}'] = vel.diff(periods=h // 2 if h > 2 else 1)
        
    # Acceleration of Kurtosis
    for h in horizons:
        kurt = daily_vol.rolling(window=h).kurt()
        vel = kurt.diff(periods=h // 2 if h > 2 else 1)
        res[f'vdist_a_006_{h}'] = vel.diff(periods=h // 2 if h > 2 else 1)
        
    # Acceleration of Gini (Concentration)
    for h in horizons:
        def gini(x):
            x = x[~np.isnan(x)]
            if len(x) < 2 or np.sum(x) == 0: return np.nan
            sorted_x = np.sort(x)
            n = len(x)
            index = np.arange(1, n + 1)
            return (np.sum((2 * index - n - 1) * sorted_x)) / (n * np.sum(sorted_x))
        gini_series = daily_vol.rolling(window=h).apply(gini, raw=True)
        vel = gini_series.diff(periods=h // 2 if h > 2 else 1)
        res[f'vdist_a_011_{h}'] = vel.diff(periods=h // 2 if h > 2 else 1)
        
    # Acceleration of Vol of Vol
    for h in horizons:
        vov = daily_vol.rolling(window=h).std()
        vel = vov.diff(periods=h // 2 if h > 2 else 1)
        res[f'vdist_a_016_{h}'] = vel.diff(periods=h // 2 if h > 2 else 1)
        
    # Acceleration of Panic Density
    for h in horizons:
        def high_decile_density(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            threshold = np.percentile(x, 90)
            return (x >= threshold).sum() / len(x)
        panic = daily_vol.rolling(window=h).apply(high_decile_density, raw=True)
        vel = panic.diff(periods=h // 2 if h > 2 else 1)
        res[f'vdist_a_021_{h}'] = vel.diff(periods=h // 2 if h > 2 else 1)

    return res

VDIST_A_REGISTRY = {
    'vdist_3rd_derivatives': vdist_3rd_derivatives
}
