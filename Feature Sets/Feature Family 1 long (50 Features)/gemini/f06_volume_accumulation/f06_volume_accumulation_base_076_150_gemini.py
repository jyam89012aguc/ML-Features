import pandas as pd
import numpy as np
def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _acc_up_vol_ratio(c, v, w): return (v * (c.diff() > 0)).rolling(w, min_periods=min(w, 5)).sum() / v.rolling(w, min_periods=min(w, 5)).sum().replace(0, np.nan)
def _acc_mf_multiplier(h, l, c): return ((c - l) - (h - c)) / (h - l).replace(0, np.nan)

def f06_volume_accumulation_obv_trend_w5_v076_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w10_v077_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w21_v078_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w42_v079_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w63_v080_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w126_v081_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w252_v082_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w504_v083_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w20_v084_signal(arg_close, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 20).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_obv_trend_w100_v085_signal(arg_close_adj, arg_volume) -> pd.Series:
    o = (arg_volume * np.sign(arg_close_adj.diff()).fillna(0)).cumsum()
    res = o / _sma(o, 100).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w5_v086_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w10_v087_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w21_v088_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w42_v089_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w63_v090_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w126_v091_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w252_v092_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w504_v093_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w20_v094_signal(arg_close, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close.diff(), 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_force_index_sma_w100_v095_signal(arg_close_adj, arg_volume) -> pd.Series:
    res = _sma(arg_volume * arg_close_adj.diff(), 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w5_v096_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w10_v097_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w21_v098_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w42_v099_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w63_v100_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w126_v101_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w252_v102_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w504_v103_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w20_v104_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    dm = ((arg_high + arg_low)/2 - (arg_high.shift(1) + arg_low.shift(1))/2)
    br = arg_volume / (arg_high - arg_low).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_emv_sma_w100_v105_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    h, l = arg_high * adj, arg_low * adj
    dm = ((h + l)/2 - (h.shift(1) + l.shift(1))/2)
    br = arg_volume / (h - l).replace(0, np.nan)
    res = _sma(dm / br.replace(0, np.nan), 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w5_v106_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(5, min_periods=min(5, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(5, min_periods=min(5, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w10_v107_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(10, min_periods=min(10, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(10, min_periods=min(10, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w21_v108_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(21, min_periods=min(21, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(21, min_periods=min(21, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w42_v109_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(42, min_periods=min(42, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(42, min_periods=min(42, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w63_v110_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(63, min_periods=min(63, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(63, min_periods=min(63, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w126_v111_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(126, min_periods=min(126, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(126, min_periods=min(126, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w252_v112_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(252, min_periods=min(252, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(252, min_periods=min(252, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w504_v113_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(504, min_periods=min(504, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(504, min_periods=min(504, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w20_v114_signal(arg_close, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close.diff() > 0)).rolling(20, min_periods=min(20, 5)).sum()
    dn_v = (arg_volume * (arg_close.diff() < 0)).rolling(20, min_periods=min(20, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_accumulation_ratio_w100_v115_signal(arg_close_adj, arg_volume) -> pd.Series:
    up_v = (arg_volume * (arg_close_adj.diff() > 0)).rolling(100, min_periods=min(100, 5)).sum()
    dn_v = (arg_volume * (arg_close_adj.diff() < 0)).rolling(100, min_periods=min(100, 5)).sum()
    res = up_v / dn_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w5_v116_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(5, min_periods=min(5, 5)).sum()
    sum_v = arg_volume.rolling(5, min_periods=min(5, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w10_v117_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(10, min_periods=min(10, 5)).sum()
    sum_v = arg_volume.rolling(10, min_periods=min(10, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w21_v118_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(21, min_periods=min(21, 5)).sum()
    sum_v = arg_volume.rolling(21, min_periods=min(21, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w42_v119_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(42, min_periods=min(42, 5)).sum()
    sum_v = arg_volume.rolling(42, min_periods=min(42, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w63_v120_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(63, min_periods=min(63, 5)).sum()
    sum_v = arg_volume.rolling(63, min_periods=min(63, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w126_v121_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(126, min_periods=min(126, 5)).sum()
    sum_v = arg_volume.rolling(126, min_periods=min(126, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w252_v122_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(252, min_periods=min(252, 5)).sum()
    sum_v = arg_volume.rolling(252, min_periods=min(252, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w504_v123_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(504, min_periods=min(504, 5)).sum()
    sum_v = arg_volume.rolling(504, min_periods=min(504, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w20_v124_signal(arg_close, arg_volume) -> pd.Series:
    abs_diff = arg_close.diff().abs().rolling(20, min_periods=min(20, 5)).sum()
    sum_v = arg_volume.rolling(20, min_periods=min(20, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_volume_efficiency_w100_v125_signal(arg_close_adj, arg_volume) -> pd.Series:
    abs_diff = arg_close_adj.diff().abs().rolling(100, min_periods=min(100, 5)).sum()
    sum_v = arg_volume.rolling(100, min_periods=min(100, 5)).sum()
    res = abs_diff / sum_v.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w5_v126_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w10_v127_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w21_v128_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w42_v129_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w63_v130_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w126_v131_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w252_v132_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w504_v133_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w20_v134_signal(arg_close, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 20).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_pvt_trend_w100_v135_signal(arg_close_adj, arg_volume) -> pd.Series:
    pvt = (arg_volume * arg_close_adj.pct_change()).fillna(0).cumsum()
    res = pvt / _sma(pvt, 100).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w5_v136_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(5, min_periods=min(5, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(5, min_periods=min(5, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w10_v137_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(10, min_periods=min(10, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(10, min_periods=min(10, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w21_v138_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(21, min_periods=min(21, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(21, min_periods=min(21, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w42_v139_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(42, min_periods=min(42, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(42, min_periods=min(42, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w63_v140_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(63, min_periods=min(63, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(63, min_periods=min(63, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w126_v141_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(126, min_periods=min(126, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(126, min_periods=min(126, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w252_v142_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(252, min_periods=min(252, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(252, min_periods=min(252, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w504_v143_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(504, min_periods=min(504, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(504, min_periods=min(504, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w20_v144_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    p = (arg_high + arg_low + arg_close) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(20, min_periods=min(20, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(20, min_periods=min(20, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_money_flow_index_w100_v145_signal(arg_high, arg_low, arg_close, arg_close_adj, arg_volume) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    p = (arg_high * adj + arg_low * adj + arg_close_adj) / 3
    mf = p * arg_volume
    up_mf = (mf * (p.diff() > 0)).rolling(100, min_periods=min(100, 5)).sum()
    dn_mf = (mf * (p.diff() < 0)).rolling(100, min_periods=min(100, 5)).sum()
    res = 100 - (100 / (1 + up_mf / dn_mf.replace(0, np.nan)))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w5_v146_signal(arg_close, arg_volume) -> pd.Series:
    vwap = (arg_close * arg_volume).rolling(5, min_periods=min(5, 5)).sum() / arg_volume.rolling(5, min_periods=min(5, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w21_v147_signal(arg_close, arg_volume) -> pd.Series:
    vwap = (arg_close * arg_volume).rolling(21, min_periods=min(21, 5)).sum() / arg_volume.rolling(21, min_periods=min(21, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w63_v148_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(63, min_periods=min(63, 5)).sum() / arg_volume.rolling(63, min_periods=min(63, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w126_v149_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(126, min_periods=min(126, 5)).sum() / arg_volume.rolling(126, min_periods=min(126, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_volume_accumulation_vwap_rel_close_w252_v150_signal(arg_close_adj, arg_volume) -> pd.Series:
    vwap = (arg_close_adj * arg_volume).rolling(252, min_periods=min(252, 5)).sum() / arg_volume.rolling(252, min_periods=min(252, 5)).sum().replace(0, np.nan)
    res = vwap / arg_close_adj.replace(0, np.nan)
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
