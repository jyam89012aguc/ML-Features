import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _cross_sectional_momentum_proxy(closeadj, w):
    roc = closeadj.pct_change(w)
    return roc - roc.rolling(w, min_periods=2).median()

# sl5 5d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_5d_slope_v001_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_5d_slope_v002_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_5d_slope_v003_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.rolling(5, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_5d_slope_v004_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = _z(sig, 5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_5d_slope_v005_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_5d_slope_v006_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_5d_slope_v007_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_5d_slope_v008_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_5d_slope_v009_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_5d_slope_v010_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_5d_slope_v011_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_5d_slope_v012_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_5d_slope_v013_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_5d_slope_v014_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_5d_slope_v015_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_10d_slope_v016_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_10d_slope_v017_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_10d_slope_v018_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.rolling(10, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_10d_slope_v019_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = _z(sig, 10)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_10d_slope_v020_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_10d_slope_v021_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_10d_slope_v022_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_10d_slope_v023_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_10d_slope_v024_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_10d_slope_v025_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_10d_slope_v026_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_10d_slope_v027_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_10d_slope_v028_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_10d_slope_v029_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_10d_slope_v030_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_15d_slope_v031_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_15d_slope_v032_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_15d_slope_v033_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.rolling(15, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_15d_slope_v034_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = _z(sig, 15)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_15d_slope_v035_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_15d_slope_v036_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_15d_slope_v037_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_15d_slope_v038_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_15d_slope_v039_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_15d_slope_v040_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_15d_slope_v041_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_15d_slope_v042_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_15d_slope_v043_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_15d_slope_v044_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_15d_slope_v045_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_21d_slope_v046_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_21d_slope_v047_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_21d_slope_v048_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.rolling(21, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_21d_slope_v049_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = _z(sig, 21)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_21d_slope_v050_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_21d_slope_v051_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_21d_slope_v052_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_21d_slope_v053_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_21d_slope_v054_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_21d_slope_v055_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_21d_slope_v056_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_21d_slope_v057_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_21d_slope_v058_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_21d_slope_v059_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_21d_slope_v060_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_42d_slope_v061_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_42d_slope_v062_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_42d_slope_v063_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.rolling(42, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_42d_slope_v064_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = _z(sig, 42)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_42d_slope_v065_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_42d_slope_v066_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_42d_slope_v067_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_42d_slope_v068_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_42d_slope_v069_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_42d_slope_v070_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_42d_slope_v071_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_42d_slope_v072_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_42d_slope_v073_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_42d_slope_v074_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_42d_slope_v075_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_63d_slope_v076_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_63d_slope_v077_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_63d_slope_v078_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.rolling(63, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_63d_slope_v079_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = _z(sig, 63)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_63d_slope_v080_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_63d_slope_v081_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_63d_slope_v082_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_63d_slope_v083_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_63d_slope_v084_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_63d_slope_v085_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_63d_slope_v086_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_63d_slope_v087_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_63d_slope_v088_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_63d_slope_v089_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_63d_slope_v090_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_84d_slope_v091_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_84d_slope_v092_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_84d_slope_v093_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.rolling(84, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_84d_slope_v094_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = _z(sig, 84)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_84d_slope_v095_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_84d_slope_v096_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_84d_slope_v097_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_84d_slope_v098_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_84d_slope_v099_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_84d_slope_v100_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_84d_slope_v101_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_84d_slope_v102_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_84d_slope_v103_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_84d_slope_v104_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_84d_slope_v105_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_126d_slope_v106_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_126d_slope_v107_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_126d_slope_v108_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.rolling(126, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_126d_slope_v109_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = _z(sig, 126)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_126d_slope_v110_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_126d_slope_v111_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_126d_slope_v112_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_126d_slope_v113_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_126d_slope_v114_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_126d_slope_v115_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_126d_slope_v116_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_126d_slope_v117_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_126d_slope_v118_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_126d_slope_v119_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_126d_slope_v120_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_252d_slope_v121_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_252d_slope_v122_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_252d_slope_v123_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.rolling(252, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_252d_slope_v124_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = _z(sig, 252)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_252d_slope_v125_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_252d_slope_v126_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_252d_slope_v127_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_252d_slope_v128_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_252d_slope_v129_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_252d_slope_v130_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_252d_slope_v131_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_252d_slope_v132_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_252d_slope_v133_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_252d_slope_v134_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_252d_slope_v135_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d level xmom
def f15xm_f15_cross_sectional_momentum_xmom_level_504d_slope_v136_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d mean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_504d_slope_v137_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d var xmom
def f15xm_f15_cross_sectional_momentum_xmom_std_504d_slope_v138_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.rolling(504, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d zscore xmom
def f15xm_f15_cross_sectional_momentum_xmom_zscore_504d_slope_v139_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = _z(sig, 504)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d change xmom
def f15xm_f15_cross_sectional_momentum_xmom_delta_504d_slope_v140_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d relchg xmom
def f15xm_f15_cross_sectional_momentum_xmom_pctdelta_504d_slope_v141_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q75gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_upper_gap_504d_slope_v142_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q25gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_lower_gap_504d_slope_v143_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d smean gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_504d_slope_v144_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d energy xmom
def f15xm_f15_cross_sectional_momentum_xmom_energy_504d_slope_v145_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d ewm gap xmom
def f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_504d_slope_v146_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d tail relief xmom
def f15xm_f15_cross_sectional_momentum_xmom_tail_relief_504d_slope_v147_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d peak fade xmom
def f15xm_f15_cross_sectional_momentum_xmom_peak_fade_504d_slope_v148_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d absmean xmom
def f15xm_f15_cross_sectional_momentum_xmom_mean_abs_504d_slope_v149_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d voladj chg xmom
def f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_504d_slope_v150_signal(closeadj):
    sig = _cross_sectional_momentum_proxy(closeadj, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [f15xm_f15_cross_sectional_momentum_xmom_level_5d_slope_v001_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_5d_slope_v002_signal, f15xm_f15_cross_sectional_momentum_xmom_std_5d_slope_v003_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_5d_slope_v004_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_5d_slope_v005_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_5d_slope_v006_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_5d_slope_v007_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_5d_slope_v008_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_5d_slope_v009_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_5d_slope_v010_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_5d_slope_v011_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_5d_slope_v012_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_5d_slope_v013_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_5d_slope_v014_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_5d_slope_v015_signal, f15xm_f15_cross_sectional_momentum_xmom_level_10d_slope_v016_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_10d_slope_v017_signal, f15xm_f15_cross_sectional_momentum_xmom_std_10d_slope_v018_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_10d_slope_v019_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_10d_slope_v020_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_10d_slope_v021_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_10d_slope_v022_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_10d_slope_v023_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_10d_slope_v024_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_10d_slope_v025_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_10d_slope_v026_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_10d_slope_v027_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_10d_slope_v028_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_10d_slope_v029_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_10d_slope_v030_signal, f15xm_f15_cross_sectional_momentum_xmom_level_15d_slope_v031_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_15d_slope_v032_signal, f15xm_f15_cross_sectional_momentum_xmom_std_15d_slope_v033_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_15d_slope_v034_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_15d_slope_v035_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_15d_slope_v036_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_15d_slope_v037_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_15d_slope_v038_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_15d_slope_v039_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_15d_slope_v040_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_15d_slope_v041_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_15d_slope_v042_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_15d_slope_v043_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_15d_slope_v044_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_15d_slope_v045_signal, f15xm_f15_cross_sectional_momentum_xmom_level_21d_slope_v046_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_21d_slope_v047_signal, f15xm_f15_cross_sectional_momentum_xmom_std_21d_slope_v048_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_21d_slope_v049_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_21d_slope_v050_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_21d_slope_v051_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_21d_slope_v052_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_21d_slope_v053_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_21d_slope_v054_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_21d_slope_v055_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_21d_slope_v056_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_21d_slope_v057_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_21d_slope_v058_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_21d_slope_v059_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_21d_slope_v060_signal, f15xm_f15_cross_sectional_momentum_xmom_level_42d_slope_v061_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_42d_slope_v062_signal, f15xm_f15_cross_sectional_momentum_xmom_std_42d_slope_v063_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_42d_slope_v064_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_42d_slope_v065_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_42d_slope_v066_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_42d_slope_v067_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_42d_slope_v068_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_42d_slope_v069_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_42d_slope_v070_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_42d_slope_v071_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_42d_slope_v072_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_42d_slope_v073_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_42d_slope_v074_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_42d_slope_v075_signal, f15xm_f15_cross_sectional_momentum_xmom_level_63d_slope_v076_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_63d_slope_v077_signal, f15xm_f15_cross_sectional_momentum_xmom_std_63d_slope_v078_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_63d_slope_v079_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_63d_slope_v080_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_63d_slope_v081_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_63d_slope_v082_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_63d_slope_v083_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_63d_slope_v084_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_63d_slope_v085_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_63d_slope_v086_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_63d_slope_v087_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_63d_slope_v088_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_63d_slope_v089_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_63d_slope_v090_signal, f15xm_f15_cross_sectional_momentum_xmom_level_84d_slope_v091_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_84d_slope_v092_signal, f15xm_f15_cross_sectional_momentum_xmom_std_84d_slope_v093_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_84d_slope_v094_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_84d_slope_v095_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_84d_slope_v096_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_84d_slope_v097_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_84d_slope_v098_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_84d_slope_v099_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_84d_slope_v100_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_84d_slope_v101_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_84d_slope_v102_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_84d_slope_v103_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_84d_slope_v104_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_84d_slope_v105_signal, f15xm_f15_cross_sectional_momentum_xmom_level_126d_slope_v106_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_126d_slope_v107_signal, f15xm_f15_cross_sectional_momentum_xmom_std_126d_slope_v108_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_126d_slope_v109_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_126d_slope_v110_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_126d_slope_v111_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_126d_slope_v112_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_126d_slope_v113_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_126d_slope_v114_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_126d_slope_v115_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_126d_slope_v116_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_126d_slope_v117_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_126d_slope_v118_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_126d_slope_v119_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_126d_slope_v120_signal, f15xm_f15_cross_sectional_momentum_xmom_level_252d_slope_v121_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_252d_slope_v122_signal, f15xm_f15_cross_sectional_momentum_xmom_std_252d_slope_v123_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_252d_slope_v124_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_252d_slope_v125_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_252d_slope_v126_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_252d_slope_v127_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_252d_slope_v128_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_252d_slope_v129_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_252d_slope_v130_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_252d_slope_v131_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_252d_slope_v132_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_252d_slope_v133_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_252d_slope_v134_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_252d_slope_v135_signal, f15xm_f15_cross_sectional_momentum_xmom_level_504d_slope_v136_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_504d_slope_v137_signal, f15xm_f15_cross_sectional_momentum_xmom_std_504d_slope_v138_signal, f15xm_f15_cross_sectional_momentum_xmom_zscore_504d_slope_v139_signal, f15xm_f15_cross_sectional_momentum_xmom_delta_504d_slope_v140_signal, f15xm_f15_cross_sectional_momentum_xmom_pctdelta_504d_slope_v141_signal, f15xm_f15_cross_sectional_momentum_xmom_upper_gap_504d_slope_v142_signal, f15xm_f15_cross_sectional_momentum_xmom_lower_gap_504d_slope_v143_signal, f15xm_f15_cross_sectional_momentum_xmom_short_mean_gap_504d_slope_v144_signal, f15xm_f15_cross_sectional_momentum_xmom_energy_504d_slope_v145_signal, f15xm_f15_cross_sectional_momentum_xmom_ewm_gap_504d_slope_v146_signal, f15xm_f15_cross_sectional_momentum_xmom_tail_relief_504d_slope_v147_signal, f15xm_f15_cross_sectional_momentum_xmom_peak_fade_504d_slope_v148_signal, f15xm_f15_cross_sectional_momentum_xmom_mean_abs_504d_slope_v149_signal, f15xm_f15_cross_sectional_momentum_xmom_vol_adj_delta_504d_slope_v150_signal]}
F15_CROSS_SECTIONAL_MOMENTUM_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    closeadj = base
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(closeadj)
        y2 = func(closeadj)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_cross_sectional_momentum_proxy" in src
    assert ok_nan >= int(0.80 * len(funcs))
