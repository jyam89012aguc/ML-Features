import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _candle_body_ratio(open, high, low, close, w):
    body = close - open
    rng = (high - low).abs().replace(0, np.nan)
    return (body / rng).rolling(w, min_periods=2).mean()

# jk5 5d level body
def f06cb_f06_candle_body_ratios_body_level_5d_jerk_v001_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d mean body
def f06cb_f06_candle_body_ratios_body_mean_5d_jerk_v002_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d var body
def f06cb_f06_candle_body_ratios_body_std_5d_jerk_v003_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_5d_jerk_v004_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = _z(sig, 5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d change body
def f06cb_f06_candle_body_ratios_body_delta_5d_jerk_v005_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_5d_jerk_v006_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_5d_jerk_v007_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_5d_jerk_v008_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_5d_jerk_v009_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d energy body
def f06cb_f06_candle_body_ratios_body_energy_5d_jerk_v010_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_5d_jerk_v011_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_5d_jerk_v012_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_5d_jerk_v013_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_5d_jerk_v014_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_5d_jerk_v015_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d level body
def f06cb_f06_candle_body_ratios_body_level_10d_jerk_v016_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d mean body
def f06cb_f06_candle_body_ratios_body_mean_10d_jerk_v017_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d var body
def f06cb_f06_candle_body_ratios_body_std_10d_jerk_v018_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_10d_jerk_v019_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = _z(sig, 10)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d change body
def f06cb_f06_candle_body_ratios_body_delta_10d_jerk_v020_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_10d_jerk_v021_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_10d_jerk_v022_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_10d_jerk_v023_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_10d_jerk_v024_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d energy body
def f06cb_f06_candle_body_ratios_body_energy_10d_jerk_v025_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_10d_jerk_v026_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_10d_jerk_v027_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_10d_jerk_v028_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_10d_jerk_v029_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_10d_jerk_v030_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d level body
def f06cb_f06_candle_body_ratios_body_level_15d_jerk_v031_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d mean body
def f06cb_f06_candle_body_ratios_body_mean_15d_jerk_v032_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d var body
def f06cb_f06_candle_body_ratios_body_std_15d_jerk_v033_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_15d_jerk_v034_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = _z(sig, 15)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d change body
def f06cb_f06_candle_body_ratios_body_delta_15d_jerk_v035_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_15d_jerk_v036_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_15d_jerk_v037_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_15d_jerk_v038_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_15d_jerk_v039_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d energy body
def f06cb_f06_candle_body_ratios_body_energy_15d_jerk_v040_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_15d_jerk_v041_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_15d_jerk_v042_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_15d_jerk_v043_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_15d_jerk_v044_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_15d_jerk_v045_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d level body
def f06cb_f06_candle_body_ratios_body_level_21d_jerk_v046_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d mean body
def f06cb_f06_candle_body_ratios_body_mean_21d_jerk_v047_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d var body
def f06cb_f06_candle_body_ratios_body_std_21d_jerk_v048_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_21d_jerk_v049_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = _z(sig, 21)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d change body
def f06cb_f06_candle_body_ratios_body_delta_21d_jerk_v050_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_21d_jerk_v051_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_21d_jerk_v052_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_21d_jerk_v053_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_21d_jerk_v054_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d energy body
def f06cb_f06_candle_body_ratios_body_energy_21d_jerk_v055_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_21d_jerk_v056_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_21d_jerk_v057_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_21d_jerk_v058_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_21d_jerk_v059_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_21d_jerk_v060_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d level body
def f06cb_f06_candle_body_ratios_body_level_42d_jerk_v061_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d mean body
def f06cb_f06_candle_body_ratios_body_mean_42d_jerk_v062_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d var body
def f06cb_f06_candle_body_ratios_body_std_42d_jerk_v063_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_42d_jerk_v064_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = _z(sig, 42)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d change body
def f06cb_f06_candle_body_ratios_body_delta_42d_jerk_v065_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_42d_jerk_v066_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_42d_jerk_v067_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_42d_jerk_v068_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_42d_jerk_v069_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d energy body
def f06cb_f06_candle_body_ratios_body_energy_42d_jerk_v070_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_42d_jerk_v071_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_42d_jerk_v072_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_42d_jerk_v073_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_42d_jerk_v074_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_42d_jerk_v075_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d level body
def f06cb_f06_candle_body_ratios_body_level_63d_jerk_v076_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d mean body
def f06cb_f06_candle_body_ratios_body_mean_63d_jerk_v077_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d var body
def f06cb_f06_candle_body_ratios_body_std_63d_jerk_v078_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_63d_jerk_v079_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = _z(sig, 63)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d change body
def f06cb_f06_candle_body_ratios_body_delta_63d_jerk_v080_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_63d_jerk_v081_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_63d_jerk_v082_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_63d_jerk_v083_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_63d_jerk_v084_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d energy body
def f06cb_f06_candle_body_ratios_body_energy_63d_jerk_v085_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_63d_jerk_v086_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_63d_jerk_v087_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_63d_jerk_v088_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_63d_jerk_v089_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_63d_jerk_v090_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d level body
def f06cb_f06_candle_body_ratios_body_level_84d_jerk_v091_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d mean body
def f06cb_f06_candle_body_ratios_body_mean_84d_jerk_v092_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d var body
def f06cb_f06_candle_body_ratios_body_std_84d_jerk_v093_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_84d_jerk_v094_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = _z(sig, 84)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d change body
def f06cb_f06_candle_body_ratios_body_delta_84d_jerk_v095_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_84d_jerk_v096_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_84d_jerk_v097_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_84d_jerk_v098_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_84d_jerk_v099_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d energy body
def f06cb_f06_candle_body_ratios_body_energy_84d_jerk_v100_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_84d_jerk_v101_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_84d_jerk_v102_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_84d_jerk_v103_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_84d_jerk_v104_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_84d_jerk_v105_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d level body
def f06cb_f06_candle_body_ratios_body_level_126d_jerk_v106_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d mean body
def f06cb_f06_candle_body_ratios_body_mean_126d_jerk_v107_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d var body
def f06cb_f06_candle_body_ratios_body_std_126d_jerk_v108_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_126d_jerk_v109_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = _z(sig, 126)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d change body
def f06cb_f06_candle_body_ratios_body_delta_126d_jerk_v110_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_126d_jerk_v111_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_126d_jerk_v112_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_126d_jerk_v113_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_126d_jerk_v114_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d energy body
def f06cb_f06_candle_body_ratios_body_energy_126d_jerk_v115_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_126d_jerk_v116_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_126d_jerk_v117_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_126d_jerk_v118_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_126d_jerk_v119_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_126d_jerk_v120_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d level body
def f06cb_f06_candle_body_ratios_body_level_252d_jerk_v121_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d mean body
def f06cb_f06_candle_body_ratios_body_mean_252d_jerk_v122_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d var body
def f06cb_f06_candle_body_ratios_body_std_252d_jerk_v123_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_252d_jerk_v124_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = _z(sig, 252)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d change body
def f06cb_f06_candle_body_ratios_body_delta_252d_jerk_v125_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_252d_jerk_v126_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_252d_jerk_v127_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_252d_jerk_v128_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_252d_jerk_v129_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d energy body
def f06cb_f06_candle_body_ratios_body_energy_252d_jerk_v130_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_252d_jerk_v131_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_252d_jerk_v132_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_252d_jerk_v133_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_252d_jerk_v134_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_252d_jerk_v135_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d level body
def f06cb_f06_candle_body_ratios_body_level_504d_jerk_v136_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d mean body
def f06cb_f06_candle_body_ratios_body_mean_504d_jerk_v137_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d var body
def f06cb_f06_candle_body_ratios_body_std_504d_jerk_v138_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d zscore body
def f06cb_f06_candle_body_ratios_body_zscore_504d_jerk_v139_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = _z(sig, 504)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d change body
def f06cb_f06_candle_body_ratios_body_delta_504d_jerk_v140_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d relchg body
def f06cb_f06_candle_body_ratios_body_pctdelta_504d_jerk_v141_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q75gap body
def f06cb_f06_candle_body_ratios_body_upper_gap_504d_jerk_v142_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q25gap body
def f06cb_f06_candle_body_ratios_body_lower_gap_504d_jerk_v143_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d smean gap body
def f06cb_f06_candle_body_ratios_body_short_mean_gap_504d_jerk_v144_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d energy body
def f06cb_f06_candle_body_ratios_body_energy_504d_jerk_v145_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d ewm gap body
def f06cb_f06_candle_body_ratios_body_ewm_gap_504d_jerk_v146_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d tail relief body
def f06cb_f06_candle_body_ratios_body_tail_relief_504d_jerk_v147_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d peak fade body
def f06cb_f06_candle_body_ratios_body_peak_fade_504d_jerk_v148_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d absmean body
def f06cb_f06_candle_body_ratios_body_mean_abs_504d_jerk_v149_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d voladj chg body
def f06cb_f06_candle_body_ratios_body_vol_adj_delta_504d_jerk_v150_signal(open, high, low, close):
    sig = _candle_body_ratio(open, high, low, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['open', 'high', 'low', 'close'], "func": fn} for fn in [f06cb_f06_candle_body_ratios_body_level_5d_jerk_v001_signal, f06cb_f06_candle_body_ratios_body_mean_5d_jerk_v002_signal, f06cb_f06_candle_body_ratios_body_std_5d_jerk_v003_signal, f06cb_f06_candle_body_ratios_body_zscore_5d_jerk_v004_signal, f06cb_f06_candle_body_ratios_body_delta_5d_jerk_v005_signal, f06cb_f06_candle_body_ratios_body_pctdelta_5d_jerk_v006_signal, f06cb_f06_candle_body_ratios_body_upper_gap_5d_jerk_v007_signal, f06cb_f06_candle_body_ratios_body_lower_gap_5d_jerk_v008_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_5d_jerk_v009_signal, f06cb_f06_candle_body_ratios_body_energy_5d_jerk_v010_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_5d_jerk_v011_signal, f06cb_f06_candle_body_ratios_body_tail_relief_5d_jerk_v012_signal, f06cb_f06_candle_body_ratios_body_peak_fade_5d_jerk_v013_signal, f06cb_f06_candle_body_ratios_body_mean_abs_5d_jerk_v014_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_5d_jerk_v015_signal, f06cb_f06_candle_body_ratios_body_level_10d_jerk_v016_signal, f06cb_f06_candle_body_ratios_body_mean_10d_jerk_v017_signal, f06cb_f06_candle_body_ratios_body_std_10d_jerk_v018_signal, f06cb_f06_candle_body_ratios_body_zscore_10d_jerk_v019_signal, f06cb_f06_candle_body_ratios_body_delta_10d_jerk_v020_signal, f06cb_f06_candle_body_ratios_body_pctdelta_10d_jerk_v021_signal, f06cb_f06_candle_body_ratios_body_upper_gap_10d_jerk_v022_signal, f06cb_f06_candle_body_ratios_body_lower_gap_10d_jerk_v023_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_10d_jerk_v024_signal, f06cb_f06_candle_body_ratios_body_energy_10d_jerk_v025_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_10d_jerk_v026_signal, f06cb_f06_candle_body_ratios_body_tail_relief_10d_jerk_v027_signal, f06cb_f06_candle_body_ratios_body_peak_fade_10d_jerk_v028_signal, f06cb_f06_candle_body_ratios_body_mean_abs_10d_jerk_v029_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_10d_jerk_v030_signal, f06cb_f06_candle_body_ratios_body_level_15d_jerk_v031_signal, f06cb_f06_candle_body_ratios_body_mean_15d_jerk_v032_signal, f06cb_f06_candle_body_ratios_body_std_15d_jerk_v033_signal, f06cb_f06_candle_body_ratios_body_zscore_15d_jerk_v034_signal, f06cb_f06_candle_body_ratios_body_delta_15d_jerk_v035_signal, f06cb_f06_candle_body_ratios_body_pctdelta_15d_jerk_v036_signal, f06cb_f06_candle_body_ratios_body_upper_gap_15d_jerk_v037_signal, f06cb_f06_candle_body_ratios_body_lower_gap_15d_jerk_v038_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_15d_jerk_v039_signal, f06cb_f06_candle_body_ratios_body_energy_15d_jerk_v040_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_15d_jerk_v041_signal, f06cb_f06_candle_body_ratios_body_tail_relief_15d_jerk_v042_signal, f06cb_f06_candle_body_ratios_body_peak_fade_15d_jerk_v043_signal, f06cb_f06_candle_body_ratios_body_mean_abs_15d_jerk_v044_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_15d_jerk_v045_signal, f06cb_f06_candle_body_ratios_body_level_21d_jerk_v046_signal, f06cb_f06_candle_body_ratios_body_mean_21d_jerk_v047_signal, f06cb_f06_candle_body_ratios_body_std_21d_jerk_v048_signal, f06cb_f06_candle_body_ratios_body_zscore_21d_jerk_v049_signal, f06cb_f06_candle_body_ratios_body_delta_21d_jerk_v050_signal, f06cb_f06_candle_body_ratios_body_pctdelta_21d_jerk_v051_signal, f06cb_f06_candle_body_ratios_body_upper_gap_21d_jerk_v052_signal, f06cb_f06_candle_body_ratios_body_lower_gap_21d_jerk_v053_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_21d_jerk_v054_signal, f06cb_f06_candle_body_ratios_body_energy_21d_jerk_v055_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_21d_jerk_v056_signal, f06cb_f06_candle_body_ratios_body_tail_relief_21d_jerk_v057_signal, f06cb_f06_candle_body_ratios_body_peak_fade_21d_jerk_v058_signal, f06cb_f06_candle_body_ratios_body_mean_abs_21d_jerk_v059_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_21d_jerk_v060_signal, f06cb_f06_candle_body_ratios_body_level_42d_jerk_v061_signal, f06cb_f06_candle_body_ratios_body_mean_42d_jerk_v062_signal, f06cb_f06_candle_body_ratios_body_std_42d_jerk_v063_signal, f06cb_f06_candle_body_ratios_body_zscore_42d_jerk_v064_signal, f06cb_f06_candle_body_ratios_body_delta_42d_jerk_v065_signal, f06cb_f06_candle_body_ratios_body_pctdelta_42d_jerk_v066_signal, f06cb_f06_candle_body_ratios_body_upper_gap_42d_jerk_v067_signal, f06cb_f06_candle_body_ratios_body_lower_gap_42d_jerk_v068_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_42d_jerk_v069_signal, f06cb_f06_candle_body_ratios_body_energy_42d_jerk_v070_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_42d_jerk_v071_signal, f06cb_f06_candle_body_ratios_body_tail_relief_42d_jerk_v072_signal, f06cb_f06_candle_body_ratios_body_peak_fade_42d_jerk_v073_signal, f06cb_f06_candle_body_ratios_body_mean_abs_42d_jerk_v074_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_42d_jerk_v075_signal, f06cb_f06_candle_body_ratios_body_level_63d_jerk_v076_signal, f06cb_f06_candle_body_ratios_body_mean_63d_jerk_v077_signal, f06cb_f06_candle_body_ratios_body_std_63d_jerk_v078_signal, f06cb_f06_candle_body_ratios_body_zscore_63d_jerk_v079_signal, f06cb_f06_candle_body_ratios_body_delta_63d_jerk_v080_signal, f06cb_f06_candle_body_ratios_body_pctdelta_63d_jerk_v081_signal, f06cb_f06_candle_body_ratios_body_upper_gap_63d_jerk_v082_signal, f06cb_f06_candle_body_ratios_body_lower_gap_63d_jerk_v083_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_63d_jerk_v084_signal, f06cb_f06_candle_body_ratios_body_energy_63d_jerk_v085_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_63d_jerk_v086_signal, f06cb_f06_candle_body_ratios_body_tail_relief_63d_jerk_v087_signal, f06cb_f06_candle_body_ratios_body_peak_fade_63d_jerk_v088_signal, f06cb_f06_candle_body_ratios_body_mean_abs_63d_jerk_v089_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_63d_jerk_v090_signal, f06cb_f06_candle_body_ratios_body_level_84d_jerk_v091_signal, f06cb_f06_candle_body_ratios_body_mean_84d_jerk_v092_signal, f06cb_f06_candle_body_ratios_body_std_84d_jerk_v093_signal, f06cb_f06_candle_body_ratios_body_zscore_84d_jerk_v094_signal, f06cb_f06_candle_body_ratios_body_delta_84d_jerk_v095_signal, f06cb_f06_candle_body_ratios_body_pctdelta_84d_jerk_v096_signal, f06cb_f06_candle_body_ratios_body_upper_gap_84d_jerk_v097_signal, f06cb_f06_candle_body_ratios_body_lower_gap_84d_jerk_v098_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_84d_jerk_v099_signal, f06cb_f06_candle_body_ratios_body_energy_84d_jerk_v100_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_84d_jerk_v101_signal, f06cb_f06_candle_body_ratios_body_tail_relief_84d_jerk_v102_signal, f06cb_f06_candle_body_ratios_body_peak_fade_84d_jerk_v103_signal, f06cb_f06_candle_body_ratios_body_mean_abs_84d_jerk_v104_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_84d_jerk_v105_signal, f06cb_f06_candle_body_ratios_body_level_126d_jerk_v106_signal, f06cb_f06_candle_body_ratios_body_mean_126d_jerk_v107_signal, f06cb_f06_candle_body_ratios_body_std_126d_jerk_v108_signal, f06cb_f06_candle_body_ratios_body_zscore_126d_jerk_v109_signal, f06cb_f06_candle_body_ratios_body_delta_126d_jerk_v110_signal, f06cb_f06_candle_body_ratios_body_pctdelta_126d_jerk_v111_signal, f06cb_f06_candle_body_ratios_body_upper_gap_126d_jerk_v112_signal, f06cb_f06_candle_body_ratios_body_lower_gap_126d_jerk_v113_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_126d_jerk_v114_signal, f06cb_f06_candle_body_ratios_body_energy_126d_jerk_v115_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_126d_jerk_v116_signal, f06cb_f06_candle_body_ratios_body_tail_relief_126d_jerk_v117_signal, f06cb_f06_candle_body_ratios_body_peak_fade_126d_jerk_v118_signal, f06cb_f06_candle_body_ratios_body_mean_abs_126d_jerk_v119_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_126d_jerk_v120_signal, f06cb_f06_candle_body_ratios_body_level_252d_jerk_v121_signal, f06cb_f06_candle_body_ratios_body_mean_252d_jerk_v122_signal, f06cb_f06_candle_body_ratios_body_std_252d_jerk_v123_signal, f06cb_f06_candle_body_ratios_body_zscore_252d_jerk_v124_signal, f06cb_f06_candle_body_ratios_body_delta_252d_jerk_v125_signal, f06cb_f06_candle_body_ratios_body_pctdelta_252d_jerk_v126_signal, f06cb_f06_candle_body_ratios_body_upper_gap_252d_jerk_v127_signal, f06cb_f06_candle_body_ratios_body_lower_gap_252d_jerk_v128_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_252d_jerk_v129_signal, f06cb_f06_candle_body_ratios_body_energy_252d_jerk_v130_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_252d_jerk_v131_signal, f06cb_f06_candle_body_ratios_body_tail_relief_252d_jerk_v132_signal, f06cb_f06_candle_body_ratios_body_peak_fade_252d_jerk_v133_signal, f06cb_f06_candle_body_ratios_body_mean_abs_252d_jerk_v134_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_252d_jerk_v135_signal, f06cb_f06_candle_body_ratios_body_level_504d_jerk_v136_signal, f06cb_f06_candle_body_ratios_body_mean_504d_jerk_v137_signal, f06cb_f06_candle_body_ratios_body_std_504d_jerk_v138_signal, f06cb_f06_candle_body_ratios_body_zscore_504d_jerk_v139_signal, f06cb_f06_candle_body_ratios_body_delta_504d_jerk_v140_signal, f06cb_f06_candle_body_ratios_body_pctdelta_504d_jerk_v141_signal, f06cb_f06_candle_body_ratios_body_upper_gap_504d_jerk_v142_signal, f06cb_f06_candle_body_ratios_body_lower_gap_504d_jerk_v143_signal, f06cb_f06_candle_body_ratios_body_short_mean_gap_504d_jerk_v144_signal, f06cb_f06_candle_body_ratios_body_energy_504d_jerk_v145_signal, f06cb_f06_candle_body_ratios_body_ewm_gap_504d_jerk_v146_signal, f06cb_f06_candle_body_ratios_body_tail_relief_504d_jerk_v147_signal, f06cb_f06_candle_body_ratios_body_peak_fade_504d_jerk_v148_signal, f06cb_f06_candle_body_ratios_body_mean_abs_504d_jerk_v149_signal, f06cb_f06_candle_body_ratios_body_vol_adj_delta_504d_jerk_v150_signal]}
F06_CANDLE_BODY_RATIOS_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    open = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    high = pd.concat([open, close], axis=1).max(axis=1) * (1.0 + pd.Series(np.random.uniform(0.003, 0.05, n)))
    low = pd.concat([open, close], axis=1).min(axis=1) * (1.0 - pd.Series(np.random.uniform(0.003, 0.05, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(open, high, low, close)
        y2 = func(open, high, low, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_candle_body_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
