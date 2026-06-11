import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (crypto winter drawdown) =====
def _f04_dd(s, w):
    # drawdown from rolling peak: close/peak - 1 (<= 0, continuous)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    return s / peak.replace(0, np.nan) - 1.0


def _f04_underwater(s, w):
    # cumulative underwater AREA: rolling sum of instantaneous drawdown depth
    # (continuous integral of depth, NOT a day count)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).sum()


def _f04_recovery(s, w):
    # recovery off the rolling trough: close/trough - 1 (>= 0, continuous)
    trough = s.rolling(w, min_periods=max(2, w // 2)).min()
    return s / trough.replace(0, np.nan) - 1.0


def _f04_painvol(s, w):
    # dispersion (std) of the drawdown path over the window (underwater severity vol)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).std()


# ============ FEATURES 001-075 ============

# 63d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_63d_base_v001_signal(closeadj):
    result = _f04_dd(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_126d_base_v002_signal(closeadj):
    result = _f04_dd(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown depth from rolling peak (annual winter depth)
def f04cw_f04_crypto_winter_drawdown_dd_252d_base_v003_signal(closeadj):
    result = _f04_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown depth from rolling peak (multi-year winter depth)
def f04cw_f04_crypto_winter_drawdown_dd_504d_base_v004_signal(closeadj):
    result = _f04_dd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_42d_base_v005_signal(closeadj):
    result = _f04_dd(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_84d_base_v006_signal(closeadj):
    result = _f04_dd(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_189d_base_v007_signal(closeadj):
    result = _f04_dd(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_378d_base_v008_signal(closeadj):
    result = _f04_dd(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# expanding-style 504d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_504d_base_v009_signal(closeadj):
    result = _f04_underwater(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_252d_base_v010_signal(closeadj):
    result = _f04_underwater(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_126d_base_v011_signal(closeadj):
    result = _f04_underwater(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_63d_base_v012_signal(closeadj):
    result = _f04_underwater(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_189d_base_v013_signal(closeadj):
    result = _f04_underwater(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d underwater AREA (continuous depth integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_378d_base_v014_signal(closeadj):
    result = _f04_underwater(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d recovery off rolling trough
def f04cw_f04_crypto_winter_drawdown_recov_63d_base_v015_signal(closeadj):
    result = _f04_recovery(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d recovery off rolling trough
def f04cw_f04_crypto_winter_drawdown_recov_126d_base_v016_signal(closeadj):
    result = _f04_recovery(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d recovery off rolling trough
def f04cw_f04_crypto_winter_drawdown_recov_252d_base_v017_signal(closeadj):
    result = _f04_recovery(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d recovery off rolling trough (multi-year spring rebound)
def f04cw_f04_crypto_winter_drawdown_recov_504d_base_v018_signal(closeadj):
    result = _f04_recovery(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d recovery off rolling trough
def f04cw_f04_crypto_winter_drawdown_recov_42d_base_v019_signal(closeadj):
    result = _f04_recovery(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d recovery off rolling trough
def f04cw_f04_crypto_winter_drawdown_recov_189d_base_v020_signal(closeadj):
    result = _f04_recovery(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown path volatility (pain dispersion)
def f04cw_f04_crypto_winter_drawdown_ddvol_63d_base_v021_signal(closeadj):
    result = _f04_painvol(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown path volatility
def f04cw_f04_crypto_winter_drawdown_ddvol_126d_base_v022_signal(closeadj):
    result = _f04_painvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown path volatility
def f04cw_f04_crypto_winter_drawdown_ddvol_252d_base_v023_signal(closeadj):
    result = _f04_painvol(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown path volatility
def f04cw_f04_crypto_winter_drawdown_ddvol_504d_base_v024_signal(closeadj):
    result = _f04_painvol(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pain index = mean drawdown depth over window (Ulcer-style level)
def f04cw_f04_crypto_winter_drawdown_pain_126d_base_v025_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pain index = mean drawdown depth over window
def f04cw_f04_crypto_winter_drawdown_pain_252d_base_v026_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pain index = mean drawdown depth over window
def f04cw_f04_crypto_winter_drawdown_pain_63d_base_v027_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pain index = mean drawdown depth over window
def f04cw_f04_crypto_winter_drawdown_pain_504d_base_v028_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 504), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Ulcer index = RMS of drawdown depth (severity magnitude)
def f04cw_f04_crypto_winter_drawdown_ulcer_252d_base_v029_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Ulcer index = RMS of drawdown depth
def f04cw_f04_crypto_winter_drawdown_ulcer_126d_base_v030_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Ulcer index = RMS of drawdown depth
def f04cw_f04_crypto_winter_drawdown_ulcer_63d_base_v031_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = np.sqrt((dd * dd).rolling(63, min_periods=21).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Ulcer index = RMS of drawdown depth
def f04cw_f04_crypto_winter_drawdown_ulcer_504d_base_v032_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MAR-style ratio: trailing return over max drawdown depth
def f04cw_f04_crypto_winter_drawdown_mar_252d_base_v033_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    maxdd = _f04_dd(closeadj, 252).rolling(252, min_periods=84).min().abs()
    result = _safe_div(ret, maxdd)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d MAR-style ratio
def f04cw_f04_crypto_winter_drawdown_mar_126d_base_v034_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    maxdd = _f04_dd(closeadj, 126).rolling(126, min_periods=42).min().abs()
    result = _safe_div(ret, maxdd)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d MAR-style ratio
def f04cw_f04_crypto_winter_drawdown_mar_504d_base_v035_signal(closeadj):
    ret = closeadj / closeadj.shift(504) - 1.0
    maxdd = _f04_dd(closeadj, 504).rolling(252, min_periods=84).min().abs()
    result = _safe_div(ret, maxdd)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown z-score (how unusual is current depth vs its own history)
def f04cw_f04_crypto_winter_drawdown_ddz_252d_base_v036_signal(closeadj):
    result = _z(_f04_dd(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown z-score
def f04cw_f04_crypto_winter_drawdown_ddz_126d_base_v037_signal(closeadj):
    result = _z(_f04_dd(closeadj, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown z-score
def f04cw_f04_crypto_winter_drawdown_ddz_63d_base_v038_signal(closeadj):
    result = _z(_f04_dd(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown z-score over 504d
def f04cw_f04_crypto_winter_drawdown_ddz_504d_base_v039_signal(closeadj):
    result = _z(_f04_dd(closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# depth weighted by dollar-volume (capitulation flow): 126d dd * dv z-score
def f04cw_f04_crypto_winter_drawdown_ddflow_126d_base_v040_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 126) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# depth weighted by dollar-volume: 252d dd * dv z-score
def f04cw_f04_crypto_winter_drawdown_ddflow_252d_base_v041_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 252) * _z(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# depth weighted by dollar-volume: 63d dd * dv z-score
def f04cw_f04_crypto_winter_drawdown_ddflow_63d_base_v042_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 63) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope: rate of change of recovery-off-trough over 21d (252d trough base)
def f04cw_f04_crypto_winter_drawdown_recovslope_252d_base_v043_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec - rec.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope over 21d (126d trough base)
def f04cw_f04_crypto_winter_drawdown_recovslope_126d_base_v044_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    result = rec - rec.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope over 10d (63d trough base)
def f04cw_f04_crypto_winter_drawdown_recovslope_63d_base_v045_signal(closeadj):
    rec = _f04_recovery(closeadj, 63)
    result = rec - rec.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown deepening slope: change in dd over 21d (252d peak base)
def f04cw_f04_crypto_winter_drawdown_ddslope_252d_base_v046_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd - dd.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown deepening slope: change in dd over 21d (126d peak base)
def f04cw_f04_crypto_winter_drawdown_ddslope_126d_base_v047_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd - dd.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio: depth recovered vs depth from peak (252d)
def f04cw_f04_crypto_winter_drawdown_recratio_252d_base_v048_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dd = _f04_dd(closeadj, 252).abs()
    result = _safe_div(rec, rec + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio (126d)
def f04cw_f04_crypto_winter_drawdown_recratio_126d_base_v049_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    dd = _f04_dd(closeadj, 126).abs()
    result = _safe_div(rec, rec + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio (63d)
def f04cw_f04_crypto_winter_drawdown_recratio_63d_base_v050_signal(closeadj):
    rec = _f04_recovery(closeadj, 63)
    dd = _f04_dd(closeadj, 63).abs()
    result = _safe_div(rec, rec + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# average drawdown over 252d normalized by realized vol (vol-adjusted pain)
def f04cw_f04_crypto_winter_drawdown_painvoladj_252d_base_v051_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 252), 252)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# average drawdown over 126d normalized by realized vol
def f04cw_f04_crypto_winter_drawdown_painvoladj_126d_base_v052_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 126), 126)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area normalized by window length (mean depth per day, continuous)
def f04cw_f04_crypto_winter_drawdown_uwmean_252d_base_v053_signal(closeadj):
    result = _f04_underwater(closeadj, 252) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area normalized by window length (126d)
def f04cw_f04_crypto_winter_drawdown_uwmean_126d_base_v054_signal(closeadj):
    result = _f04_underwater(closeadj, 126) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area normalized by window length (504d)
def f04cw_f04_crypto_winter_drawdown_uwmean_504d_base_v055_signal(closeadj):
    result = _f04_underwater(closeadj, 504) / 504.0
    return result.replace([np.inf, -np.inf], np.nan)


# depth severity skew: skew of drawdown path over 252d
def f04cw_f04_crypto_winter_drawdown_ddskew_252d_base_v056_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# depth severity skew over 126d
def f04cw_f04_crypto_winter_drawdown_ddskew_126d_base_v057_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# depth severity kurtosis over 252d (tail pain regime)
def f04cw_f04_crypto_winter_drawdown_ddkurt_252d_base_v058_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(252, min_periods=84).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# current depth relative to worst depth in 252d (fraction of max pain, continuous)
def f04cw_f04_crypto_winter_drawdown_ddfrac_252d_base_v059_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    worst = dd.rolling(252, min_periods=84).min()
    result = _safe_div(dd, worst)
    return result.replace([np.inf, -np.inf], np.nan)


# current depth relative to worst depth in 126d
def f04cw_f04_crypto_winter_drawdown_ddfrac_126d_base_v060_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    worst = dd.rolling(126, min_periods=42).min()
    result = _safe_div(dd, worst)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed drawdown depth: 21d mean of 252d dd (denoised winter level)
def f04cw_f04_crypto_winter_drawdown_ddsmooth_252d_base_v061_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 252), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed drawdown depth: 21d mean of 126d dd
def f04cw_f04_crypto_winter_drawdown_ddsmooth_126d_base_v062_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of drawdown depth (252d dd, span 63)
def f04cw_f04_crypto_winter_drawdown_ddewm_252d_base_v063_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of drawdown depth (126d dd, span 42)
def f04cw_f04_crypto_winter_drawdown_ddewm_126d_base_v064_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area difference: 252d area minus its 21d-prior value (area momentum)
def f04cw_f04_crypto_winter_drawdown_uwslope_252d_base_v065_signal(closeadj):
    uw = _f04_underwater(closeadj, 252)
    result = uw - uw.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area difference (126d)
def f04cw_f04_crypto_winter_drawdown_uwslope_126d_base_v066_signal(closeadj):
    uw = _f04_underwater(closeadj, 126)
    result = uw - uw.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# depth dispersion ratio: short pain vol over long pain vol (severity regime)
def f04cw_f04_crypto_winter_drawdown_ddvolratio_base_v067_signal(closeadj):
    result = _safe_div(_f04_painvol(closeadj, 63), _f04_painvol(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# depth spread: 63d dd minus 252d dd (local vs structural winter)
def f04cw_f04_crypto_winter_drawdown_ddspread_63_252_base_v068_signal(closeadj):
    result = _f04_dd(closeadj, 63) - _f04_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# depth spread: 126d dd minus 504d dd
def f04cw_f04_crypto_winter_drawdown_ddspread_126_504_base_v069_signal(closeadj):
    result = _f04_dd(closeadj, 126) - _f04_dd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery minus drawdown net winter state (252d)
def f04cw_f04_crypto_winter_drawdown_netstate_252d_base_v070_signal(closeadj):
    result = _f04_recovery(closeadj, 252) + _f04_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery minus drawdown net winter state (126d)
def f04cw_f04_crypto_winter_drawdown_netstate_126d_base_v071_signal(closeadj):
    result = _f04_recovery(closeadj, 126) + _f04_dd(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d depth over 252d (how deep vs history)
def f04cw_f04_crypto_winter_drawdown_ddrank_126d_base_v072_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d depth over 252d
def f04cw_f04_crypto_winter_drawdown_ddrank_63d_base_v073_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar-style: annualized 252d return over Ulcer index (return per pain)
def f04cw_f04_crypto_winter_drawdown_retoverulcer_252d_base_v074_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    dd = _f04_dd(closeadj, 252)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(ret, ulcer)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery thrust scaled by underwater area (rebound per unit pain, 252d)
def f04cw_f04_crypto_winter_drawdown_reboundpain_252d_base_v075_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    uw = _f04_underwater(closeadj, 252).abs()
    result = _safe_div(rec, uw / 252.0)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04cw_f04_crypto_winter_drawdown_dd_63d_base_v001_signal,
    f04cw_f04_crypto_winter_drawdown_dd_126d_base_v002_signal,
    f04cw_f04_crypto_winter_drawdown_dd_252d_base_v003_signal,
    f04cw_f04_crypto_winter_drawdown_dd_504d_base_v004_signal,
    f04cw_f04_crypto_winter_drawdown_dd_42d_base_v005_signal,
    f04cw_f04_crypto_winter_drawdown_dd_84d_base_v006_signal,
    f04cw_f04_crypto_winter_drawdown_dd_189d_base_v007_signal,
    f04cw_f04_crypto_winter_drawdown_dd_378d_base_v008_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_504d_base_v009_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_252d_base_v010_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_126d_base_v011_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_63d_base_v012_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_189d_base_v013_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_378d_base_v014_signal,
    f04cw_f04_crypto_winter_drawdown_recov_63d_base_v015_signal,
    f04cw_f04_crypto_winter_drawdown_recov_126d_base_v016_signal,
    f04cw_f04_crypto_winter_drawdown_recov_252d_base_v017_signal,
    f04cw_f04_crypto_winter_drawdown_recov_504d_base_v018_signal,
    f04cw_f04_crypto_winter_drawdown_recov_42d_base_v019_signal,
    f04cw_f04_crypto_winter_drawdown_recov_189d_base_v020_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_63d_base_v021_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_126d_base_v022_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_252d_base_v023_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_504d_base_v024_signal,
    f04cw_f04_crypto_winter_drawdown_pain_126d_base_v025_signal,
    f04cw_f04_crypto_winter_drawdown_pain_252d_base_v026_signal,
    f04cw_f04_crypto_winter_drawdown_pain_63d_base_v027_signal,
    f04cw_f04_crypto_winter_drawdown_pain_504d_base_v028_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_252d_base_v029_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_126d_base_v030_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_63d_base_v031_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_504d_base_v032_signal,
    f04cw_f04_crypto_winter_drawdown_mar_252d_base_v033_signal,
    f04cw_f04_crypto_winter_drawdown_mar_126d_base_v034_signal,
    f04cw_f04_crypto_winter_drawdown_mar_504d_base_v035_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_252d_base_v036_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_126d_base_v037_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_63d_base_v038_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_504d_base_v039_signal,
    f04cw_f04_crypto_winter_drawdown_ddflow_126d_base_v040_signal,
    f04cw_f04_crypto_winter_drawdown_ddflow_252d_base_v041_signal,
    f04cw_f04_crypto_winter_drawdown_ddflow_63d_base_v042_signal,
    f04cw_f04_crypto_winter_drawdown_recovslope_252d_base_v043_signal,
    f04cw_f04_crypto_winter_drawdown_recovslope_126d_base_v044_signal,
    f04cw_f04_crypto_winter_drawdown_recovslope_63d_base_v045_signal,
    f04cw_f04_crypto_winter_drawdown_ddslope_252d_base_v046_signal,
    f04cw_f04_crypto_winter_drawdown_ddslope_126d_base_v047_signal,
    f04cw_f04_crypto_winter_drawdown_recratio_252d_base_v048_signal,
    f04cw_f04_crypto_winter_drawdown_recratio_126d_base_v049_signal,
    f04cw_f04_crypto_winter_drawdown_recratio_63d_base_v050_signal,
    f04cw_f04_crypto_winter_drawdown_painvoladj_252d_base_v051_signal,
    f04cw_f04_crypto_winter_drawdown_painvoladj_126d_base_v052_signal,
    f04cw_f04_crypto_winter_drawdown_uwmean_252d_base_v053_signal,
    f04cw_f04_crypto_winter_drawdown_uwmean_126d_base_v054_signal,
    f04cw_f04_crypto_winter_drawdown_uwmean_504d_base_v055_signal,
    f04cw_f04_crypto_winter_drawdown_ddskew_252d_base_v056_signal,
    f04cw_f04_crypto_winter_drawdown_ddskew_126d_base_v057_signal,
    f04cw_f04_crypto_winter_drawdown_ddkurt_252d_base_v058_signal,
    f04cw_f04_crypto_winter_drawdown_ddfrac_252d_base_v059_signal,
    f04cw_f04_crypto_winter_drawdown_ddfrac_126d_base_v060_signal,
    f04cw_f04_crypto_winter_drawdown_ddsmooth_252d_base_v061_signal,
    f04cw_f04_crypto_winter_drawdown_ddsmooth_126d_base_v062_signal,
    f04cw_f04_crypto_winter_drawdown_ddewm_252d_base_v063_signal,
    f04cw_f04_crypto_winter_drawdown_ddewm_126d_base_v064_signal,
    f04cw_f04_crypto_winter_drawdown_uwslope_252d_base_v065_signal,
    f04cw_f04_crypto_winter_drawdown_uwslope_126d_base_v066_signal,
    f04cw_f04_crypto_winter_drawdown_ddvolratio_base_v067_signal,
    f04cw_f04_crypto_winter_drawdown_ddspread_63_252_base_v068_signal,
    f04cw_f04_crypto_winter_drawdown_ddspread_126_504_base_v069_signal,
    f04cw_f04_crypto_winter_drawdown_netstate_252d_base_v070_signal,
    f04cw_f04_crypto_winter_drawdown_netstate_126d_base_v071_signal,
    f04cw_f04_crypto_winter_drawdown_ddrank_126d_base_v072_signal,
    f04cw_f04_crypto_winter_drawdown_ddrank_63d_base_v073_signal,
    f04cw_f04_crypto_winter_drawdown_retoverulcer_252d_base_v074_signal,
    f04cw_f04_crypto_winter_drawdown_reboundpain_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_CRYPTO_WINTER_DRAWDOWN_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f04_dd", "_f04_underwater", "_f04_recovery", "_f04_painvol")
    n_features = 0
    nan_ok = 0
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
    print(f"OK f04_crypto_winter_drawdown_base_001_075_claude: {n_features} features pass")
