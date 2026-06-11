import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _candle_sequence_pressure(open, close, w):
    body = (close - open) / open.abs().replace(0, np.nan)
    return body.ewm(span=max(2, w), adjust=False, min_periods=2).mean()

# sl5 5d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_5d_slope_v001_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_5d_slope_v002_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_5d_slope_v003_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_5d_slope_v004_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = _z(sig, 5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_5d_slope_v005_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_5d_slope_v006_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_5d_slope_v007_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_5d_slope_v008_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_5d_slope_v009_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_5d_slope_v010_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_5d_slope_v011_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_5d_slope_v012_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_5d_slope_v013_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_5d_slope_v014_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_5d_slope_v015_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_10d_slope_v016_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_10d_slope_v017_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_10d_slope_v018_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_10d_slope_v019_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = _z(sig, 10)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_10d_slope_v020_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_10d_slope_v021_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_10d_slope_v022_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_10d_slope_v023_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_10d_slope_v024_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_10d_slope_v025_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_10d_slope_v026_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_10d_slope_v027_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_10d_slope_v028_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_10d_slope_v029_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_10d_slope_v030_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_15d_slope_v031_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_15d_slope_v032_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_15d_slope_v033_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_15d_slope_v034_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = _z(sig, 15)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_15d_slope_v035_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_15d_slope_v036_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_15d_slope_v037_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_15d_slope_v038_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_15d_slope_v039_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_15d_slope_v040_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_15d_slope_v041_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_15d_slope_v042_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_15d_slope_v043_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_15d_slope_v044_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_15d_slope_v045_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_21d_slope_v046_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_21d_slope_v047_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_21d_slope_v048_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_21d_slope_v049_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = _z(sig, 21)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_21d_slope_v050_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_21d_slope_v051_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_21d_slope_v052_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_21d_slope_v053_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_21d_slope_v054_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_21d_slope_v055_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_21d_slope_v056_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_21d_slope_v057_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_21d_slope_v058_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_21d_slope_v059_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_21d_slope_v060_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_42d_slope_v061_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_42d_slope_v062_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_42d_slope_v063_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_42d_slope_v064_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = _z(sig, 42)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_42d_slope_v065_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_42d_slope_v066_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_42d_slope_v067_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_42d_slope_v068_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_42d_slope_v069_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_42d_slope_v070_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_42d_slope_v071_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_42d_slope_v072_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_42d_slope_v073_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_42d_slope_v074_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_42d_slope_v075_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_63d_slope_v076_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_63d_slope_v077_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_63d_slope_v078_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_63d_slope_v079_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = _z(sig, 63)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_63d_slope_v080_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_63d_slope_v081_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_63d_slope_v082_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_63d_slope_v083_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_63d_slope_v084_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_63d_slope_v085_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_63d_slope_v086_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_63d_slope_v087_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_63d_slope_v088_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_63d_slope_v089_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_63d_slope_v090_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_84d_slope_v091_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_84d_slope_v092_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_84d_slope_v093_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_84d_slope_v094_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = _z(sig, 84)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_84d_slope_v095_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_84d_slope_v096_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_84d_slope_v097_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_84d_slope_v098_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_84d_slope_v099_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_84d_slope_v100_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_84d_slope_v101_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_84d_slope_v102_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_84d_slope_v103_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_84d_slope_v104_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_84d_slope_v105_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_126d_slope_v106_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_126d_slope_v107_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_126d_slope_v108_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_126d_slope_v109_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = _z(sig, 126)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_126d_slope_v110_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_126d_slope_v111_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_126d_slope_v112_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_126d_slope_v113_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_126d_slope_v114_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_126d_slope_v115_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_126d_slope_v116_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_126d_slope_v117_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_126d_slope_v118_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_126d_slope_v119_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_126d_slope_v120_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_252d_slope_v121_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_252d_slope_v122_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_252d_slope_v123_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_252d_slope_v124_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = _z(sig, 252)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_252d_slope_v125_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_252d_slope_v126_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_252d_slope_v127_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_252d_slope_v128_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_252d_slope_v129_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_252d_slope_v130_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_252d_slope_v131_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_252d_slope_v132_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_252d_slope_v133_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_252d_slope_v134_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_252d_slope_v135_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d level seq
def f10cs_f10_candle_sequence_patterns_seq_level_504d_slope_v136_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d mean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_504d_slope_v137_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d var seq
def f10cs_f10_candle_sequence_patterns_seq_std_504d_slope_v138_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d zscore seq
def f10cs_f10_candle_sequence_patterns_seq_zscore_504d_slope_v139_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = _z(sig, 504)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d change seq
def f10cs_f10_candle_sequence_patterns_seq_delta_504d_slope_v140_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d relchg seq
def f10cs_f10_candle_sequence_patterns_seq_pctdelta_504d_slope_v141_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q75gap seq
def f10cs_f10_candle_sequence_patterns_seq_upper_gap_504d_slope_v142_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q25gap seq
def f10cs_f10_candle_sequence_patterns_seq_lower_gap_504d_slope_v143_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d smean gap seq
def f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_504d_slope_v144_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d energy seq
def f10cs_f10_candle_sequence_patterns_seq_energy_504d_slope_v145_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d ewm gap seq
def f10cs_f10_candle_sequence_patterns_seq_ewm_gap_504d_slope_v146_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d tail relief seq
def f10cs_f10_candle_sequence_patterns_seq_tail_relief_504d_slope_v147_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d peak fade seq
def f10cs_f10_candle_sequence_patterns_seq_peak_fade_504d_slope_v148_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d absmean seq
def f10cs_f10_candle_sequence_patterns_seq_mean_abs_504d_slope_v149_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d voladj chg seq
def f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_504d_slope_v150_signal(open, close):
    sig = _candle_sequence_pressure(open, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['open', 'close'], "func": fn} for fn in [f10cs_f10_candle_sequence_patterns_seq_level_5d_slope_v001_signal, f10cs_f10_candle_sequence_patterns_seq_mean_5d_slope_v002_signal, f10cs_f10_candle_sequence_patterns_seq_std_5d_slope_v003_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_5d_slope_v004_signal, f10cs_f10_candle_sequence_patterns_seq_delta_5d_slope_v005_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_5d_slope_v006_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_5d_slope_v007_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_5d_slope_v008_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_5d_slope_v009_signal, f10cs_f10_candle_sequence_patterns_seq_energy_5d_slope_v010_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_5d_slope_v011_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_5d_slope_v012_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_5d_slope_v013_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_5d_slope_v014_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_5d_slope_v015_signal, f10cs_f10_candle_sequence_patterns_seq_level_10d_slope_v016_signal, f10cs_f10_candle_sequence_patterns_seq_mean_10d_slope_v017_signal, f10cs_f10_candle_sequence_patterns_seq_std_10d_slope_v018_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_10d_slope_v019_signal, f10cs_f10_candle_sequence_patterns_seq_delta_10d_slope_v020_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_10d_slope_v021_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_10d_slope_v022_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_10d_slope_v023_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_10d_slope_v024_signal, f10cs_f10_candle_sequence_patterns_seq_energy_10d_slope_v025_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_10d_slope_v026_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_10d_slope_v027_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_10d_slope_v028_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_10d_slope_v029_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_10d_slope_v030_signal, f10cs_f10_candle_sequence_patterns_seq_level_15d_slope_v031_signal, f10cs_f10_candle_sequence_patterns_seq_mean_15d_slope_v032_signal, f10cs_f10_candle_sequence_patterns_seq_std_15d_slope_v033_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_15d_slope_v034_signal, f10cs_f10_candle_sequence_patterns_seq_delta_15d_slope_v035_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_15d_slope_v036_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_15d_slope_v037_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_15d_slope_v038_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_15d_slope_v039_signal, f10cs_f10_candle_sequence_patterns_seq_energy_15d_slope_v040_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_15d_slope_v041_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_15d_slope_v042_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_15d_slope_v043_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_15d_slope_v044_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_15d_slope_v045_signal, f10cs_f10_candle_sequence_patterns_seq_level_21d_slope_v046_signal, f10cs_f10_candle_sequence_patterns_seq_mean_21d_slope_v047_signal, f10cs_f10_candle_sequence_patterns_seq_std_21d_slope_v048_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_21d_slope_v049_signal, f10cs_f10_candle_sequence_patterns_seq_delta_21d_slope_v050_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_21d_slope_v051_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_21d_slope_v052_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_21d_slope_v053_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_21d_slope_v054_signal, f10cs_f10_candle_sequence_patterns_seq_energy_21d_slope_v055_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_21d_slope_v056_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_21d_slope_v057_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_21d_slope_v058_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_21d_slope_v059_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_21d_slope_v060_signal, f10cs_f10_candle_sequence_patterns_seq_level_42d_slope_v061_signal, f10cs_f10_candle_sequence_patterns_seq_mean_42d_slope_v062_signal, f10cs_f10_candle_sequence_patterns_seq_std_42d_slope_v063_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_42d_slope_v064_signal, f10cs_f10_candle_sequence_patterns_seq_delta_42d_slope_v065_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_42d_slope_v066_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_42d_slope_v067_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_42d_slope_v068_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_42d_slope_v069_signal, f10cs_f10_candle_sequence_patterns_seq_energy_42d_slope_v070_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_42d_slope_v071_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_42d_slope_v072_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_42d_slope_v073_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_42d_slope_v074_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_42d_slope_v075_signal, f10cs_f10_candle_sequence_patterns_seq_level_63d_slope_v076_signal, f10cs_f10_candle_sequence_patterns_seq_mean_63d_slope_v077_signal, f10cs_f10_candle_sequence_patterns_seq_std_63d_slope_v078_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_63d_slope_v079_signal, f10cs_f10_candle_sequence_patterns_seq_delta_63d_slope_v080_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_63d_slope_v081_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_63d_slope_v082_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_63d_slope_v083_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_63d_slope_v084_signal, f10cs_f10_candle_sequence_patterns_seq_energy_63d_slope_v085_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_63d_slope_v086_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_63d_slope_v087_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_63d_slope_v088_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_63d_slope_v089_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_63d_slope_v090_signal, f10cs_f10_candle_sequence_patterns_seq_level_84d_slope_v091_signal, f10cs_f10_candle_sequence_patterns_seq_mean_84d_slope_v092_signal, f10cs_f10_candle_sequence_patterns_seq_std_84d_slope_v093_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_84d_slope_v094_signal, f10cs_f10_candle_sequence_patterns_seq_delta_84d_slope_v095_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_84d_slope_v096_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_84d_slope_v097_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_84d_slope_v098_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_84d_slope_v099_signal, f10cs_f10_candle_sequence_patterns_seq_energy_84d_slope_v100_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_84d_slope_v101_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_84d_slope_v102_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_84d_slope_v103_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_84d_slope_v104_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_84d_slope_v105_signal, f10cs_f10_candle_sequence_patterns_seq_level_126d_slope_v106_signal, f10cs_f10_candle_sequence_patterns_seq_mean_126d_slope_v107_signal, f10cs_f10_candle_sequence_patterns_seq_std_126d_slope_v108_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_126d_slope_v109_signal, f10cs_f10_candle_sequence_patterns_seq_delta_126d_slope_v110_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_126d_slope_v111_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_126d_slope_v112_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_126d_slope_v113_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_126d_slope_v114_signal, f10cs_f10_candle_sequence_patterns_seq_energy_126d_slope_v115_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_126d_slope_v116_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_126d_slope_v117_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_126d_slope_v118_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_126d_slope_v119_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_126d_slope_v120_signal, f10cs_f10_candle_sequence_patterns_seq_level_252d_slope_v121_signal, f10cs_f10_candle_sequence_patterns_seq_mean_252d_slope_v122_signal, f10cs_f10_candle_sequence_patterns_seq_std_252d_slope_v123_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_252d_slope_v124_signal, f10cs_f10_candle_sequence_patterns_seq_delta_252d_slope_v125_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_252d_slope_v126_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_252d_slope_v127_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_252d_slope_v128_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_252d_slope_v129_signal, f10cs_f10_candle_sequence_patterns_seq_energy_252d_slope_v130_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_252d_slope_v131_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_252d_slope_v132_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_252d_slope_v133_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_252d_slope_v134_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_252d_slope_v135_signal, f10cs_f10_candle_sequence_patterns_seq_level_504d_slope_v136_signal, f10cs_f10_candle_sequence_patterns_seq_mean_504d_slope_v137_signal, f10cs_f10_candle_sequence_patterns_seq_std_504d_slope_v138_signal, f10cs_f10_candle_sequence_patterns_seq_zscore_504d_slope_v139_signal, f10cs_f10_candle_sequence_patterns_seq_delta_504d_slope_v140_signal, f10cs_f10_candle_sequence_patterns_seq_pctdelta_504d_slope_v141_signal, f10cs_f10_candle_sequence_patterns_seq_upper_gap_504d_slope_v142_signal, f10cs_f10_candle_sequence_patterns_seq_lower_gap_504d_slope_v143_signal, f10cs_f10_candle_sequence_patterns_seq_short_mean_gap_504d_slope_v144_signal, f10cs_f10_candle_sequence_patterns_seq_energy_504d_slope_v145_signal, f10cs_f10_candle_sequence_patterns_seq_ewm_gap_504d_slope_v146_signal, f10cs_f10_candle_sequence_patterns_seq_tail_relief_504d_slope_v147_signal, f10cs_f10_candle_sequence_patterns_seq_peak_fade_504d_slope_v148_signal, f10cs_f10_candle_sequence_patterns_seq_mean_abs_504d_slope_v149_signal, f10cs_f10_candle_sequence_patterns_seq_vol_adj_delta_504d_slope_v150_signal]}
F10_CANDLE_SEQUENCE_PATTERNS_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    open = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(open, close)
        y2 = func(open, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_candle_sequence_pressure" in src
    assert ok_nan >= int(0.80 * len(funcs))
