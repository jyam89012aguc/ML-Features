import pandas as pd
import numpy as np
from typing import Dict, Any

def vdist_2nd_derivatives(df: pd.DataFrame) -> pd.DataFrame:
    """
    Domain 34: Volatility Distribution - 2nd Derivatives (Velocity)
    Rate of change of key distributional metrics.
    """
    res = pd.DataFrame(index=df.index)
    
    log_ret = np.log(df['close'] / df['close'].shift(1))
    daily_vol = log_ret.rolling(window=5).std()
    
    horizons = [5, 21, 63, 126, 252]
    
    # Velocity of Skewness
    for h in horizons:
        skew = daily_vol.rolling(window=h).skew()
        res[f'vdist_v_001_{h}'] = skew.diff(periods=h // 2 if h > 2 else 1)
        
    # Velocity of Kurtosis
    for h in horizons:
        kurt = daily_vol.rolling(window=h).kurt()
        res[f'vdist_v_006_{h}'] = kurt.diff(periods=h // 2 if h > 2 else 1)
        
    # Velocity of Gini (Concentration)
    for h in horizons:
        def gini(x):
            x = x[~np.isnan(x)]
            if len(x) < 2 or np.sum(x) == 0: return np.nan
            sorted_x = np.sort(x)
            n = len(x)
            index = np.arange(1, n + 1)
            return (np.sum((2 * index - n - 1) * sorted_x)) / (n * np.sum(sorted_x))
        gini_series = daily_vol.rolling(window=h).apply(gini, raw=True)
        res[f'vdist_v_011_{h}'] = gini_series.diff(periods=h // 2 if h > 2 else 1)
        
    # Velocity of Vol of Vol
    for h in horizons:
        vov = daily_vol.rolling(window=h).std()
        res[f'vdist_v_016_{h}'] = vov.diff(periods=h // 2 if h > 2 else 1)
        
    # Velocity of Panic Density
    for h in horizons:
        def high_decile_density(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            threshold = np.percentile(x, 90)
            return (x >= threshold).sum() / len(x)
        panic = daily_vol.rolling(window=h).apply(high_decile_density, raw=True)
        res[f'vdist_v_021_{h}'] = panic.diff(periods=h // 2 if h > 2 else 1)

    return res

VDIST_V_REGISTRY = {
    'vdist_2nd_derivatives': vdist_2nd_derivatives
}
