# f07_price_moving_averages_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _ma_sma(c, w):
    return c.rolling(w, min_periods=1).mean()

def _ma_ema(c, w):
    return c.ewm(span=w, adjust=False).mean()

# f07_price_moving_averages_open_sma_2d
def f07_price_moving_averages_open_sma_2d_base_v001_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_2d
def f07_price_moving_averages_open_ema_2d_base_v002_signal(arg_open):
    res = arg_open / _ma_ema(arg_open, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_rel_2d
def f07_price_moving_averages_open_sma_rel_2d_base_v003_signal(arg_open, arg_close):
    res = _ma_sma(arg_open, 2) / _ma_sma(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_rel_2d
def f07_price_moving_averages_open_ema_rel_2d_base_v004_signal(arg_open, arg_close):
    res = _ma_ema(arg_open, 2) / _ma_ema(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_bb_pct_2d
def f07_price_moving_averages_open_bb_pct_2d_base_v005_signal(arg_open):
    res = (arg_open - (_ma_sma(arg_open, 2) - 2 * arg_open.rolling(2).std())) / (4 * arg_open.rolling(2).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_zscore_2d
def f07_price_moving_averages_open_zscore_2d_base_v006_signal(arg_open):
    res = (arg_open - _ma_sma(arg_open, 2)) / arg_open.rolling(2).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_max_2d
def f07_price_moving_averages_open_sma_dist_max_2d_base_v007_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 2).rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_min_2d
def f07_price_moving_averages_open_sma_dist_min_2d_base_v008_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 2).rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_2d
def f07_price_moving_averages_high_sma_2d_base_v009_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_ema_2d
def f07_price_moving_averages_high_ema_2d_base_v010_signal(arg_high):
    res = arg_high / _ma_ema(arg_high, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_rel_2d
def f07_price_moving_averages_high_sma_rel_2d_base_v011_signal(arg_high, arg_close):
    res = _ma_sma(arg_high, 2) / _ma_sma(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_ema_rel_2d
def f07_price_moving_averages_high_ema_rel_2d_base_v012_signal(arg_high, arg_close):
    res = _ma_ema(arg_high, 2) / _ma_ema(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_bb_pct_2d
def f07_price_moving_averages_high_bb_pct_2d_base_v013_signal(arg_high):
    res = (arg_high - (_ma_sma(arg_high, 2) - 2 * arg_high.rolling(2).std())) / (4 * arg_high.rolling(2).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_zscore_2d
def f07_price_moving_averages_high_zscore_2d_base_v014_signal(arg_high):
    res = (arg_high - _ma_sma(arg_high, 2)) / arg_high.rolling(2).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_max_2d
def f07_price_moving_averages_high_sma_dist_max_2d_base_v015_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 2).rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_min_2d
def f07_price_moving_averages_high_sma_dist_min_2d_base_v016_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 2).rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_2d
def f07_price_moving_averages_low_sma_2d_base_v017_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_2d
def f07_price_moving_averages_low_ema_2d_base_v018_signal(arg_low):
    res = arg_low / _ma_ema(arg_low, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_rel_2d
def f07_price_moving_averages_low_sma_rel_2d_base_v019_signal(arg_low, arg_close):
    res = _ma_sma(arg_low, 2) / _ma_sma(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_rel_2d
def f07_price_moving_averages_low_ema_rel_2d_base_v020_signal(arg_low, arg_close):
    res = _ma_ema(arg_low, 2) / _ma_ema(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_bb_pct_2d
def f07_price_moving_averages_low_bb_pct_2d_base_v021_signal(arg_low):
    res = (arg_low - (_ma_sma(arg_low, 2) - 2 * arg_low.rolling(2).std())) / (4 * arg_low.rolling(2).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_zscore_2d
def f07_price_moving_averages_low_zscore_2d_base_v022_signal(arg_low):
    res = (arg_low - _ma_sma(arg_low, 2)) / arg_low.rolling(2).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_max_2d
def f07_price_moving_averages_low_sma_dist_max_2d_base_v023_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 2).rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_min_2d
def f07_price_moving_averages_low_sma_dist_min_2d_base_v024_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 2).rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_2d
def f07_price_moving_averages_close_sma_2d_base_v025_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_2d
def f07_price_moving_averages_close_ema_2d_base_v026_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_2d
def f07_price_moving_averages_close_sma_rel_2d_base_v027_signal(arg_close):
    res = _ma_sma(arg_close, 2) / _ma_sma(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_2d
def f07_price_moving_averages_close_ema_rel_2d_base_v028_signal(arg_close):
    res = _ma_ema(arg_close, 2) / _ma_ema(arg_close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_2d
def f07_price_moving_averages_close_bb_pct_2d_base_v029_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 2) - 2 * arg_close.rolling(2).std())) / (4 * arg_close.rolling(2).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_2d
def f07_price_moving_averages_close_zscore_2d_base_v030_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 2)) / arg_close.rolling(2).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_2d
def f07_price_moving_averages_close_sma_dist_max_2d_base_v031_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 2).rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_2d
def f07_price_moving_averages_close_sma_dist_min_2d_base_v032_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 2).rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_3d
def f07_price_moving_averages_open_sma_3d_base_v033_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_3d
def f07_price_moving_averages_open_ema_3d_base_v034_signal(arg_open):
    res = arg_open / _ma_ema(arg_open, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_rel_3d
def f07_price_moving_averages_open_sma_rel_3d_base_v035_signal(arg_open, arg_close):
    res = _ma_sma(arg_open, 3) / _ma_sma(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_rel_3d
def f07_price_moving_averages_open_ema_rel_3d_base_v036_signal(arg_open, arg_close):
    res = _ma_ema(arg_open, 3) / _ma_ema(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_bb_pct_3d
def f07_price_moving_averages_open_bb_pct_3d_base_v037_signal(arg_open):
    res = (arg_open - (_ma_sma(arg_open, 3) - 2 * arg_open.rolling(3).std())) / (4 * arg_open.rolling(3).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_zscore_3d
def f07_price_moving_averages_open_zscore_3d_base_v038_signal(arg_open):
    res = (arg_open - _ma_sma(arg_open, 3)) / arg_open.rolling(3).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_max_3d
def f07_price_moving_averages_open_sma_dist_max_3d_base_v039_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 3).rolling(15).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_min_3d
def f07_price_moving_averages_open_sma_dist_min_3d_base_v040_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 3).rolling(15).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_3d
def f07_price_moving_averages_high_sma_3d_base_v041_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_ema_3d
def f07_price_moving_averages_high_ema_3d_base_v042_signal(arg_high):
    res = arg_high / _ma_ema(arg_high, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_rel_3d
def f07_price_moving_averages_high_sma_rel_3d_base_v043_signal(arg_high, arg_close):
    res = _ma_sma(arg_high, 3) / _ma_sma(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_ema_rel_3d
def f07_price_moving_averages_high_ema_rel_3d_base_v044_signal(arg_high, arg_close):
    res = _ma_ema(arg_high, 3) / _ma_ema(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_bb_pct_3d
def f07_price_moving_averages_high_bb_pct_3d_base_v045_signal(arg_high):
    res = (arg_high - (_ma_sma(arg_high, 3) - 2 * arg_high.rolling(3).std())) / (4 * arg_high.rolling(3).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_zscore_3d
def f07_price_moving_averages_high_zscore_3d_base_v046_signal(arg_high):
    res = (arg_high - _ma_sma(arg_high, 3)) / arg_high.rolling(3).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_max_3d
def f07_price_moving_averages_high_sma_dist_max_3d_base_v047_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 3).rolling(15).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_min_3d
def f07_price_moving_averages_high_sma_dist_min_3d_base_v048_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 3).rolling(15).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_3d
def f07_price_moving_averages_low_sma_3d_base_v049_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_3d
def f07_price_moving_averages_low_ema_3d_base_v050_signal(arg_low):
    res = arg_low / _ma_ema(arg_low, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_rel_3d
def f07_price_moving_averages_low_sma_rel_3d_base_v051_signal(arg_low, arg_close):
    res = _ma_sma(arg_low, 3) / _ma_sma(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_rel_3d
def f07_price_moving_averages_low_ema_rel_3d_base_v052_signal(arg_low, arg_close):
    res = _ma_ema(arg_low, 3) / _ma_ema(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_bb_pct_3d
def f07_price_moving_averages_low_bb_pct_3d_base_v053_signal(arg_low):
    res = (arg_low - (_ma_sma(arg_low, 3) - 2 * arg_low.rolling(3).std())) / (4 * arg_low.rolling(3).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_zscore_3d
def f07_price_moving_averages_low_zscore_3d_base_v054_signal(arg_low):
    res = (arg_low - _ma_sma(arg_low, 3)) / arg_low.rolling(3).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_max_3d
def f07_price_moving_averages_low_sma_dist_max_3d_base_v055_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 3).rolling(15).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_min_3d
def f07_price_moving_averages_low_sma_dist_min_3d_base_v056_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 3).rolling(15).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_3d
def f07_price_moving_averages_close_sma_3d_base_v057_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_3d
def f07_price_moving_averages_close_ema_3d_base_v058_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_3d
def f07_price_moving_averages_close_sma_rel_3d_base_v059_signal(arg_close):
    res = _ma_sma(arg_close, 3) / _ma_sma(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_3d
def f07_price_moving_averages_close_ema_rel_3d_base_v060_signal(arg_close):
    res = _ma_ema(arg_close, 3) / _ma_ema(arg_close, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_3d
def f07_price_moving_averages_close_bb_pct_3d_base_v061_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 3) - 2 * arg_close.rolling(3).std())) / (4 * arg_close.rolling(3).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_3d
def f07_price_moving_averages_close_zscore_3d_base_v062_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 3)) / arg_close.rolling(3).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_3d
def f07_price_moving_averages_close_sma_dist_max_3d_base_v063_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 3).rolling(15).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_3d
def f07_price_moving_averages_close_sma_dist_min_3d_base_v064_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 3).rolling(15).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_5d
def f07_price_moving_averages_open_sma_5d_base_v065_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_5d
def f07_price_moving_averages_open_ema_5d_base_v066_signal(arg_open):
    res = arg_open / _ma_ema(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_rel_5d
def f07_price_moving_averages_open_sma_rel_5d_base_v067_signal(arg_open, arg_close):
    res = _ma_sma(arg_open, 5) / _ma_sma(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_ema_rel_5d
def f07_price_moving_averages_open_ema_rel_5d_base_v068_signal(arg_open, arg_close):
    res = _ma_ema(arg_open, 5) / _ma_ema(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_bb_pct_5d
def f07_price_moving_averages_open_bb_pct_5d_base_v069_signal(arg_open):
    res = (arg_open - (_ma_sma(arg_open, 5) - 2 * arg_open.rolling(5).std())) / (4 * arg_open.rolling(5).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_zscore_5d
def f07_price_moving_averages_open_zscore_5d_base_v070_signal(arg_open):
    res = (arg_open - _ma_sma(arg_open, 5)) / arg_open.rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_max_5d
def f07_price_moving_averages_open_sma_dist_max_5d_base_v071_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 5).rolling(25).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_open_sma_dist_min_5d
def f07_price_moving_averages_open_sma_dist_min_5d_base_v072_signal(arg_open):
    res = arg_open / _ma_sma(arg_open, 5).rolling(25).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_5d
def f07_price_moving_averages_high_sma_5d_base_v073_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_ema_5d
def f07_price_moving_averages_high_ema_5d_base_v074_signal(arg_high):
    res = arg_high / _ma_ema(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_rel_5d
def f07_price_moving_averages_high_sma_rel_5d_base_v075_signal(arg_high, arg_close):
    res = _ma_sma(arg_high, 5) / _ma_sma(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    'f07_price_moving_averages_open_sma_2d_base_v001_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_2d_base_v001_signal},
    'f07_price_moving_averages_open_ema_2d_base_v002_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_2d_base_v002_signal},
    'f07_price_moving_averages_open_sma_rel_2d_base_v003_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_2d_base_v003_signal},
    'f07_price_moving_averages_open_ema_rel_2d_base_v004_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_2d_base_v004_signal},
    'f07_price_moving_averages_open_bb_pct_2d_base_v005_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_2d_base_v005_signal},
    'f07_price_moving_averages_open_zscore_2d_base_v006_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_2d_base_v006_signal},
    'f07_price_moving_averages_open_sma_dist_max_2d_base_v007_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_2d_base_v007_signal},
    'f07_price_moving_averages_open_sma_dist_min_2d_base_v008_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_2d_base_v008_signal},
    'f07_price_moving_averages_high_sma_2d_base_v009_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_2d_base_v009_signal},
    'f07_price_moving_averages_high_ema_2d_base_v010_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_2d_base_v010_signal},
    'f07_price_moving_averages_high_sma_rel_2d_base_v011_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_2d_base_v011_signal},
    'f07_price_moving_averages_high_ema_rel_2d_base_v012_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_2d_base_v012_signal},
    'f07_price_moving_averages_high_bb_pct_2d_base_v013_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_2d_base_v013_signal},
    'f07_price_moving_averages_high_zscore_2d_base_v014_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_2d_base_v014_signal},
    'f07_price_moving_averages_high_sma_dist_max_2d_base_v015_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_2d_base_v015_signal},
    'f07_price_moving_averages_high_sma_dist_min_2d_base_v016_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_2d_base_v016_signal},
    'f07_price_moving_averages_low_sma_2d_base_v017_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_2d_base_v017_signal},
    'f07_price_moving_averages_low_ema_2d_base_v018_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_2d_base_v018_signal},
    'f07_price_moving_averages_low_sma_rel_2d_base_v019_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_2d_base_v019_signal},
    'f07_price_moving_averages_low_ema_rel_2d_base_v020_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_2d_base_v020_signal},
    'f07_price_moving_averages_low_bb_pct_2d_base_v021_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_2d_base_v021_signal},
    'f07_price_moving_averages_low_zscore_2d_base_v022_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_2d_base_v022_signal},
    'f07_price_moving_averages_low_sma_dist_max_2d_base_v023_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_2d_base_v023_signal},
    'f07_price_moving_averages_low_sma_dist_min_2d_base_v024_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_2d_base_v024_signal},
    'f07_price_moving_averages_close_sma_2d_base_v025_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_2d_base_v025_signal},
    'f07_price_moving_averages_close_ema_2d_base_v026_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_2d_base_v026_signal},
    'f07_price_moving_averages_close_sma_rel_2d_base_v027_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_2d_base_v027_signal},
    'f07_price_moving_averages_close_ema_rel_2d_base_v028_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_2d_base_v028_signal},
    'f07_price_moving_averages_close_bb_pct_2d_base_v029_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_2d_base_v029_signal},
    'f07_price_moving_averages_close_zscore_2d_base_v030_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_2d_base_v030_signal},
    'f07_price_moving_averages_close_sma_dist_max_2d_base_v031_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_2d_base_v031_signal},
    'f07_price_moving_averages_close_sma_dist_min_2d_base_v032_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_2d_base_v032_signal},
    'f07_price_moving_averages_open_sma_3d_base_v033_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_3d_base_v033_signal},
    'f07_price_moving_averages_open_ema_3d_base_v034_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_3d_base_v034_signal},
    'f07_price_moving_averages_open_sma_rel_3d_base_v035_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_3d_base_v035_signal},
    'f07_price_moving_averages_open_ema_rel_3d_base_v036_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_3d_base_v036_signal},
    'f07_price_moving_averages_open_bb_pct_3d_base_v037_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_3d_base_v037_signal},
    'f07_price_moving_averages_open_zscore_3d_base_v038_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_3d_base_v038_signal},
    'f07_price_moving_averages_open_sma_dist_max_3d_base_v039_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_3d_base_v039_signal},
    'f07_price_moving_averages_open_sma_dist_min_3d_base_v040_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_3d_base_v040_signal},
    'f07_price_moving_averages_high_sma_3d_base_v041_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_3d_base_v041_signal},
    'f07_price_moving_averages_high_ema_3d_base_v042_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_3d_base_v042_signal},
    'f07_price_moving_averages_high_sma_rel_3d_base_v043_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_3d_base_v043_signal},
    'f07_price_moving_averages_high_ema_rel_3d_base_v044_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_3d_base_v044_signal},
    'f07_price_moving_averages_high_bb_pct_3d_base_v045_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_3d_base_v045_signal},
    'f07_price_moving_averages_high_zscore_3d_base_v046_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_3d_base_v046_signal},
    'f07_price_moving_averages_high_sma_dist_max_3d_base_v047_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_3d_base_v047_signal},
    'f07_price_moving_averages_high_sma_dist_min_3d_base_v048_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_3d_base_v048_signal},
    'f07_price_moving_averages_low_sma_3d_base_v049_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_3d_base_v049_signal},
    'f07_price_moving_averages_low_ema_3d_base_v050_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_3d_base_v050_signal},
    'f07_price_moving_averages_low_sma_rel_3d_base_v051_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_3d_base_v051_signal},
    'f07_price_moving_averages_low_ema_rel_3d_base_v052_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_3d_base_v052_signal},
    'f07_price_moving_averages_low_bb_pct_3d_base_v053_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_3d_base_v053_signal},
    'f07_price_moving_averages_low_zscore_3d_base_v054_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_3d_base_v054_signal},
    'f07_price_moving_averages_low_sma_dist_max_3d_base_v055_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_3d_base_v055_signal},
    'f07_price_moving_averages_low_sma_dist_min_3d_base_v056_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_3d_base_v056_signal},
    'f07_price_moving_averages_close_sma_3d_base_v057_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_3d_base_v057_signal},
    'f07_price_moving_averages_close_ema_3d_base_v058_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_3d_base_v058_signal},
    'f07_price_moving_averages_close_sma_rel_3d_base_v059_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_3d_base_v059_signal},
    'f07_price_moving_averages_close_ema_rel_3d_base_v060_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_3d_base_v060_signal},
    'f07_price_moving_averages_close_bb_pct_3d_base_v061_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_3d_base_v061_signal},
    'f07_price_moving_averages_close_zscore_3d_base_v062_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_3d_base_v062_signal},
    'f07_price_moving_averages_close_sma_dist_max_3d_base_v063_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_3d_base_v063_signal},
    'f07_price_moving_averages_close_sma_dist_min_3d_base_v064_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_3d_base_v064_signal},
    'f07_price_moving_averages_open_sma_5d_base_v065_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_5d_base_v065_signal},
    'f07_price_moving_averages_open_ema_5d_base_v066_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_5d_base_v066_signal},
    'f07_price_moving_averages_open_sma_rel_5d_base_v067_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_5d_base_v067_signal},
    'f07_price_moving_averages_open_ema_rel_5d_base_v068_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_5d_base_v068_signal},
    'f07_price_moving_averages_open_bb_pct_5d_base_v069_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_5d_base_v069_signal},
    'f07_price_moving_averages_open_zscore_5d_base_v070_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_5d_base_v070_signal},
    'f07_price_moving_averages_open_sma_dist_max_5d_base_v071_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_5d_base_v071_signal},
    'f07_price_moving_averages_open_sma_dist_min_5d_base_v072_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_5d_base_v072_signal},
    'f07_price_moving_averages_high_sma_5d_base_v073_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_5d_base_v073_signal},
    'f07_price_moving_averages_high_ema_5d_base_v074_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_5d_base_v074_signal},
    'f07_price_moving_averages_high_sma_rel_5d_base_v075_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_5d_base_v075_signal},
}

F07_PRICE_MOVING_AVERAGES_REGISTRY_001_075 = REGISTRY

if __name__ == '__main__':
    n = 1000
    df = pd.DataFrame({k: np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100 for k in ['open', 'high', 'low', 'close', 'closeadj']})
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info['inputs']]
        y = info['func'](*inputs)
        assert len(y) > 0
        assert y.nunique() > 2
        assert y.std() > 0
    print('Tests passed!')
