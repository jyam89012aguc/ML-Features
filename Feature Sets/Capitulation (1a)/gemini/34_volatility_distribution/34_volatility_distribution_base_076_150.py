import pandas as pd
import numpy as np
from typing import Dict, Any

def vdist_076_150(df: pd.DataFrame) -> pd.DataFrame:
    """
    Domain 34: Volatility Distribution - Base Features 076-150
    """
    res = pd.DataFrame(index=df.index)
    
    log_ret = np.log(df['close'] / df['close'].shift(1))
    daily_vol = log_ret.rolling(window=5).std()
    
    horizons = [5, 21, 63, 126, 252]
    
    # 16. Median Absolute Deviation of volatility
    for h in horizons:
        def mad(x):
            x = x[~np.isnan(x)]
            if len(x) < 5: return np.nan
            median = np.median(x)
            return np.median(np.abs(x - median))
        res[f'vdist_076_{h}'] = daily_vol.rolling(window=h).apply(mad, raw=True)
        
    # 17. Ratio of IQR to Total Range of Volatility
    for h in horizons:
        def iqr_range_ratio(x):
            x = x[~np.isnan(x)]
            if len(x) < 5: return np.nan
            r = np.max(x) - np.min(x)
            if r == 0: return 0
            return (np.percentile(x, 75) - np.percentile(x, 25)) / r
        res[f'vdist_081_{h}'] = daily_vol.rolling(window=h).apply(iqr_range_ratio, raw=True)
        
    # 18. Volatility density in the lowest decile (Apathy density)
    for h in horizons:
        def low_decile_density(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            threshold = np.percentile(x, 10)
            return (x <= threshold).sum() / len(x)
        res[f'vdist_086_{h}'] = daily_vol.rolling(window=h).apply(low_decile_density, raw=True)
        
    # 19. Volatility density in the highest decile (Panic density)
    for h in horizons:
        def high_decile_density(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            threshold = np.percentile(x, 90)
            return (x >= threshold).sum() / len(x)
        res[f'vdist_091_{h}'] = daily_vol.rolling(window=h).apply(high_decile_density, raw=True)
        
    # 20. Skewness of 'Volatility Shocks' (vol / rolling_mean_vol)
    for h in horizons:
        shocks = daily_vol / daily_vol.rolling(window=21).mean()
        res[f'vdist_096_{h}'] = shocks.rolling(window=h).skew()
        
    # 21. Kurtosis of 'Volatility Shocks'
    for h in horizons:
        shocks = daily_vol / daily_vol.rolling(window=21).mean()
        res[f'vdist_101_{h}'] = shocks.rolling(window=h).kurt()
        
    # 22. Turnover-weighted volatility distribution skew (if volume exists)
    if 'volume' in df.columns:
        turnover = df['volume'] * df['close']
        for h in horizons:
            # Simplified turnover weighting: weighted skew is complex in rolling. 
            # We'll use corr between vol and turnover as a proxy for weighted distribution bias.
            res[f'vdist_106_{h}'] = daily_vol.rolling(window=h).corr(turnover)
    else:
        for h in horizons:
            res[f'vdist_106_{h}'] = np.nan
            
    # 23. Persistence of volatility in the top quintile
    for h in horizons:
        def top_quintile_persistence(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            thresh = np.percentile(x, 80)
            is_high = (x > thresh).astype(int)
            # Count transitions from high to high
            transitions = np.sum((is_high[:-1] == 1) & (is_high[1:] == 1))
            total_high = np.sum(is_high[:-1])
            if total_high == 0: return 0
            return transitions / total_high
        res[f'vdist_111_{h}'] = daily_vol.rolling(window=h).apply(top_quintile_persistence, raw=True)
        
    # 24. Volatility Distribution Drift (Median(t) / Median(t-h))
    for h in horizons:
        median_vol = daily_vol.rolling(window=h).median()
        res[f'vdist_116_{h}'] = median_vol / median_vol.shift(h)
        
    # 25. Volatility Spread Expansion (IQR(t) / IQR(t-h))
    for h in horizons:
        q75 = daily_vol.rolling(window=h).quantile(0.75)
        q25 = daily_vol.rolling(window=h).quantile(0.25)
        iqr = q75 - q25
        res[f'vdist_121_{h}'] = iqr / iqr.shift(h)
        
    # 26. Price Skewness * Volatility Kurtosis (Joint Distribution Score)
    for h in horizons:
        p_skew = df['close'].pct_change().rolling(window=h).skew()
        v_kurt = daily_vol.rolling(window=h).kurt()
        res[f'vdist_126_{h}'] = p_skew * v_kurt
        
    # 27. Hurst Exponent Proxy for Volatility (RS range / std)
    for h in horizons:
        def hurst_proxy(x):
            x = x[~np.isnan(x)]
            if len(x) < 21: return np.nan
            # Simplified: (max - min) / std
            std = np.std(x)
            if std == 0: return 0
            return (np.max(x) - np.min(x)) / std
        res[f'vdist_131_{h}'] = daily_vol.rolling(window=h).apply(hurst_proxy, raw=True)
        
    # 28. Volatility Path Efficiency (Net change / Total absolute changes)
    for h in horizons:
        def efficiency(x):
            x = x[~np.isnan(x)]
            if len(x) < 5: return np.nan
            net = x[-1] - x[0]
            total = np.sum(np.abs(np.diff(x)))
            if total == 0: return 0
            return net / total
        res[f'vdist_136_{h}'] = daily_vol.rolling(window=h).apply(efficiency, raw=True)
        
    # 29. Count of Volatility 'Climax' events (vol > 3 sigma)
    for h in horizons:
        def climax_count(x):
            x = x[~np.isnan(x)]
            if len(x) < 10: return np.nan
            return (x > np.mean(x) + 3 * np.std(x)).sum()
        res[f'vdist_141_{h}'] = daily_vol.rolling(window=h).apply(climax_count, raw=True)
        
    # 30. Ratio of Volatility skewness to price skewness
    for h in horizons:
        p_skew = df['close'].pct_change().rolling(window=h).skew()
        v_skew = daily_vol.rolling(window=h).skew()
        res[f'vdist_146_{h}'] = v_skew / p_skew.replace(0, np.nan)

    return res

VDIST_REGISTRY = {
    'vdist_076_150': vdist_076_150
}
