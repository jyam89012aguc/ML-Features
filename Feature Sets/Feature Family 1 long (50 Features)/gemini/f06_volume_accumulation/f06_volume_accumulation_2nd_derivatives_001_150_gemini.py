import pandas as pd
import numpy as np
def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _acc_up_vol_ratio(c, v, w): return (v * (c.diff() > 0)).rolling(w, min_periods=min(w, 5)).sum() / v.rolling(w, min_periods=min(w, 5)).sum().replace(0, np.nan)
def _acc_mf_multiplier(h, l, c): return ((c - l) - (h - c)) / (h - l).replace(0, np.nan)

def f06_volume_accumulation_up_vol_ratio_w5_slope_v001_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 5)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w10_slope_v002_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 10)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w21_slope_v003_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 21)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w42_slope_v004_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 42)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w63_slope_v005_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 63)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w126_slope_v006_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 126)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w252_slope_v007_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 252)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w504_slope_v008_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 504)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w20_slope_v009_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 20)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w100_slope_v010_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 100)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w5_slope_v011_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 5)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w10_slope_v012_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 10)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w21_slope_v013_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 21)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w42_slope_v014_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 42)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w63_slope_v015_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 63)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w126_slope_v016_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 126)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w252_slope_v017_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 252)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w504_slope_v018_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 504)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w20_slope_v019_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 20)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w100_slope_v020_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 100)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w5_slope_v021_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 5)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w10_slope_v022_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 10)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w21_slope_v023_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 21)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w42_slope_v024_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 42)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w63_slope_v025_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 63)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w126_slope_v026_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 126)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w252_slope_v027_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 252)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w504_slope_v028_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 504)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w20_slope_v029_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 20)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w100_slope_v030_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 100)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w5_slope_v031_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(5, min_periods=min(5, 5)).sum() / arg_volume.rolling(5, min_periods=min(5, 5)).sum().replace(0, np.nan))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w10_slope_v032_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(10, min_periods=min(10, 5)).sum() / arg_volume.rolling(10, min_periods=min(10, 5)).sum().replace(0, np.nan))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w21_slope_v033_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(21, min_periods=min(21, 5)).sum() / arg_volume.rolling(21, min_periods=min(21, 5)).sum().replace(0, np.nan))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w42_slope_v034_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(42, min_periods=min(42, 5)).sum() / arg_volume.rolling(42, min_periods=min(42, 5)).sum().replace(0, np.nan))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w63_slope_v035_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(63, min_periods=min(63, 5)).sum() / arg_volume.rolling(63, min_periods=min(63, 5)).sum().replace(0, np.nan))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w126_slope_v036_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(126, min_periods=min(126, 5)).sum() / arg_volume.rolling(126, min_periods=min(126, 5)).sum().replace(0, np.nan))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w252_slope_v037_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(252, min_periods=min(252, 5)).sum() / arg_volume.rolling(252, min_periods=min(252, 5)).sum().replace(0, np.nan))
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w504_slope_v038_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(504, min_periods=min(504, 5)).sum() / arg_volume.rolling(504, min_periods=min(504, 5)).sum().replace(0, np.nan))
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w20_slope_v039_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(20, min_periods=min(20, 5)).sum() / arg_volume.rolling(20, min_periods=min(20, 5)).sum().replace(0, np.nan))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w100_slope_v040_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(100, min_periods=min(100, 5)).sum() / arg_volume.rolling(100, min_periods=min(100, 5)).sum().replace(0, np.nan))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w5_slope_v041_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 5).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w10_slope_v042_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 10).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w21_slope_v043_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 21).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w42_slope_v044_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 42).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w63_slope_v045_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 63).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w126_slope_v046_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 126).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w252_slope_v047_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 252).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w504_slope_v048_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 504).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w20_slope_v049_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 20).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w100_slope_v050_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 100).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w5_slope_v051_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 5)
    res = u / _sma(u, 5).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w10_slope_v052_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 10)
    res = u / _sma(u, 10).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w21_slope_v053_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 21)
    res = u / _sma(u, 21).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w42_slope_v054_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 42)
    res = u / _sma(u, 42).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w63_slope_v055_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 63)
    res = u / _sma(u, 63).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w126_slope_v056_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 126)
    res = u / _sma(u, 126).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w252_slope_v057_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 252)
    res = u / _sma(u, 252).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w504_slope_v058_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 504)
    res = u / _sma(u, 504).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w20_slope_v059_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 20)
    res = u / _sma(u, 20).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w100_slope_v060_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 100)
    res = u / _sma(u, 100).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w5_slope_v061_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(5, min_periods=min(5, 5)).sum()
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w10_slope_v062_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(10, min_periods=min(10, 5)).sum()
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w21_slope_v063_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(21, min_periods=min(21, 5)).sum()
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w42_slope_v064_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(42, min_periods=min(42, 5)).sum()
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w63_slope_v065_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(63, min_periods=min(63, 5)).sum()
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w126_slope_v066_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(126, min_periods=min(126, 5)).sum()
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w252_slope_v067_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(252, min_periods=min(252, 5)).sum()
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w504_slope_v068_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(504, min_periods=min(504, 5)).sum()
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w20_slope_v069_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(20, min_periods=min(20, 5)).sum()
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w100_slope_v070_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(100, min_periods=min(100, 5)).sum()
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w5_slope_v071_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 5) / _sma(arg_volume, 5*2).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w10_slope_v072_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 10) / _sma(arg_volume, 10*2).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w21_slope_v073_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 21) / _sma(arg_volume, 21*2).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w63_slope_v074_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 63) / _sma(arg_volume, 63*2).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w126_slope_v075_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 126) / _sma(arg_volume, 126*2).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w5_slope_v076_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 5).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w10_slope_v077_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 10).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w21_slope_v078_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 21).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w42_slope_v079_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 42).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w63_slope_v080_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 63).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w126_slope_v081_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 126).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w252_slope_v082_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 252).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w504_slope_v083_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 504).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w20_slope_v084_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 20).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w100_slope_v085_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 100).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w5_slope_v086_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 5)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w10_slope_v087_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 10)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w21_slope_v088_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 21)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w42_slope_v089_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 42)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w63_slope_v090_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 63)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w126_slope_v091_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 126)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w252_slope_v092_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 252)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w504_slope_v093_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 504)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w20_slope_v094_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 20)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w100_slope_v095_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 100)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w5_slope_v096_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 5)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w10_slope_v097_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 10)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w21_slope_v098_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 21)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w42_slope_v099_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 42)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w63_slope_v100_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 63)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w126_slope_v101_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 126)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w252_slope_v102_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 252)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w504_slope_v103_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 504)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w20_slope_v104_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 20)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w100_slope_v105_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 100)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w5_slope_v106_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(5, min_periods=min(5, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(5, min_periods=min(5, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w10_slope_v107_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(10, min_periods=min(10, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(10, min_periods=min(10, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w21_slope_v108_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(21, min_periods=min(21, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(21, min_periods=min(21, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w42_slope_v109_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(42, min_periods=min(42, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(42, min_periods=min(42, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w63_slope_v110_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(63, min_periods=min(63, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(63, min_periods=min(63, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w126_slope_v111_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(126, min_periods=min(126, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(126, min_periods=min(126, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w252_slope_v112_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(252, min_periods=min(252, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(252, min_periods=min(252, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w504_slope_v113_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(504, min_periods=min(504, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(504, min_periods=min(504, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w20_slope_v114_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(20, min_periods=min(20, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(20, min_periods=min(20, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w100_slope_v115_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(100, min_periods=min(100, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(100, min_periods=min(100, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w5_slope_v116_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(5, min_periods=min(5, 5)).sum()
    sum_v = arg_volume.rolling(5, min_periods=min(5, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w10_slope_v117_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(10, min_periods=min(10, 5)).sum()
    sum_v = arg_volume.rolling(10, min_periods=min(10, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w21_slope_v118_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(21, min_periods=min(21, 5)).sum()
    sum_v = arg_volume.rolling(21, min_periods=min(21, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w42_slope_v119_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(42, min_periods=min(42, 5)).sum()
    sum_v = arg_volume.rolling(42, min_periods=min(42, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w63_slope_v120_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(63, min_periods=min(63, 5)).sum()
    sum_v = arg_volume.rolling(63, min_periods=min(63, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w126_slope_v121_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(126, min_periods=min(126, 5)).sum()
    sum_v = arg_volume.rolling(126, min_periods=min(126, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w252_slope_v122_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(252, min_periods=min(252, 5)).sum()
    sum_v = arg_volume.rolling(252, min_periods=min(252, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w504_slope_v123_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(504, min_periods=min(504, 5)).sum()
    sum_v = arg_volume.rolling(504, min_periods=min(504, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w20_slope_v124_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(20, min_periods=min(20, 5)).sum()
    sum_v = arg_volume.rolling(20, min_periods=min(20, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w100_slope_v125_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(100, min_periods=min(100, 5)).sum()
    sum_v = arg_volume.rolling(100, min_periods=min(100, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w5_slope_v126_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 5).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w10_slope_v127_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 10).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w21_slope_v128_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 21).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w42_slope_v129_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 42).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w63_slope_v130_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 63).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w126_slope_v131_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 126).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w252_slope_v132_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 252).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w504_slope_v133_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 504).replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w20_slope_v134_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 20).replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w100_slope_v135_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 100).replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w5_slope_v136_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(5, min_periods=min(5, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(5, min_periods=min(5, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w10_slope_v137_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(10, min_periods=min(10, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(10, min_periods=min(10, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w21_slope_v138_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(21, min_periods=min(21, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(21, min_periods=min(21, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w42_slope_v139_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(42, min_periods=min(42, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(42, min_periods=min(42, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w63_slope_v140_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(63, min_periods=min(63, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(63, min_periods=min(63, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w126_slope_v141_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(126, min_periods=min(126, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(126, min_periods=min(126, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w252_slope_v142_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(252, min_periods=min(252, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(252, min_periods=min(252, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w504_slope_v143_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(504, min_periods=min(504, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(504, min_periods=min(504, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w20_slope_v144_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(20, min_periods=min(20, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(20, min_periods=min(20, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w100_slope_v145_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(100, min_periods=min(100, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(100, min_periods=min(100, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w5_slope_v146_signal(arg_close, arg_volume) -> pd.Series:
    vwap = (arg_close * arg_volume).rolling(5, min_periods=min(5, 5)).sum() / arg_volume.rolling(5, min_periods=min(5, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w21_slope_v147_signal(arg_close, arg_volume) -> pd.Series:
    vwap = (arg_close * arg_volume).rolling(21, min_periods=min(21, 5)).sum() / arg_volume.rolling(21, min_periods=min(21, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close.replace(0, np.nan)
    res = res.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w63_slope_v148_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(63, min_periods=min(63, 5)).sum() / arg_volume.rolling(63, min_periods=min(63, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w126_slope_v149_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(126, min_periods=min(126, 5)).sum() / arg_volume.rolling(126, min_periods=min(126, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
    res = res.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w252_slope_v150_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(252, min_periods=min(252, 5)).sum() / arg_volume.rolling(252, min_periods=min(252, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
    res = res.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

NAMES = [f for f in globals() if f.startswith("f06_volume_accumulation_") and f.endswith("_signal")]

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {
    "arg_open": "sep.open",
    "arg_high": "sep.high",
    "arg_low": "sep.low",
    "arg_close": "sep.close",
    "arg_close_adj": "sep.closeadj",
    "arg_volume": "sep.volume"
}
REGISTRY = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"arg_open": np.random.randn(sz).cumsum()+100, "arg_close": np.random.randn(sz).cumsum()+100, "arg_close_adj": np.random.randn(sz).cumsum()+100, "arg_high": np.random.randn(sz).cumsum()+110, "arg_low": np.random.randn(sz).cumsum()+90, "arg_volume": np.random.rand(sz)*1000000+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series); assert len(r) > 0; assert r.nunique() > 2; assert r.std() > 0
    print("OK")
