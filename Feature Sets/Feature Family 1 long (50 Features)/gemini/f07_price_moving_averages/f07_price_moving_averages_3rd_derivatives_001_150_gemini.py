# f07_price_moving_averages_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _ma_sma(c, w):
    return c.rolling(w, min_periods=1).mean()

def _ma_ema(c, w):
    return c.ewm(span=w, adjust=False).mean()

def f07_price_moving_averages_open_sma_2d_jerk_v001_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_2d_jerk_v002_signal(arg_open):
    base = arg_open / _ma_ema(arg_open, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_rel_2d_jerk_v003_signal(arg_open, arg_close):
    base = _ma_sma(arg_open, 2) / _ma_sma(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_rel_2d_jerk_v004_signal(arg_open, arg_close):
    base = _ma_ema(arg_open, 2) / _ma_ema(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_bb_pct_2d_jerk_v005_signal(arg_open):
    base = (arg_open - (_ma_sma(arg_open, 2) - 2 * arg_open.rolling(2).std())) / (4 * arg_open.rolling(2).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_zscore_2d_jerk_v006_signal(arg_open):
    base = (arg_open - _ma_sma(arg_open, 2)) / arg_open.rolling(2).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_max_2d_jerk_v007_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 2).rolling(10).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_min_2d_jerk_v008_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 2).rolling(10).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_2d_jerk_v009_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_2d_jerk_v010_signal(arg_high):
    base = arg_high / _ma_ema(arg_high, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_rel_2d_jerk_v011_signal(arg_high, arg_close):
    base = _ma_sma(arg_high, 2) / _ma_sma(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_rel_2d_jerk_v012_signal(arg_high, arg_close):
    base = _ma_ema(arg_high, 2) / _ma_ema(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_bb_pct_2d_jerk_v013_signal(arg_high):
    base = (arg_high - (_ma_sma(arg_high, 2) - 2 * arg_high.rolling(2).std())) / (4 * arg_high.rolling(2).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_zscore_2d_jerk_v014_signal(arg_high):
    base = (arg_high - _ma_sma(arg_high, 2)) / arg_high.rolling(2).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_max_2d_jerk_v015_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 2).rolling(10).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_min_2d_jerk_v016_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 2).rolling(10).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_2d_jerk_v017_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_2d_jerk_v018_signal(arg_low):
    base = arg_low / _ma_ema(arg_low, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_rel_2d_jerk_v019_signal(arg_low, arg_close):
    base = _ma_sma(arg_low, 2) / _ma_sma(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_rel_2d_jerk_v020_signal(arg_low, arg_close):
    base = _ma_ema(arg_low, 2) / _ma_ema(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_bb_pct_2d_jerk_v021_signal(arg_low):
    base = (arg_low - (_ma_sma(arg_low, 2) - 2 * arg_low.rolling(2).std())) / (4 * arg_low.rolling(2).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_zscore_2d_jerk_v022_signal(arg_low):
    base = (arg_low - _ma_sma(arg_low, 2)) / arg_low.rolling(2).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_max_2d_jerk_v023_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 2).rolling(10).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_min_2d_jerk_v024_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 2).rolling(10).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_2d_jerk_v025_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_2d_jerk_v026_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 2)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_2d_jerk_v027_signal(arg_close):
    base = _ma_sma(arg_close, 2) / _ma_sma(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_2d_jerk_v028_signal(arg_close):
    base = _ma_ema(arg_close, 2) / _ma_ema(arg_close, 6)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_2d_jerk_v029_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 2) - 2 * arg_close.rolling(2).std())) / (4 * arg_close.rolling(2).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_2d_jerk_v030_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 2)) / arg_close.rolling(2).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_2d_jerk_v031_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 2).rolling(10).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_2d_jerk_v032_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 2).rolling(10).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_3d_jerk_v033_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_3d_jerk_v034_signal(arg_open):
    base = arg_open / _ma_ema(arg_open, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_rel_3d_jerk_v035_signal(arg_open, arg_close):
    base = _ma_sma(arg_open, 3) / _ma_sma(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_rel_3d_jerk_v036_signal(arg_open, arg_close):
    base = _ma_ema(arg_open, 3) / _ma_ema(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_bb_pct_3d_jerk_v037_signal(arg_open):
    base = (arg_open - (_ma_sma(arg_open, 3) - 2 * arg_open.rolling(3).std())) / (4 * arg_open.rolling(3).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_zscore_3d_jerk_v038_signal(arg_open):
    base = (arg_open - _ma_sma(arg_open, 3)) / arg_open.rolling(3).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_max_3d_jerk_v039_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 3).rolling(15).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_min_3d_jerk_v040_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 3).rolling(15).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_3d_jerk_v041_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_3d_jerk_v042_signal(arg_high):
    base = arg_high / _ma_ema(arg_high, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_rel_3d_jerk_v043_signal(arg_high, arg_close):
    base = _ma_sma(arg_high, 3) / _ma_sma(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_rel_3d_jerk_v044_signal(arg_high, arg_close):
    base = _ma_ema(arg_high, 3) / _ma_ema(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_bb_pct_3d_jerk_v045_signal(arg_high):
    base = (arg_high - (_ma_sma(arg_high, 3) - 2 * arg_high.rolling(3).std())) / (4 * arg_high.rolling(3).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_zscore_3d_jerk_v046_signal(arg_high):
    base = (arg_high - _ma_sma(arg_high, 3)) / arg_high.rolling(3).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_max_3d_jerk_v047_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 3).rolling(15).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_min_3d_jerk_v048_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 3).rolling(15).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_3d_jerk_v049_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_3d_jerk_v050_signal(arg_low):
    base = arg_low / _ma_ema(arg_low, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_rel_3d_jerk_v051_signal(arg_low, arg_close):
    base = _ma_sma(arg_low, 3) / _ma_sma(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_rel_3d_jerk_v052_signal(arg_low, arg_close):
    base = _ma_ema(arg_low, 3) / _ma_ema(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_bb_pct_3d_jerk_v053_signal(arg_low):
    base = (arg_low - (_ma_sma(arg_low, 3) - 2 * arg_low.rolling(3).std())) / (4 * arg_low.rolling(3).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_zscore_3d_jerk_v054_signal(arg_low):
    base = (arg_low - _ma_sma(arg_low, 3)) / arg_low.rolling(3).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_max_3d_jerk_v055_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 3).rolling(15).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_min_3d_jerk_v056_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 3).rolling(15).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_3d_jerk_v057_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_3d_jerk_v058_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 3)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_3d_jerk_v059_signal(arg_close):
    base = _ma_sma(arg_close, 3) / _ma_sma(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_3d_jerk_v060_signal(arg_close):
    base = _ma_ema(arg_close, 3) / _ma_ema(arg_close, 9)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_3d_jerk_v061_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 3) - 2 * arg_close.rolling(3).std())) / (4 * arg_close.rolling(3).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_3d_jerk_v062_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 3)) / arg_close.rolling(3).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_3d_jerk_v063_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 3).rolling(15).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_3d_jerk_v064_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 3).rolling(15).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_5d_jerk_v065_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_5d_jerk_v066_signal(arg_open):
    base = arg_open / _ma_ema(arg_open, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_rel_5d_jerk_v067_signal(arg_open, arg_close):
    base = _ma_sma(arg_open, 5) / _ma_sma(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_ema_rel_5d_jerk_v068_signal(arg_open, arg_close):
    base = _ma_ema(arg_open, 5) / _ma_ema(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_bb_pct_5d_jerk_v069_signal(arg_open):
    base = (arg_open - (_ma_sma(arg_open, 5) - 2 * arg_open.rolling(5).std())) / (4 * arg_open.rolling(5).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_zscore_5d_jerk_v070_signal(arg_open):
    base = (arg_open - _ma_sma(arg_open, 5)) / arg_open.rolling(5).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_max_5d_jerk_v071_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 5).rolling(25).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_open_sma_dist_min_5d_jerk_v072_signal(arg_open):
    base = arg_open / _ma_sma(arg_open, 5).rolling(25).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_5d_jerk_v073_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_5d_jerk_v074_signal(arg_high):
    base = arg_high / _ma_ema(arg_high, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_rel_5d_jerk_v075_signal(arg_high, arg_close):
    base = _ma_sma(arg_high, 5) / _ma_sma(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_ema_rel_5d_jerk_v076_signal(arg_high, arg_close):
    base = _ma_ema(arg_high, 5) / _ma_ema(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_bb_pct_5d_jerk_v077_signal(arg_high):
    base = (arg_high - (_ma_sma(arg_high, 5) - 2 * arg_high.rolling(5).std())) / (4 * arg_high.rolling(5).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_zscore_5d_jerk_v078_signal(arg_high):
    base = (arg_high - _ma_sma(arg_high, 5)) / arg_high.rolling(5).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_max_5d_jerk_v079_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 5).rolling(25).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_high_sma_dist_min_5d_jerk_v080_signal(arg_high):
    base = arg_high / _ma_sma(arg_high, 5).rolling(25).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_5d_jerk_v081_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_5d_jerk_v082_signal(arg_low):
    base = arg_low / _ma_ema(arg_low, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_rel_5d_jerk_v083_signal(arg_low, arg_close):
    base = _ma_sma(arg_low, 5) / _ma_sma(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_ema_rel_5d_jerk_v084_signal(arg_low, arg_close):
    base = _ma_ema(arg_low, 5) / _ma_ema(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_bb_pct_5d_jerk_v085_signal(arg_low):
    base = (arg_low - (_ma_sma(arg_low, 5) - 2 * arg_low.rolling(5).std())) / (4 * arg_low.rolling(5).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_zscore_5d_jerk_v086_signal(arg_low):
    base = (arg_low - _ma_sma(arg_low, 5)) / arg_low.rolling(5).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_max_5d_jerk_v087_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 5).rolling(25).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_low_sma_dist_min_5d_jerk_v088_signal(arg_low):
    base = arg_low / _ma_sma(arg_low, 5).rolling(25).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_5d_jerk_v089_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_5d_jerk_v090_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 5)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_5d_jerk_v091_signal(arg_close):
    base = _ma_sma(arg_close, 5) / _ma_sma(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_5d_jerk_v092_signal(arg_close):
    base = _ma_ema(arg_close, 5) / _ma_ema(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_5d_jerk_v093_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 5) - 2 * arg_close.rolling(5).std())) / (4 * arg_close.rolling(5).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_5d_jerk_v094_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 5)) / arg_close.rolling(5).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_5d_jerk_v095_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 5).rolling(25).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_5d_jerk_v096_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 5).rolling(25).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_10d_jerk_v097_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 10)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_10d_jerk_v098_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 10)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_10d_jerk_v099_signal(arg_close, arg_closeadj):
    base = _ma_sma(arg_close, 10) / _ma_sma(arg_closeadj, 30)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_10d_jerk_v100_signal(arg_close, arg_closeadj):
    base = _ma_ema(arg_close, 10) / _ma_ema(arg_closeadj, 30)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_10d_jerk_v101_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 10) - 2 * arg_close.rolling(10).std())) / (4 * arg_close.rolling(10).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_10d_jerk_v102_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 10)) / arg_close.rolling(10).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_10d_jerk_v103_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 10).rolling(50).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_10d_jerk_v104_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 10).rolling(50).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_15d_jerk_v105_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_15d_jerk_v106_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 15)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_15d_jerk_v107_signal(arg_close, arg_closeadj):
    base = _ma_sma(arg_close, 15) / _ma_sma(arg_closeadj, 45)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_15d_jerk_v108_signal(arg_close, arg_closeadj):
    base = _ma_ema(arg_close, 15) / _ma_ema(arg_closeadj, 45)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_15d_jerk_v109_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 15) - 2 * arg_close.rolling(15).std())) / (4 * arg_close.rolling(15).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_15d_jerk_v110_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 15)) / arg_close.rolling(15).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_15d_jerk_v111_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 15).rolling(75).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_15d_jerk_v112_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 15).rolling(75).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_21d_jerk_v113_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 21)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_21d_jerk_v114_signal(arg_close):
    base = arg_close / _ma_ema(arg_close, 21)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_rel_21d_jerk_v115_signal(arg_close, arg_closeadj):
    base = _ma_sma(arg_close, 21) / _ma_sma(arg_closeadj, 63)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_ema_rel_21d_jerk_v116_signal(arg_close, arg_closeadj):
    base = _ma_ema(arg_close, 21) / _ma_ema(arg_closeadj, 63)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_bb_pct_21d_jerk_v117_signal(arg_close):
    base = (arg_close - (_ma_sma(arg_close, 21) - 2 * arg_close.rolling(21).std())) / (4 * arg_close.rolling(21).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_zscore_21d_jerk_v118_signal(arg_close):
    base = (arg_close - _ma_sma(arg_close, 21)) / arg_close.rolling(21).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_max_21d_jerk_v119_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 21).rolling(105).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_close_sma_dist_min_21d_jerk_v120_signal(arg_close):
    base = arg_close / _ma_sma(arg_close, 21).rolling(105).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_42d_jerk_v121_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 42)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_42d_jerk_v122_signal(arg_closeadj):
    base = arg_closeadj / _ma_ema(arg_closeadj, 42)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_rel_42d_jerk_v123_signal(arg_closeadj):
    base = _ma_sma(arg_closeadj, 42) / _ma_sma(arg_closeadj, 126)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_rel_42d_jerk_v124_signal(arg_closeadj):
    base = _ma_ema(arg_closeadj, 42) / _ma_ema(arg_closeadj, 126)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_bb_pct_42d_jerk_v125_signal(arg_closeadj):
    base = (arg_closeadj - (_ma_sma(arg_closeadj, 42) - 2 * arg_closeadj.rolling(42).std())) / (4 * arg_closeadj.rolling(42).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_zscore_42d_jerk_v126_signal(arg_closeadj):
    base = (arg_closeadj - _ma_sma(arg_closeadj, 42)) / arg_closeadj.rolling(42).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_max_42d_jerk_v127_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 42).rolling(210).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_min_42d_jerk_v128_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 42).rolling(210).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_63d_jerk_v129_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 63)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_63d_jerk_v130_signal(arg_closeadj):
    base = arg_closeadj / _ma_ema(arg_closeadj, 63)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_rel_63d_jerk_v131_signal(arg_closeadj):
    base = _ma_sma(arg_closeadj, 63) / _ma_sma(arg_closeadj, 189)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_rel_63d_jerk_v132_signal(arg_closeadj):
    base = _ma_ema(arg_closeadj, 63) / _ma_ema(arg_closeadj, 189)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_bb_pct_63d_jerk_v133_signal(arg_closeadj):
    base = (arg_closeadj - (_ma_sma(arg_closeadj, 63) - 2 * arg_closeadj.rolling(63).std())) / (4 * arg_closeadj.rolling(63).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_zscore_63d_jerk_v134_signal(arg_closeadj):
    base = (arg_closeadj - _ma_sma(arg_closeadj, 63)) / arg_closeadj.rolling(63).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_max_63d_jerk_v135_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 63).rolling(315).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_min_63d_jerk_v136_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 63).rolling(315).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_126d_jerk_v137_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 126)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_126d_jerk_v138_signal(arg_closeadj):
    base = arg_closeadj / _ma_ema(arg_closeadj, 126)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_rel_126d_jerk_v139_signal(arg_closeadj):
    base = _ma_sma(arg_closeadj, 126) / _ma_sma(arg_closeadj, 378)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_rel_126d_jerk_v140_signal(arg_closeadj):
    base = _ma_ema(arg_closeadj, 126) / _ma_ema(arg_closeadj, 378)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_bb_pct_126d_jerk_v141_signal(arg_closeadj):
    base = (arg_closeadj - (_ma_sma(arg_closeadj, 126) - 2 * arg_closeadj.rolling(126).std())) / (4 * arg_closeadj.rolling(126).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_zscore_126d_jerk_v142_signal(arg_closeadj):
    base = (arg_closeadj - _ma_sma(arg_closeadj, 126)) / arg_closeadj.rolling(126).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_max_126d_jerk_v143_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 126).rolling(630).max().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_dist_min_126d_jerk_v144_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 126).rolling(630).min().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_252d_jerk_v145_signal(arg_closeadj):
    base = arg_closeadj / _ma_sma(arg_closeadj, 252)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_252d_jerk_v146_signal(arg_closeadj):
    base = arg_closeadj / _ma_ema(arg_closeadj, 252)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_sma_rel_252d_jerk_v147_signal(arg_closeadj):
    base = _ma_sma(arg_closeadj, 252) / _ma_sma(arg_closeadj, 756)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_ema_rel_252d_jerk_v148_signal(arg_closeadj):
    base = _ma_ema(arg_closeadj, 252) / _ma_ema(arg_closeadj, 756)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_bb_pct_252d_jerk_v149_signal(arg_closeadj):
    base = (arg_closeadj - (_ma_sma(arg_closeadj, 252) - 2 * arg_closeadj.rolling(252).std())) / (4 * arg_closeadj.rolling(252).std().replace(0, np.nan))
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

def f07_price_moving_averages_closeadj_zscore_252d_jerk_v150_signal(arg_closeadj):
    base = (arg_closeadj - _ma_sma(arg_closeadj, 252)) / arg_closeadj.rolling(252).std().replace(0, np.nan)
    res = base.diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    'f07_price_moving_averages_open_sma_2d_jerk_v001_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_2d_jerk_v001_signal},
    'f07_price_moving_averages_open_ema_2d_jerk_v002_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_2d_jerk_v002_signal},
    'f07_price_moving_averages_open_sma_rel_2d_jerk_v003_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_2d_jerk_v003_signal},
    'f07_price_moving_averages_open_ema_rel_2d_jerk_v004_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_2d_jerk_v004_signal},
    'f07_price_moving_averages_open_bb_pct_2d_jerk_v005_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_2d_jerk_v005_signal},
    'f07_price_moving_averages_open_zscore_2d_jerk_v006_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_2d_jerk_v006_signal},
    'f07_price_moving_averages_open_sma_dist_max_2d_jerk_v007_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_2d_jerk_v007_signal},
    'f07_price_moving_averages_open_sma_dist_min_2d_jerk_v008_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_2d_jerk_v008_signal},
    'f07_price_moving_averages_high_sma_2d_jerk_v009_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_2d_jerk_v009_signal},
    'f07_price_moving_averages_high_ema_2d_jerk_v010_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_2d_jerk_v010_signal},
    'f07_price_moving_averages_high_sma_rel_2d_jerk_v011_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_2d_jerk_v011_signal},
    'f07_price_moving_averages_high_ema_rel_2d_jerk_v012_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_2d_jerk_v012_signal},
    'f07_price_moving_averages_high_bb_pct_2d_jerk_v013_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_2d_jerk_v013_signal},
    'f07_price_moving_averages_high_zscore_2d_jerk_v014_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_2d_jerk_v014_signal},
    'f07_price_moving_averages_high_sma_dist_max_2d_jerk_v015_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_2d_jerk_v015_signal},
    'f07_price_moving_averages_high_sma_dist_min_2d_jerk_v016_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_2d_jerk_v016_signal},
    'f07_price_moving_averages_low_sma_2d_jerk_v017_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_2d_jerk_v017_signal},
    'f07_price_moving_averages_low_ema_2d_jerk_v018_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_2d_jerk_v018_signal},
    'f07_price_moving_averages_low_sma_rel_2d_jerk_v019_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_2d_jerk_v019_signal},
    'f07_price_moving_averages_low_ema_rel_2d_jerk_v020_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_2d_jerk_v020_signal},
    'f07_price_moving_averages_low_bb_pct_2d_jerk_v021_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_2d_jerk_v021_signal},
    'f07_price_moving_averages_low_zscore_2d_jerk_v022_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_2d_jerk_v022_signal},
    'f07_price_moving_averages_low_sma_dist_max_2d_jerk_v023_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_2d_jerk_v023_signal},
    'f07_price_moving_averages_low_sma_dist_min_2d_jerk_v024_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_2d_jerk_v024_signal},
    'f07_price_moving_averages_close_sma_2d_jerk_v025_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_2d_jerk_v025_signal},
    'f07_price_moving_averages_close_ema_2d_jerk_v026_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_2d_jerk_v026_signal},
    'f07_price_moving_averages_close_sma_rel_2d_jerk_v027_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_2d_jerk_v027_signal},
    'f07_price_moving_averages_close_ema_rel_2d_jerk_v028_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_2d_jerk_v028_signal},
    'f07_price_moving_averages_close_bb_pct_2d_jerk_v029_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_2d_jerk_v029_signal},
    'f07_price_moving_averages_close_zscore_2d_jerk_v030_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_2d_jerk_v030_signal},
    'f07_price_moving_averages_close_sma_dist_max_2d_jerk_v031_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_2d_jerk_v031_signal},
    'f07_price_moving_averages_close_sma_dist_min_2d_jerk_v032_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_2d_jerk_v032_signal},
    'f07_price_moving_averages_open_sma_3d_jerk_v033_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_3d_jerk_v033_signal},
    'f07_price_moving_averages_open_ema_3d_jerk_v034_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_3d_jerk_v034_signal},
    'f07_price_moving_averages_open_sma_rel_3d_jerk_v035_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_3d_jerk_v035_signal},
    'f07_price_moving_averages_open_ema_rel_3d_jerk_v036_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_3d_jerk_v036_signal},
    'f07_price_moving_averages_open_bb_pct_3d_jerk_v037_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_3d_jerk_v037_signal},
    'f07_price_moving_averages_open_zscore_3d_jerk_v038_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_3d_jerk_v038_signal},
    'f07_price_moving_averages_open_sma_dist_max_3d_jerk_v039_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_3d_jerk_v039_signal},
    'f07_price_moving_averages_open_sma_dist_min_3d_jerk_v040_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_3d_jerk_v040_signal},
    'f07_price_moving_averages_high_sma_3d_jerk_v041_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_3d_jerk_v041_signal},
    'f07_price_moving_averages_high_ema_3d_jerk_v042_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_3d_jerk_v042_signal},
    'f07_price_moving_averages_high_sma_rel_3d_jerk_v043_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_3d_jerk_v043_signal},
    'f07_price_moving_averages_high_ema_rel_3d_jerk_v044_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_3d_jerk_v044_signal},
    'f07_price_moving_averages_high_bb_pct_3d_jerk_v045_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_3d_jerk_v045_signal},
    'f07_price_moving_averages_high_zscore_3d_jerk_v046_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_3d_jerk_v046_signal},
    'f07_price_moving_averages_high_sma_dist_max_3d_jerk_v047_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_3d_jerk_v047_signal},
    'f07_price_moving_averages_high_sma_dist_min_3d_jerk_v048_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_3d_jerk_v048_signal},
    'f07_price_moving_averages_low_sma_3d_jerk_v049_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_3d_jerk_v049_signal},
    'f07_price_moving_averages_low_ema_3d_jerk_v050_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_3d_jerk_v050_signal},
    'f07_price_moving_averages_low_sma_rel_3d_jerk_v051_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_3d_jerk_v051_signal},
    'f07_price_moving_averages_low_ema_rel_3d_jerk_v052_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_3d_jerk_v052_signal},
    'f07_price_moving_averages_low_bb_pct_3d_jerk_v053_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_3d_jerk_v053_signal},
    'f07_price_moving_averages_low_zscore_3d_jerk_v054_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_3d_jerk_v054_signal},
    'f07_price_moving_averages_low_sma_dist_max_3d_jerk_v055_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_3d_jerk_v055_signal},
    'f07_price_moving_averages_low_sma_dist_min_3d_jerk_v056_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_3d_jerk_v056_signal},
    'f07_price_moving_averages_close_sma_3d_jerk_v057_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_3d_jerk_v057_signal},
    'f07_price_moving_averages_close_ema_3d_jerk_v058_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_3d_jerk_v058_signal},
    'f07_price_moving_averages_close_sma_rel_3d_jerk_v059_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_3d_jerk_v059_signal},
    'f07_price_moving_averages_close_ema_rel_3d_jerk_v060_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_3d_jerk_v060_signal},
    'f07_price_moving_averages_close_bb_pct_3d_jerk_v061_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_3d_jerk_v061_signal},
    'f07_price_moving_averages_close_zscore_3d_jerk_v062_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_3d_jerk_v062_signal},
    'f07_price_moving_averages_close_sma_dist_max_3d_jerk_v063_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_3d_jerk_v063_signal},
    'f07_price_moving_averages_close_sma_dist_min_3d_jerk_v064_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_3d_jerk_v064_signal},
    'f07_price_moving_averages_open_sma_5d_jerk_v065_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_5d_jerk_v065_signal},
    'f07_price_moving_averages_open_ema_5d_jerk_v066_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_ema_5d_jerk_v066_signal},
    'f07_price_moving_averages_open_sma_rel_5d_jerk_v067_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_sma_rel_5d_jerk_v067_signal},
    'f07_price_moving_averages_open_ema_rel_5d_jerk_v068_signal': {'inputs': ['open', 'close'], 'func': f07_price_moving_averages_open_ema_rel_5d_jerk_v068_signal},
    'f07_price_moving_averages_open_bb_pct_5d_jerk_v069_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_bb_pct_5d_jerk_v069_signal},
    'f07_price_moving_averages_open_zscore_5d_jerk_v070_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_zscore_5d_jerk_v070_signal},
    'f07_price_moving_averages_open_sma_dist_max_5d_jerk_v071_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_max_5d_jerk_v071_signal},
    'f07_price_moving_averages_open_sma_dist_min_5d_jerk_v072_signal': {'inputs': ['open'], 'func': f07_price_moving_averages_open_sma_dist_min_5d_jerk_v072_signal},
    'f07_price_moving_averages_high_sma_5d_jerk_v073_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_5d_jerk_v073_signal},
    'f07_price_moving_averages_high_ema_5d_jerk_v074_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_ema_5d_jerk_v074_signal},
    'f07_price_moving_averages_high_sma_rel_5d_jerk_v075_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_sma_rel_5d_jerk_v075_signal},
    'f07_price_moving_averages_high_ema_rel_5d_jerk_v076_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_5d_jerk_v076_signal},
    'f07_price_moving_averages_high_bb_pct_5d_jerk_v077_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_5d_jerk_v077_signal},
    'f07_price_moving_averages_high_zscore_5d_jerk_v078_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_5d_jerk_v078_signal},
    'f07_price_moving_averages_high_sma_dist_max_5d_jerk_v079_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_5d_jerk_v079_signal},
    'f07_price_moving_averages_high_sma_dist_min_5d_jerk_v080_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_5d_jerk_v080_signal},
    'f07_price_moving_averages_low_sma_5d_jerk_v081_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_5d_jerk_v081_signal},
    'f07_price_moving_averages_low_ema_5d_jerk_v082_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_5d_jerk_v082_signal},
    'f07_price_moving_averages_low_sma_rel_5d_jerk_v083_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_5d_jerk_v083_signal},
    'f07_price_moving_averages_low_ema_rel_5d_jerk_v084_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_5d_jerk_v084_signal},
    'f07_price_moving_averages_low_bb_pct_5d_jerk_v085_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_5d_jerk_v085_signal},
    'f07_price_moving_averages_low_zscore_5d_jerk_v086_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_5d_jerk_v086_signal},
    'f07_price_moving_averages_low_sma_dist_max_5d_jerk_v087_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_5d_jerk_v087_signal},
    'f07_price_moving_averages_low_sma_dist_min_5d_jerk_v088_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_5d_jerk_v088_signal},
    'f07_price_moving_averages_close_sma_5d_jerk_v089_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_5d_jerk_v089_signal},
    'f07_price_moving_averages_close_ema_5d_jerk_v090_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_5d_jerk_v090_signal},
    'f07_price_moving_averages_close_sma_rel_5d_jerk_v091_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_5d_jerk_v091_signal},
    'f07_price_moving_averages_close_ema_rel_5d_jerk_v092_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_5d_jerk_v092_signal},
    'f07_price_moving_averages_close_bb_pct_5d_jerk_v093_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_5d_jerk_v093_signal},
    'f07_price_moving_averages_close_zscore_5d_jerk_v094_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_5d_jerk_v094_signal},
    'f07_price_moving_averages_close_sma_dist_max_5d_jerk_v095_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_5d_jerk_v095_signal},
    'f07_price_moving_averages_close_sma_dist_min_5d_jerk_v096_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_5d_jerk_v096_signal},
    'f07_price_moving_averages_close_sma_10d_jerk_v097_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_10d_jerk_v097_signal},
    'f07_price_moving_averages_close_ema_10d_jerk_v098_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_10d_jerk_v098_signal},
    'f07_price_moving_averages_close_sma_rel_10d_jerk_v099_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_10d_jerk_v099_signal},
    'f07_price_moving_averages_close_ema_rel_10d_jerk_v100_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_10d_jerk_v100_signal},
    'f07_price_moving_averages_close_bb_pct_10d_jerk_v101_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_10d_jerk_v101_signal},
    'f07_price_moving_averages_close_zscore_10d_jerk_v102_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_10d_jerk_v102_signal},
    'f07_price_moving_averages_close_sma_dist_max_10d_jerk_v103_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_10d_jerk_v103_signal},
    'f07_price_moving_averages_close_sma_dist_min_10d_jerk_v104_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_10d_jerk_v104_signal},
    'f07_price_moving_averages_close_sma_15d_jerk_v105_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_15d_jerk_v105_signal},
    'f07_price_moving_averages_close_ema_15d_jerk_v106_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_15d_jerk_v106_signal},
    'f07_price_moving_averages_close_sma_rel_15d_jerk_v107_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_15d_jerk_v107_signal},
    'f07_price_moving_averages_close_ema_rel_15d_jerk_v108_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_15d_jerk_v108_signal},
    'f07_price_moving_averages_close_bb_pct_15d_jerk_v109_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_15d_jerk_v109_signal},
    'f07_price_moving_averages_close_zscore_15d_jerk_v110_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_15d_jerk_v110_signal},
    'f07_price_moving_averages_close_sma_dist_max_15d_jerk_v111_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_15d_jerk_v111_signal},
    'f07_price_moving_averages_close_sma_dist_min_15d_jerk_v112_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_15d_jerk_v112_signal},
    'f07_price_moving_averages_close_sma_21d_jerk_v113_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_21d_jerk_v113_signal},
    'f07_price_moving_averages_close_ema_21d_jerk_v114_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_21d_jerk_v114_signal},
    'f07_price_moving_averages_close_sma_rel_21d_jerk_v115_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_21d_jerk_v115_signal},
    'f07_price_moving_averages_close_ema_rel_21d_jerk_v116_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_21d_jerk_v116_signal},
    'f07_price_moving_averages_close_bb_pct_21d_jerk_v117_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_21d_jerk_v117_signal},
    'f07_price_moving_averages_close_zscore_21d_jerk_v118_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_21d_jerk_v118_signal},
    'f07_price_moving_averages_close_sma_dist_max_21d_jerk_v119_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_21d_jerk_v119_signal},
    'f07_price_moving_averages_close_sma_dist_min_21d_jerk_v120_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_21d_jerk_v120_signal},
    'f07_price_moving_averages_closeadj_sma_42d_jerk_v121_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_42d_jerk_v121_signal},
    'f07_price_moving_averages_closeadj_ema_42d_jerk_v122_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_42d_jerk_v122_signal},
    'f07_price_moving_averages_closeadj_sma_rel_42d_jerk_v123_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_42d_jerk_v123_signal},
    'f07_price_moving_averages_closeadj_ema_rel_42d_jerk_v124_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_42d_jerk_v124_signal},
    'f07_price_moving_averages_closeadj_bb_pct_42d_jerk_v125_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_42d_jerk_v125_signal},
    'f07_price_moving_averages_closeadj_zscore_42d_jerk_v126_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_42d_jerk_v126_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_42d_jerk_v127_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_42d_jerk_v127_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_42d_jerk_v128_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_42d_jerk_v128_signal},
    'f07_price_moving_averages_closeadj_sma_63d_jerk_v129_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_63d_jerk_v129_signal},
    'f07_price_moving_averages_closeadj_ema_63d_jerk_v130_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_63d_jerk_v130_signal},
    'f07_price_moving_averages_closeadj_sma_rel_63d_jerk_v131_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_63d_jerk_v131_signal},
    'f07_price_moving_averages_closeadj_ema_rel_63d_jerk_v132_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_63d_jerk_v132_signal},
    'f07_price_moving_averages_closeadj_bb_pct_63d_jerk_v133_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_63d_jerk_v133_signal},
    'f07_price_moving_averages_closeadj_zscore_63d_jerk_v134_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_63d_jerk_v134_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_63d_jerk_v135_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_63d_jerk_v135_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_63d_jerk_v136_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_63d_jerk_v136_signal},
    'f07_price_moving_averages_closeadj_sma_126d_jerk_v137_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_126d_jerk_v137_signal},
    'f07_price_moving_averages_closeadj_ema_126d_jerk_v138_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_126d_jerk_v138_signal},
    'f07_price_moving_averages_closeadj_sma_rel_126d_jerk_v139_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_126d_jerk_v139_signal},
    'f07_price_moving_averages_closeadj_ema_rel_126d_jerk_v140_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_126d_jerk_v140_signal},
    'f07_price_moving_averages_closeadj_bb_pct_126d_jerk_v141_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_126d_jerk_v141_signal},
    'f07_price_moving_averages_closeadj_zscore_126d_jerk_v142_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_126d_jerk_v142_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_126d_jerk_v143_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_126d_jerk_v143_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_126d_jerk_v144_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_126d_jerk_v144_signal},
    'f07_price_moving_averages_closeadj_sma_252d_jerk_v145_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_252d_jerk_v145_signal},
    'f07_price_moving_averages_closeadj_ema_252d_jerk_v146_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_252d_jerk_v146_signal},
    'f07_price_moving_averages_closeadj_sma_rel_252d_jerk_v147_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_252d_jerk_v147_signal},
    'f07_price_moving_averages_closeadj_ema_rel_252d_jerk_v148_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_252d_jerk_v148_signal},
    'f07_price_moving_averages_closeadj_bb_pct_252d_jerk_v149_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_252d_jerk_v149_signal},
    'f07_price_moving_averages_closeadj_zscore_252d_jerk_v150_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_252d_jerk_v150_signal},
}

F07_PRICE_MOVING_AVERAGES_REGISTRY_JERK_001_150 = REGISTRY

if __name__ == '__main__':
    n = 1000
    df = pd.DataFrame({k: np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100 for k in ['open', 'high', 'low', 'close', 'closeadj']})
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info['inputs']]
        y = info['func'](*inputs)
        assert len(y) > 0
        assert y.nunique() > 2 or 'bb_pct' in name
        assert y.std() >= 0
    print('Tests passed!')
