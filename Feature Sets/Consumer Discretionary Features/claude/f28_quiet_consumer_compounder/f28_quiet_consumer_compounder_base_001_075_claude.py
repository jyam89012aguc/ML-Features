import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f28_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    return -_std(rets, w)


def _f28_steady_earnings_growth(netinc, w):
    g = netinc.pct_change(periods=w)
    return _mean(g, w) - _std(g, w)


def _f28_compounder_composite(closeadj, netinc, w):
    rets = closeadj.pct_change()
    vol = _std(rets, w)
    g = netinc.pct_change(periods=w)
    return _mean(g, w) / vol.replace(0, np.nan)


# ===== features =====

def f28qcc_f28_quiet_consumer_compounder_lowvol_rawx_21d_base_v001_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_mean63d_base_v002_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_std126d_base_v003_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_z252d_base_v004_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_rank504d_base_v005_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_abs21d_base_v006_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_sq63d_base_v007_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_max126d_base_v008_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_min252d_base_v009_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_rng504d_base_v010_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_med21d_base_v011_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_q7563d_base_v012_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_q25126d_base_v013_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_ema252d_base_v014_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_emastd504d_base_v015_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_diff21d_base_v016_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_pct63d_base_v017_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_log126d_base_v018_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_sign252d_base_v019_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_sum504d_base_v020_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_zsq21d_base_v021_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_centered63d_base_v022_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_ratio126d_base_v023_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_skew252d_base_v024_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_kurt504d_base_v025_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_rawx_21d_base_v026_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_mean63d_base_v027_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_std126d_base_v028_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_z252d_base_v029_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_rank504d_base_v030_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_abs21d_base_v031_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_sq63d_base_v032_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_max126d_base_v033_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_min252d_base_v034_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_rng504d_base_v035_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_med21d_base_v036_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_q7563d_base_v037_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_q25126d_base_v038_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_ema252d_base_v039_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_emastd504d_base_v040_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_diff21d_base_v041_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_pct63d_base_v042_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_log126d_base_v043_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_sign252d_base_v044_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_sum504d_base_v045_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_zsq21d_base_v046_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_centered63d_base_v047_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_ratio126d_base_v048_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_skew252d_base_v049_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_kurt504d_base_v050_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_rawx_21d_base_v051_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_mean63d_base_v052_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_std126d_base_v053_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_z252d_base_v054_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_rank504d_base_v055_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_abs21d_base_v056_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_sq63d_base_v057_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_max126d_base_v058_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_min252d_base_v059_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_rng504d_base_v060_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_med21d_base_v061_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_q7563d_base_v062_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_q25126d_base_v063_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_ema252d_base_v064_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_emastd504d_base_v065_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_diff21d_base_v066_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_pct63d_base_v067_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_log126d_base_v068_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_sign252d_base_v069_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_sum504d_base_v070_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_zsq21d_base_v071_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_centered63d_base_v072_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_ratio126d_base_v073_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_skew252d_base_v074_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_kurt504d_base_v075_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28qcc_f28_quiet_consumer_compounder_lowvol_rawx_21d_base_v001_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_mean63d_base_v002_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_std126d_base_v003_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_z252d_base_v004_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_rank504d_base_v005_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_abs21d_base_v006_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_sq63d_base_v007_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_max126d_base_v008_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_min252d_base_v009_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_rng504d_base_v010_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_med21d_base_v011_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_q7563d_base_v012_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_q25126d_base_v013_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_ema252d_base_v014_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_emastd504d_base_v015_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_diff21d_base_v016_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_pct63d_base_v017_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_log126d_base_v018_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_sign252d_base_v019_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_sum504d_base_v020_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_zsq21d_base_v021_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_centered63d_base_v022_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_ratio126d_base_v023_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_skew252d_base_v024_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_kurt504d_base_v025_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_rawx_21d_base_v026_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_mean63d_base_v027_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_std126d_base_v028_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_z252d_base_v029_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_rank504d_base_v030_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_abs21d_base_v031_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_sq63d_base_v032_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_max126d_base_v033_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_min252d_base_v034_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_rng504d_base_v035_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_med21d_base_v036_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_q7563d_base_v037_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_q25126d_base_v038_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_ema252d_base_v039_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_emastd504d_base_v040_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_diff21d_base_v041_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_pct63d_base_v042_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_log126d_base_v043_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_sign252d_base_v044_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_sum504d_base_v045_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_zsq21d_base_v046_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_centered63d_base_v047_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_ratio126d_base_v048_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_skew252d_base_v049_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_kurt504d_base_v050_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_rawx_21d_base_v051_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_mean63d_base_v052_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_std126d_base_v053_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_z252d_base_v054_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_rank504d_base_v055_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_abs21d_base_v056_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_sq63d_base_v057_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_max126d_base_v058_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_min252d_base_v059_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_rng504d_base_v060_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_med21d_base_v061_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_q7563d_base_v062_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_q25126d_base_v063_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_ema252d_base_v064_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_emastd504d_base_v065_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_diff21d_base_v066_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_pct63d_base_v067_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_log126d_base_v068_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_sign252d_base_v069_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_sum504d_base_v070_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_zsq21d_base_v071_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_centered63d_base_v072_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_ratio126d_base_v073_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_skew252d_base_v074_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_kurt504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_QUIET_CONSUMER_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps    = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_low_vol_signal", "_f28_steady_earnings_growth", "_f28_compounder_composite",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_quiet_consumer_compounder_base_001_075_claude: {n_features} features pass")
