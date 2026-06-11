import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _high_low_range_ratio(high, low, close, w):
    rng = (high - low) / close.abs().replace(0, np.nan)
    return rng.rolling(w, min_periods=2).mean() + rng.diff(max(1, w//5))

# sl5 5d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_5d_slope_v001_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_5d_slope_v002_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_5d_slope_v003_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_5d_slope_v004_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = _z(sig, 5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_5d_slope_v005_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_5d_slope_v006_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_5d_slope_v007_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_5d_slope_v008_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_5d_slope_v009_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_5d_slope_v010_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_5d_slope_v011_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_5d_slope_v012_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_5d_slope_v013_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_5d_slope_v014_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_5d_slope_v015_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_10d_slope_v016_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_10d_slope_v017_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_10d_slope_v018_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_10d_slope_v019_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = _z(sig, 10)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_10d_slope_v020_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_10d_slope_v021_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_10d_slope_v022_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_10d_slope_v023_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_10d_slope_v024_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_10d_slope_v025_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_10d_slope_v026_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_10d_slope_v027_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_10d_slope_v028_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_10d_slope_v029_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_10d_slope_v030_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_15d_slope_v031_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_15d_slope_v032_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_15d_slope_v033_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_15d_slope_v034_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = _z(sig, 15)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_15d_slope_v035_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_15d_slope_v036_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_15d_slope_v037_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_15d_slope_v038_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_15d_slope_v039_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_15d_slope_v040_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_15d_slope_v041_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_15d_slope_v042_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_15d_slope_v043_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_15d_slope_v044_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_15d_slope_v045_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_21d_slope_v046_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_21d_slope_v047_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_21d_slope_v048_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_21d_slope_v049_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = _z(sig, 21)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_21d_slope_v050_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_21d_slope_v051_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_21d_slope_v052_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_21d_slope_v053_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_21d_slope_v054_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_21d_slope_v055_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_21d_slope_v056_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_21d_slope_v057_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_21d_slope_v058_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_21d_slope_v059_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_21d_slope_v060_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_42d_slope_v061_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_42d_slope_v062_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_42d_slope_v063_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_42d_slope_v064_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = _z(sig, 42)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_42d_slope_v065_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_42d_slope_v066_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_42d_slope_v067_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_42d_slope_v068_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_42d_slope_v069_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_42d_slope_v070_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_42d_slope_v071_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_42d_slope_v072_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_42d_slope_v073_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_42d_slope_v074_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_42d_slope_v075_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_63d_slope_v076_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_63d_slope_v077_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_63d_slope_v078_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_63d_slope_v079_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = _z(sig, 63)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_63d_slope_v080_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_63d_slope_v081_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_63d_slope_v082_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_63d_slope_v083_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_63d_slope_v084_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_63d_slope_v085_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_63d_slope_v086_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_63d_slope_v087_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_63d_slope_v088_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_63d_slope_v089_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_63d_slope_v090_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_84d_slope_v091_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_84d_slope_v092_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_84d_slope_v093_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_84d_slope_v094_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = _z(sig, 84)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_84d_slope_v095_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_84d_slope_v096_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_84d_slope_v097_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_84d_slope_v098_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_84d_slope_v099_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_84d_slope_v100_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_84d_slope_v101_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_84d_slope_v102_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_84d_slope_v103_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_84d_slope_v104_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_84d_slope_v105_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_126d_slope_v106_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_126d_slope_v107_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_126d_slope_v108_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_126d_slope_v109_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = _z(sig, 126)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_126d_slope_v110_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_126d_slope_v111_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_126d_slope_v112_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_126d_slope_v113_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_126d_slope_v114_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_126d_slope_v115_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_126d_slope_v116_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_126d_slope_v117_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_126d_slope_v118_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_126d_slope_v119_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_126d_slope_v120_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_252d_slope_v121_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_252d_slope_v122_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_252d_slope_v123_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_252d_slope_v124_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = _z(sig, 252)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_252d_slope_v125_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_252d_slope_v126_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_252d_slope_v127_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_252d_slope_v128_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_252d_slope_v129_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_252d_slope_v130_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_252d_slope_v131_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_252d_slope_v132_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_252d_slope_v133_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_252d_slope_v134_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_252d_slope_v135_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_504d_slope_v136_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_504d_slope_v137_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_504d_slope_v138_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_504d_slope_v139_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = _z(sig, 504)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_504d_slope_v140_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d relchg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_504d_slope_v141_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_504d_slope_v142_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_504d_slope_v143_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_504d_slope_v144_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_504d_slope_v145_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_504d_slope_v146_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_504d_slope_v147_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_504d_slope_v148_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_504d_slope_v149_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_504d_slope_v150_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'close'], "func": fn} for fn in [f08hl_f08_high_low_range_dynamics_hlrng_level_5d_slope_v001_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_5d_slope_v002_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_5d_slope_v003_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_5d_slope_v004_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_5d_slope_v005_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_5d_slope_v006_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_5d_slope_v007_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_5d_slope_v008_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_5d_slope_v009_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_5d_slope_v010_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_5d_slope_v011_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_5d_slope_v012_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_5d_slope_v013_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_5d_slope_v014_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_5d_slope_v015_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_10d_slope_v016_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_10d_slope_v017_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_10d_slope_v018_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_10d_slope_v019_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_10d_slope_v020_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_10d_slope_v021_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_10d_slope_v022_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_10d_slope_v023_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_10d_slope_v024_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_10d_slope_v025_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_10d_slope_v026_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_10d_slope_v027_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_10d_slope_v028_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_10d_slope_v029_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_10d_slope_v030_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_15d_slope_v031_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_15d_slope_v032_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_15d_slope_v033_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_15d_slope_v034_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_15d_slope_v035_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_15d_slope_v036_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_15d_slope_v037_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_15d_slope_v038_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_15d_slope_v039_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_15d_slope_v040_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_15d_slope_v041_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_15d_slope_v042_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_15d_slope_v043_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_15d_slope_v044_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_15d_slope_v045_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_21d_slope_v046_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_21d_slope_v047_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_21d_slope_v048_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_21d_slope_v049_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_21d_slope_v050_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_21d_slope_v051_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_21d_slope_v052_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_21d_slope_v053_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_21d_slope_v054_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_21d_slope_v055_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_21d_slope_v056_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_21d_slope_v057_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_21d_slope_v058_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_21d_slope_v059_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_21d_slope_v060_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_42d_slope_v061_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_42d_slope_v062_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_42d_slope_v063_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_42d_slope_v064_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_42d_slope_v065_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_42d_slope_v066_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_42d_slope_v067_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_42d_slope_v068_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_42d_slope_v069_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_42d_slope_v070_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_42d_slope_v071_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_42d_slope_v072_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_42d_slope_v073_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_42d_slope_v074_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_42d_slope_v075_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_63d_slope_v076_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_63d_slope_v077_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_63d_slope_v078_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_63d_slope_v079_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_63d_slope_v080_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_63d_slope_v081_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_63d_slope_v082_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_63d_slope_v083_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_63d_slope_v084_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_63d_slope_v085_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_63d_slope_v086_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_63d_slope_v087_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_63d_slope_v088_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_63d_slope_v089_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_63d_slope_v090_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_84d_slope_v091_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_84d_slope_v092_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_84d_slope_v093_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_84d_slope_v094_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_84d_slope_v095_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_84d_slope_v096_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_84d_slope_v097_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_84d_slope_v098_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_84d_slope_v099_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_84d_slope_v100_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_84d_slope_v101_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_84d_slope_v102_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_84d_slope_v103_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_84d_slope_v104_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_84d_slope_v105_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_126d_slope_v106_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_126d_slope_v107_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_126d_slope_v108_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_126d_slope_v109_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_126d_slope_v110_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_126d_slope_v111_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_126d_slope_v112_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_126d_slope_v113_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_126d_slope_v114_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_126d_slope_v115_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_126d_slope_v116_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_126d_slope_v117_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_126d_slope_v118_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_126d_slope_v119_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_126d_slope_v120_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_252d_slope_v121_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_252d_slope_v122_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_252d_slope_v123_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_252d_slope_v124_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_252d_slope_v125_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_252d_slope_v126_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_252d_slope_v127_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_252d_slope_v128_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_252d_slope_v129_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_252d_slope_v130_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_252d_slope_v131_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_252d_slope_v132_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_252d_slope_v133_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_252d_slope_v134_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_252d_slope_v135_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_504d_slope_v136_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_504d_slope_v137_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_504d_slope_v138_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_504d_slope_v139_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_504d_slope_v140_signal, f08hl_f08_high_low_range_dynamics_hlrng_pctdelta_504d_slope_v141_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_504d_slope_v142_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_504d_slope_v143_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_504d_slope_v144_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_504d_slope_v145_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_504d_slope_v146_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_504d_slope_v147_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_504d_slope_v148_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_504d_slope_v149_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_504d_slope_v150_signal]}
F08_HIGH_LOW_RANGE_DYNAMICS_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    high = close * (1.0 + pd.Series(np.random.uniform(0.003, 0.05, n)))
    low = close * (1.0 - pd.Series(np.random.uniform(0.003, 0.05, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(high, low, close)
        y2 = func(high, low, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_high_low_range_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
