import pandas as pd
import numpy as np
def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _acc_up_vol_ratio(c, v, w): return (v * (c.diff() > 0)).rolling(w, min_periods=min(w, 5)).sum() / v.rolling(w, min_periods=min(w, 5)).sum().replace(0, np.nan)
def _acc_mf_multiplier(h, l, c): return ((c - l) - (h - c)) / (h - l).replace(0, np.nan)

def f06_volume_accumulation_up_vol_ratio_w5_v001_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w10_v002_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w21_v003_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w42_v004_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w63_v005_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w126_v006_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w252_v007_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w504_v008_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w20_v009_signal(arg_close, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close, arg_volume, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_w100_v010_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _acc_up_vol_ratio(arg_close_adj, arg_volume, 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w5_v011_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w10_v012_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w21_v013_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w42_v014_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w63_v015_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w126_v016_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w252_v017_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w504_v018_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w20_v019_signal(arg_high, arg_low, arg_close) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close), 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_multiplier_sma_w100_v020_signal(arg_high, arg_low, arg_close, arg_close_adj) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj), 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w5_v021_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w10_v022_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w21_v023_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w42_v024_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w63_v025_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w126_v026_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w252_v027_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w504_v028_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w20_v029_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = _sma(_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_mf_volume_sma_w100_v030_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _sma(_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume, 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w5_v031_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(5, min_periods=min(5, 5)).sum() / arg_volume.rolling(5, min_periods=min(5, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w10_v032_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(10, min_periods=min(10, 5)).sum() / arg_volume.rolling(10, min_periods=min(10, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w21_v033_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(21, min_periods=min(21, 5)).sum() / arg_volume.rolling(21, min_periods=min(21, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w42_v034_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(42, min_periods=min(42, 5)).sum() / arg_volume.rolling(42, min_periods=min(42, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w63_v035_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(63, min_periods=min(63, 5)).sum() / arg_volume.rolling(63, min_periods=min(63, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w126_v036_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(126, min_periods=min(126, 5)).sum() / arg_volume.rolling(126, min_periods=min(126, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w252_v037_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(252, min_periods=min(252, 5)).sum() / arg_volume.rolling(252, min_periods=min(252, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w504_v038_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(504, min_periods=min(504, 5)).sum() / arg_volume.rolling(504, min_periods=min(504, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w20_v039_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    res = ((_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).rolling(20, min_periods=min(20, 5)).sum() / arg_volume.rolling(20, min_periods=min(20, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_chaikin_money_flow_w100_v040_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = ((_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).rolling(100, min_periods=min(100, 5)).sum() / arg_volume.rolling(100, min_periods=min(100, 5)).sum().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w5_v041_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w10_v042_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w21_v043_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w42_v044_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w63_v045_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w126_v046_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w252_v047_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w504_v048_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w20_v049_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    adl = (_acc_mf_multiplier(arg_high, arg_low, arg_close) * arg_volume).cumsum()
    res = adl / _sma(adl, 20).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_adl_to_sma_w100_v050_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    adl = (_acc_mf_multiplier(arg_high * adj, arg_low * adj, arg_close_adj) * arg_volume).cumsum()
    res = adl / _sma(adl, 100).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w5_v051_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 5)
    res = u / _sma(u, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w10_v052_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 10)
    res = u / _sma(u, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w21_v053_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 21)
    res = u / _sma(u, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w42_v054_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 42)
    res = u / _sma(u, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w63_v055_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 63)
    res = u / _sma(u, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w126_v056_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 126)
    res = u / _sma(u, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w252_v057_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 252)
    res = u / _sma(u, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w504_v058_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 504)
    res = u / _sma(u, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w20_v059_signal(arg_close, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close, arg_volume, 20)
    res = u / _sma(u, 20).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_up_vol_ratio_rel_sma_w100_v060_signal(arg_close_adj, arg_volume) -> pd.Series:
    u = _acc_up_vol_ratio(arg_close_adj, arg_volume, 100)
    res = u / _sma(u, 100).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w5_v061_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(5, min_periods=min(5, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w10_v062_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(10, min_periods=min(10, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w21_v063_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(21, min_periods=min(21, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w42_v064_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(42, min_periods=min(42, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w63_v065_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(63, min_periods=min(63, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w126_v066_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(126, min_periods=min(126, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w252_v067_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(252, min_periods=min(252, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w504_v068_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(504, min_periods=min(504, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w20_v069_signal(arg_close, arg_volume) -> pd.Series:
    res = ((arg_close.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(20, min_periods=min(20, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_count_up_high_vol_w100_v070_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = ((arg_close_adj.diff() > 0) & (arg_volume > _sma(arg_volume, 21))).rolling(100, min_periods=min(100, 5)).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w5_v071_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 5) / _sma(arg_volume, 5*2).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w10_v072_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 10) / _sma(arg_volume, 10*2).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w21_v073_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 21) / _sma(arg_volume, 21*2).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w63_v074_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 63) / _sma(arg_volume, 63*2).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_trend_w126_v075_signal(arg_volume) -> pd.Series:
    res = _sma(arg_volume, 126) / _sma(arg_volume, 126*2).replace(0, np.nan)
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
