import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd * xd).sum()
        if denom == 0:
            return np.nan
        return float((xd * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_f, raw=True)


# ===== liquidity domain primitives =====
def _f14_dollar_vol(closeadj, volume):
    return closeadj * volume


def _f14_amihud(closeadj, volume, w):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    illiq = ret / dv
    return illiq.rolling(w, min_periods=max(2, w // 2)).mean() * 1e9


def _f14_amihud_daily(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    return (ret / dv) * 1e9


def _f14_vwap_dev(high, low, closeadj, volume, w):
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(w, min_periods=max(2, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    vwap = pv / vv
    return closeadj / vwap.replace(0, np.nan) - 1.0


def _f14_turnover(volume, w):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)
    return volume / base


# ===== derivative operators =====
def _roc(s, w):
    # discrete first derivative: change over w bars
    return s - s.shift(w)


def _jerk(s, w):
    # discrete second derivative: change of the change over w bars
    return (s - s.shift(w)) - (s.shift(w) - s.shift(2 * w))


# jerk amihud 21d/5d
def f14lq_f14_liquidity_profile_amihud_21d_jerk_v001_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihud 63d/21d
def f14lq_f14_liquidity_profile_amihud_63d_jerk_v002_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihud 126d/21d
def f14lq_f14_liquidity_profile_amihud_126d_jerk_v003_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 126).clip(lower=0))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihud 252d/63d
def f14lq_f14_liquidity_profile_amihud_252d_jerk_v004_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 252).clip(lower=0))
    gg = g
    d = _jerk(gg, 63)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudz 126d/21d
def f14lq_f14_liquidity_profile_amihudz_126d_jerk_v005_signal(closeadj, volume):
    g = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudratio 63d/21d
def f14lq_f14_liquidity_profile_amihudratio_63d_jerk_v006_signal(closeadj, volume):
    g = np.log(_f14_amihud(closeadj, volume, 21).clip(lower=1e-12) / _f14_amihud(closeadj, volume, 126).clip(lower=1e-12))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudrank 63d/21d
def f14lq_f14_liquidity_profile_amihudrank_63d_jerk_v007_signal(closeadj, volume):
    g = _rank(_f14_amihud(closeadj, volume, 63), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudwk 5d/5d
def f14lq_f14_liquidity_profile_amihudwk_5d_jerk_v008_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 5).clip(lower=0))
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudturn 63d/21d
def f14lq_f14_liquidity_profile_amihudturn_63d_jerk_v009_signal(closeadj, volume):
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    t = _z(np.log(_mean(volume, 63).replace(0, np.nan)), 252)
    g = a - t
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqema 63d/21d
def f14lq_f14_liquidity_profile_illiqema_63d_jerk_v010_signal(closeadj, volume):
    il = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    g = il.ewm(span=63, min_periods=21).mean()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliq 21d/5d
def f14lq_f14_liquidity_profile_dollarliq_21d_jerk_v011_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliq 63d/21d
def f14lq_f14_liquidity_profile_dollarliq_63d_jerk_v012_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 63).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliq 252d/63d
def f14lq_f14_liquidity_profile_dollarliq_252d_jerk_v013_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 252).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 63)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqexpand 63d/21d
def f14lq_f14_liquidity_profile_liqexpand_63d_jerk_v014_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    sh = _z(np.log(_mean(dv, 63).replace(0, np.nan)), 252)
    lo = _z(np.log(_mean(dv, 252).replace(0, np.nan)), 504)
    g = sh - lo
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqramp 21d/5d
def f14lq_f14_liquidity_profile_liqramp_21d_jerk_v015_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = np.log(_mean(dv, 21) / _mean(dv, 63).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqz 126d/21d
def f14lq_f14_liquidity_profile_dollarliqz_126d_jerk_v016_signal(closeadj, volume):
    g = _z(_mean(_f14_dollar_vol(closeadj, volume), 126), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqrank 63d/21d
def f14lq_f14_liquidity_profile_dollarliqrank_63d_jerk_v017_signal(closeadj, volume):
    g = _rank(_mean(_f14_dollar_vol(closeadj, volume), 63), 504)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqfloor 63d/21d
def f14lq_f14_liquidity_profile_liqfloor_63d_jerk_v018_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = dv.rolling(63, min_periods=21).min() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqperprice 63d/21d
def f14lq_f14_liquidity_profile_liqperprice_63d_jerk_v019_signal(closeadj, volume):
    g = np.log((_mean(_f14_dollar_vol(closeadj, volume), 63) / _mean(closeadj, 63).replace(0, np.nan)).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqconc 63d/21d
def f14lq_f14_liquidity_profile_liqconc_63d_jerk_v020_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = dv.rolling(63, min_periods=21).max() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnover 21d/5d
def f14lq_f14_liquidity_profile_turnover_21d_jerk_v021_signal(volume):
    g = _mean(volume, 5) / _mean(volume, 63).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnover 63d/21d
def f14lq_f14_liquidity_profile_turnover_63d_jerk_v022_signal(volume):
    g = _mean(volume, 21) / _mean(volume, 126).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoverz 63d/21d
def f14lq_f14_liquidity_profile_turnoverz_63d_jerk_v023_signal(volume):
    g = _z(_f14_turnover(volume, 63), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoverrank 21d/5d
def f14lq_f14_liquidity_profile_turnoverrank_21d_jerk_v024_signal(volume):
    g = _rank(_mean(volume, 21), 252)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnvol 63d/21d
def f14lq_f14_liquidity_profile_turnvol_63d_jerk_v025_signal(volume):
    g = _std(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnskew 126d/21d
def f14lq_f14_liquidity_profile_turnskew_126d_jerk_v026_signal(volume):
    g = volume.rolling(126, min_periods=63).skew()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnac1 63d/21d
def f14lq_f14_liquidity_profile_turnac1_63d_jerk_v027_signal(volume):
    v = np.log(volume.replace(0, np.nan))
    g = v.rolling(63, min_periods=21).corr(v.shift(1))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnmom 21d/5d
def f14lq_f14_liquidity_profile_turnmom_21d_jerk_v028_signal(volume):
    base = np.log(_mean(volume, 21).replace(0, np.nan))
    g = base - base.shift(21)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk cleanturn 63d/21d
def f14lq_f14_liquidity_profile_cleanturn_63d_jerk_v029_signal(volume):
    g = _z(_mean(volume, 21) / _std(volume, 63).replace(0, np.nan), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnregime 252d/63d
def f14lq_f14_liquidity_profile_turnregime_252d_jerk_v030_signal(volume):
    v = np.log(volume.replace(0, np.nan))
    g = _z(_std(v, 63), 252)
    gg = g
    d = _jerk(gg, 63)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdev 21d/5d
def f14lq_f14_liquidity_profile_vwapdev_21d_jerk_v031_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 21)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdev 63d/21d
def f14lq_f14_liquidity_profile_vwapdev_63d_jerk_v032_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdev 126d/21d
def f14lq_f14_liquidity_profile_vwapdev_126d_jerk_v033_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdevz 252d/63d
def f14lq_f14_liquidity_profile_vwapdevz_252d_jerk_v034_signal(high, low, closeadj, volume):
    g = _z(_f14_vwap_dev(high, low, closeadj, volume, 21), 252)
    gg = g
    d = _jerk(gg, 63)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapslip 63d/21d
def f14lq_f14_liquidity_profile_vwapslip_63d_jerk_v035_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 21).abs().rolling(63, min_periods=21).mean()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapasym 63d/21d
def f14lq_f14_liquidity_profile_vwapasym_63d_jerk_v036_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    up = d.clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).mean()
    g = (up - dn) / (up + dn).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdisp 63d/21d
def f14lq_f14_liquidity_profile_vwapdisp_63d_jerk_v037_signal(high, low, closeadj, volume):
    g = _std(_f14_vwap_dev(high, low, closeadj, volume, 21), 63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk tpgap 21d/5d
def f14lq_f14_liquidity_profile_tpgap_21d_jerk_v038_signal(high, low, closeadj):
    tp = (high + low + closeadj) / 3.0
    g = (tp / closeadj.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).mean()
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapband 21d/5d
def f14lq_f14_liquidity_profile_vwapband_21d_jerk_v039_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(21, min_periods=10).sum()
    vv = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    vwap = pv / vv
    disp = (closeadj - vwap).rolling(21, min_periods=10).std().replace(0, np.nan)
    g = (closeadj - vwap) / disp
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapside 63d/21d
def f14lq_f14_liquidity_profile_vwapside_63d_jerk_v040_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    g = (d > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqtrend 63d/21d
def f14lq_f14_liquidity_profile_liqtrend_63d_jerk_v041_signal(closeadj, volume):
    g = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqtrend 126d/21d
def f14lq_f14_liquidity_profile_liqtrend_126d_jerk_v042_signal(closeadj, volume):
    g = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqmom 63d/21d
def f14lq_f14_liquidity_profile_liqmom_63d_jerk_v043_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    g = dv - dv.shift(63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqtrend 126d/21d
def f14lq_f14_liquidity_profile_illiqtrend_126d_jerk_v044_signal(closeadj, volume):
    g = _slope(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqaccel 63d/21d
def f14lq_f14_liquidity_profile_liqaccel_63d_jerk_v045_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    sl = _slope(dv, 63)
    g = sl - sl.shift(63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudmom 63d/21d
def f14lq_f14_liquidity_profile_amihudmom_63d_jerk_v046_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    g = a - a.shift(63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvol 63d/21d
def f14lq_f14_liquidity_profile_liqvol_63d_jerk_v047_signal(closeadj, volume):
    g = _std(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvol 126d/21d
def f14lq_f14_liquidity_profile_liqvol_126d_jerk_v048_signal(closeadj, volume):
    g = _std(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqcv 126d/21d
def f14lq_f14_liquidity_profile_liqcv_126d_jerk_v049_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqvol 252d/63d
def f14lq_f14_liquidity_profile_illiqvol_252d_jerk_v050_signal(closeadj, volume):
    g = _std(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    gg = g
    d = _jerk(gg, 63)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqvol 126d/21d
def f14lq_f14_liquidity_profile_illiqvol_126d_jerk_v051_signal(closeadj, volume):
    g = _std(np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvov 126d/21d
def f14lq_f14_liquidity_profile_liqvov_126d_jerk_v052_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    g = _std(_std(dv, 21), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvolratio 63d/21d
def f14lq_f14_liquidity_profile_liqvolratio_63d_jerk_v053_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    g = np.log(_std(dv, 21).replace(0, np.nan) / _std(dv, 126).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqdownvol 63d/21d
def f14lq_f14_liquidity_profile_liqdownvol_63d_jerk_v054_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    g = chg.where(chg < 0).rolling(63, min_periods=21).std()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk flowimb 21d/5d
def f14lq_f14_liquidity_profile_flowimb_21d_jerk_v055_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    g = signed.rolling(21, min_periods=10).sum() / dv.rolling(21, min_periods=10).sum().replace(0, np.nan)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk flowimb 63d/21d
def f14lq_f14_liquidity_profile_flowimb_63d_jerk_v056_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    g = signed.rolling(63, min_periods=21).sum() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqflowvol 63d/21d
def f14lq_f14_liquidity_profile_liqflowvol_63d_jerk_v057_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    frac = signed / dv.replace(0, np.nan)
    g = frac.rolling(63, min_periods=21).std()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqhitrate 63d/21d
def f14lq_f14_liquidity_profile_liqhitrate_63d_jerk_v058_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    up = chg.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-chg.clip(upper=0)).rolling(63, min_periods=21).sum()
    g = (up - dn) / (up + dn).replace(0, np.nan)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk volretelast 63d/21d
def f14lq_f14_liquidity_profile_volretelast_63d_jerk_v059_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    g = cov / var
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk kyle 63d/21d
def f14lq_f14_liquidity_profile_kyle_63d_jerk_v060_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f14_dollar_vol(closeadj, volume) / 1e6
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    g = -(cov / var)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rollspread 63d/21d
def f14lq_f14_liquidity_profile_rollspread_63d_jerk_v061_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    g = np.sqrt((-cov).clip(lower=0))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rollspreadz 126d/21d
def f14lq_f14_liquidity_profile_rollspreadz_126d_jerk_v062_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    g = _z(np.sqrt((-cov).clip(lower=0)), 126)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk hlspread 21d/5d
def f14lq_f14_liquidity_profile_hlspread_21d_jerk_v063_signal(high, low):
    beta = (np.log(high / low.replace(0, np.nan)) ** 2)
    beta2 = beta.rolling(2, min_periods=2).sum()
    hl2 = (np.maximum(high, high.shift(1)) / np.minimum(low, low.shift(1)).replace(0, np.nan))
    gamma = np.log(hl2) ** 2
    alpha = (np.sqrt(2 * beta2) - np.sqrt(beta2)) / (3 - 2 * np.sqrt(2)) - np.sqrt(gamma / (3 - 2 * np.sqrt(2)))
    spread = 2 * (np.exp(alpha) - 1) / (1 + np.exp(alpha))
    g = spread.rolling(21, min_periods=10).mean()
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rangeilliq 63d/21d
def f14lq_f14_liquidity_profile_rangeilliq_63d_jerk_v064_signal(high, low, volume):
    spr = (high - low)
    il = np.log1p(((spr / volume.replace(0, np.nan)) * 1e6).clip(lower=0))
    g = _z(il.rolling(63, min_periods=21).mean(), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk spreadcost 21d/5d
def f14lq_f14_liquidity_profile_spreadcost_21d_jerk_v065_signal(high, low, closeadj):
    spr = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    aret = closeadj.pct_change().abs().rolling(21, min_periods=10).mean().replace(0, np.nan)
    g = np.log((spr / aret).replace(0, np.nan))
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk fragility 63d/21d
def f14lq_f14_liquidity_profile_fragility_63d_jerk_v066_signal(closeadj, volume):
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    g = tz + az
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk tradability 63d/21d
def f14lq_f14_liquidity_profile_tradability_63d_jerk_v067_signal(high, low, closeadj, volume):
    liq = _z(np.log(_mean(_f14_dollar_vol(closeadj, volume), 63).replace(0, np.nan)), 252)
    illiq = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    slip = _z(_f14_vwap_dev(high, low, closeadj, volume, 21).abs().rolling(63, min_periods=21).mean(), 252)
    g = liq - illiq - slip
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk stressidx 126d/21d
def f14lq_f14_liquidity_profile_stressidx_126d_jerk_v068_signal(closeadj, volume):
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    lvz = _z(_std(dv, 63), 252)
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    g = az + lvz - tz
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk costcomposite 63d/21d
def f14lq_f14_liquidity_profile_costcomposite_63d_jerk_v069_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    t = np.log(_mean(volume, 63).replace(0, np.nan))
    g = _z(a + 0.5 * t, 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqpxdiv 63d/21d
def f14lq_f14_liquidity_profile_liqpxdiv_63d_jerk_v070_signal(closeadj, volume):
    px = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    liq = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    g = np.sign(px) * (px - liq)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqdrift 63d/21d
def f14lq_f14_liquidity_profile_liqdrift_63d_jerk_v071_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    w = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    g = (ret * w).rolling(63, min_periods=21).sum() - ret.rolling(63, min_periods=21).mean()
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk realimpact 21d/5d
def f14lq_f14_liquidity_profile_realimpact_21d_jerk_v072_signal(closeadj, volume):
    ret21 = closeadj.pct_change(21).abs()
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan)
    g = _z(np.log1p(((ret21 / dv) * 1e9).clip(lower=0)), 252)
    gg = g
    d = _jerk(gg, 5)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqmom63 63d/21d
def f14lq_f14_liquidity_profile_liqmom63_63d_jerk_v073_signal(closeadj, volume):
    ret = closeadj.pct_change(63)
    a = np.sqrt(_f14_amihud(closeadj, volume, 63).clip(lower=0)).replace(0, np.nan)
    g = ret / a
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqpervol 63d/21d
def f14lq_f14_liquidity_profile_liqpervol_63d_jerk_v074_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std().replace(0, np.nan)
    g = _z(np.log((dv * vol).replace(0, np.nan)), 252)
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqherf 126d/21d
def f14lq_f14_liquidity_profile_liqherf_126d_jerk_v075_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = np.log(dv.rolling(126, min_periods=63).max() / dv.rolling(126, min_periods=63).median().replace(0, np.nan))
    gg = g
    d = _jerk(gg, 21)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudsm 21d/26d
def f14lq_f14_liquidity_profile_amihudsm_21d_jerk_v076_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudsm 63d/42d
def f14lq_f14_liquidity_profile_amihudsm_63d_jerk_v077_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudsm 126d/42d
def f14lq_f14_liquidity_profile_amihudsm_126d_jerk_v078_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 126).clip(lower=0))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudsm 252d/84d
def f14lq_f14_liquidity_profile_amihudsm_252d_jerk_v079_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 252).clip(lower=0))
    gg = g.ewm(span=63, min_periods=31).mean() - g.rolling(168, min_periods=84).mean()
    d = _jerk(gg, 84)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudzsm 126d/42d
def f14lq_f14_liquidity_profile_amihudzsm_126d_jerk_v080_signal(closeadj, volume):
    g = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudratiosm 63d/42d
def f14lq_f14_liquidity_profile_amihudratiosm_63d_jerk_v081_signal(closeadj, volume):
    g = np.log(_f14_amihud(closeadj, volume, 21).clip(lower=1e-12) / _f14_amihud(closeadj, volume, 126).clip(lower=1e-12))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudranksm 63d/42d
def f14lq_f14_liquidity_profile_amihudranksm_63d_jerk_v082_signal(closeadj, volume):
    g = _rank(_f14_amihud(closeadj, volume, 63), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudwksm 5d/26d
def f14lq_f14_liquidity_profile_amihudwksm_5d_jerk_v083_signal(closeadj, volume):
    g = np.log1p(_f14_amihud(closeadj, volume, 5).clip(lower=0))
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudturnsm 63d/42d
def f14lq_f14_liquidity_profile_amihudturnsm_63d_jerk_v084_signal(closeadj, volume):
    a = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    t = _z(np.log(_mean(volume, 63).replace(0, np.nan)), 252)
    g = a - t
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqemasm 63d/42d
def f14lq_f14_liquidity_profile_illiqemasm_63d_jerk_v085_signal(closeadj, volume):
    il = np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0))
    g = il.ewm(span=63, min_periods=21).mean()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqsm 21d/26d
def f14lq_f14_liquidity_profile_dollarliqsm_21d_jerk_v086_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqsm 63d/42d
def f14lq_f14_liquidity_profile_dollarliqsm_63d_jerk_v087_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 63).replace(0, np.nan))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqsm 252d/84d
def f14lq_f14_liquidity_profile_dollarliqsm_252d_jerk_v088_signal(closeadj, volume):
    g = np.log(_mean(_f14_dollar_vol(closeadj, volume), 252).replace(0, np.nan))
    gg = g.ewm(span=63, min_periods=31).mean() - g.rolling(168, min_periods=84).mean()
    d = _jerk(gg, 84)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqexpandsm 63d/42d
def f14lq_f14_liquidity_profile_liqexpandsm_63d_jerk_v089_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    sh = _z(np.log(_mean(dv, 63).replace(0, np.nan)), 252)
    lo = _z(np.log(_mean(dv, 252).replace(0, np.nan)), 504)
    g = sh - lo
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqrampsm 21d/26d
def f14lq_f14_liquidity_profile_liqrampsm_21d_jerk_v090_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = np.log(_mean(dv, 21) / _mean(dv, 63).replace(0, np.nan))
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqzsm 126d/42d
def f14lq_f14_liquidity_profile_dollarliqzsm_126d_jerk_v091_signal(closeadj, volume):
    g = _z(_mean(_f14_dollar_vol(closeadj, volume), 126), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk dollarliqranksm 63d/42d
def f14lq_f14_liquidity_profile_dollarliqranksm_63d_jerk_v092_signal(closeadj, volume):
    g = _rank(_mean(_f14_dollar_vol(closeadj, volume), 63), 504)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqfloorsm 63d/42d
def f14lq_f14_liquidity_profile_liqfloorsm_63d_jerk_v093_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = dv.rolling(63, min_periods=21).min() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqperpricesm 63d/42d
def f14lq_f14_liquidity_profile_liqperpricesm_63d_jerk_v094_signal(closeadj, volume):
    g = np.log((_mean(_f14_dollar_vol(closeadj, volume), 63) / _mean(closeadj, 63).replace(0, np.nan)).replace(0, np.nan))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqconcsm 63d/42d
def f14lq_f14_liquidity_profile_liqconcsm_63d_jerk_v095_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = dv.rolling(63, min_periods=21).max() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoversm 21d/26d
def f14lq_f14_liquidity_profile_turnoversm_21d_jerk_v096_signal(volume):
    g = _mean(volume, 5) / _mean(volume, 63).replace(0, np.nan)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoversm 63d/42d
def f14lq_f14_liquidity_profile_turnoversm_63d_jerk_v097_signal(volume):
    g = _mean(volume, 21) / _mean(volume, 126).replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoverzsm 63d/42d
def f14lq_f14_liquidity_profile_turnoverzsm_63d_jerk_v098_signal(volume):
    g = _z(_f14_turnover(volume, 63), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnoverranksm 21d/26d
def f14lq_f14_liquidity_profile_turnoverranksm_21d_jerk_v099_signal(volume):
    g = _rank(_mean(volume, 21), 252)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnvolsm 63d/42d
def f14lq_f14_liquidity_profile_turnvolsm_63d_jerk_v100_signal(volume):
    g = _std(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnskewsm 126d/42d
def f14lq_f14_liquidity_profile_turnskewsm_126d_jerk_v101_signal(volume):
    g = volume.rolling(126, min_periods=63).skew()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnac1sm 63d/42d
def f14lq_f14_liquidity_profile_turnac1sm_63d_jerk_v102_signal(volume):
    v = np.log(volume.replace(0, np.nan))
    g = v.rolling(63, min_periods=21).corr(v.shift(1))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnmomsm 21d/26d
def f14lq_f14_liquidity_profile_turnmomsm_21d_jerk_v103_signal(volume):
    base = np.log(_mean(volume, 21).replace(0, np.nan))
    g = base - base.shift(21)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk cleanturnsm 63d/42d
def f14lq_f14_liquidity_profile_cleanturnsm_63d_jerk_v104_signal(volume):
    g = _z(_mean(volume, 21) / _std(volume, 63).replace(0, np.nan), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk turnregimesm 252d/84d
def f14lq_f14_liquidity_profile_turnregimesm_252d_jerk_v105_signal(volume):
    v = np.log(volume.replace(0, np.nan))
    g = _z(_std(v, 63), 252)
    gg = g.ewm(span=63, min_periods=31).mean() - g.rolling(168, min_periods=84).mean()
    d = _jerk(gg, 84)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdevsm 21d/26d
def f14lq_f14_liquidity_profile_vwapdevsm_21d_jerk_v106_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 21)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdevsm 63d/42d
def f14lq_f14_liquidity_profile_vwapdevsm_63d_jerk_v107_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdevsm 126d/42d
def f14lq_f14_liquidity_profile_vwapdevsm_126d_jerk_v108_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdevzsm 252d/84d
def f14lq_f14_liquidity_profile_vwapdevzsm_252d_jerk_v109_signal(high, low, closeadj, volume):
    g = _z(_f14_vwap_dev(high, low, closeadj, volume, 21), 252)
    gg = g.ewm(span=63, min_periods=31).mean() - g.rolling(168, min_periods=84).mean()
    d = _jerk(gg, 84)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapslipsm 63d/42d
def f14lq_f14_liquidity_profile_vwapslipsm_63d_jerk_v110_signal(high, low, closeadj, volume):
    g = _f14_vwap_dev(high, low, closeadj, volume, 21).abs().rolling(63, min_periods=21).mean()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapasymsm 63d/42d
def f14lq_f14_liquidity_profile_vwapasymsm_63d_jerk_v111_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    up = d.clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).mean()
    g = (up - dn) / (up + dn).replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapdispsm 63d/42d
def f14lq_f14_liquidity_profile_vwapdispsm_63d_jerk_v112_signal(high, low, closeadj, volume):
    g = _std(_f14_vwap_dev(high, low, closeadj, volume, 21), 63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk tpgapsm 21d/26d
def f14lq_f14_liquidity_profile_tpgapsm_21d_jerk_v113_signal(high, low, closeadj):
    tp = (high + low + closeadj) / 3.0
    g = (tp / closeadj.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).mean()
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapbandsm 21d/26d
def f14lq_f14_liquidity_profile_vwapbandsm_21d_jerk_v114_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    pv = (tp * volume).rolling(21, min_periods=10).sum()
    vv = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    vwap = pv / vv
    disp = (closeadj - vwap).rolling(21, min_periods=10).std().replace(0, np.nan)
    g = (closeadj - vwap) / disp
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk vwapsidesm 63d/42d
def f14lq_f14_liquidity_profile_vwapsidesm_63d_jerk_v115_signal(high, low, closeadj, volume):
    d = _f14_vwap_dev(high, low, closeadj, volume, 21)
    g = (d > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqtrendsm 63d/42d
def f14lq_f14_liquidity_profile_liqtrendsm_63d_jerk_v116_signal(closeadj, volume):
    g = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqtrendsm 126d/42d
def f14lq_f14_liquidity_profile_liqtrendsm_126d_jerk_v117_signal(closeadj, volume):
    g = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqmomsm 63d/42d
def f14lq_f14_liquidity_profile_liqmomsm_63d_jerk_v118_signal(closeadj, volume):
    dv = np.log(_mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan))
    g = dv - dv.shift(63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqtrendsm 126d/42d
def f14lq_f14_liquidity_profile_illiqtrendsm_126d_jerk_v119_signal(closeadj, volume):
    g = _slope(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqaccelsm 63d/42d
def f14lq_f14_liquidity_profile_liqaccelsm_63d_jerk_v120_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    sl = _slope(dv, 63)
    g = sl - sl.shift(63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk amihudmomsm 63d/42d
def f14lq_f14_liquidity_profile_amihudmomsm_63d_jerk_v121_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0))
    g = a - a.shift(63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvolsm 63d/42d
def f14lq_f14_liquidity_profile_liqvolsm_63d_jerk_v122_signal(closeadj, volume):
    g = _std(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvolsm 126d/42d
def f14lq_f14_liquidity_profile_liqvolsm_126d_jerk_v123_signal(closeadj, volume):
    g = _std(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqcvsm 126d/42d
def f14lq_f14_liquidity_profile_liqcvsm_126d_jerk_v124_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqvolsm 252d/84d
def f14lq_f14_liquidity_profile_illiqvolsm_252d_jerk_v125_signal(closeadj, volume):
    g = _std(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    gg = g.ewm(span=63, min_periods=31).mean() - g.rolling(168, min_periods=84).mean()
    d = _jerk(gg, 84)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk illiqvolsm 126d/42d
def f14lq_f14_liquidity_profile_illiqvolsm_126d_jerk_v126_signal(closeadj, volume):
    g = _std(np.log1p(_f14_amihud_daily(closeadj, volume).clip(lower=0)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvovsm 126d/42d
def f14lq_f14_liquidity_profile_liqvovsm_126d_jerk_v127_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    g = _std(_std(dv, 21), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqvolratiosm 63d/42d
def f14lq_f14_liquidity_profile_liqvolratiosm_63d_jerk_v128_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    g = np.log(_std(dv, 21).replace(0, np.nan) / _std(dv, 126).replace(0, np.nan))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqdownvolsm 63d/42d
def f14lq_f14_liquidity_profile_liqdownvolsm_63d_jerk_v129_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    g = chg.where(chg < 0).rolling(63, min_periods=21).std()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk flowimbsm 21d/26d
def f14lq_f14_liquidity_profile_flowimbsm_21d_jerk_v130_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    g = signed.rolling(21, min_periods=10).sum() / dv.rolling(21, min_periods=10).sum().replace(0, np.nan)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk flowimbsm 63d/42d
def f14lq_f14_liquidity_profile_flowimbsm_63d_jerk_v131_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    g = signed.rolling(63, min_periods=21).sum() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqflowvolsm 63d/42d
def f14lq_f14_liquidity_profile_liqflowvolsm_63d_jerk_v132_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    frac = signed / dv.replace(0, np.nan)
    g = frac.rolling(63, min_periods=21).std()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqhitratesm 63d/42d
def f14lq_f14_liquidity_profile_liqhitratesm_63d_jerk_v133_signal(closeadj, volume):
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    chg = dv.diff()
    up = chg.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-chg.clip(upper=0)).rolling(63, min_periods=21).sum()
    g = (up - dn) / (up + dn).replace(0, np.nan)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk volretelastsm 63d/42d
def f14lq_f14_liquidity_profile_volretelastsm_63d_jerk_v134_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    g = cov / var
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk kylesm 63d/42d
def f14lq_f14_liquidity_profile_kylesm_63d_jerk_v135_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _f14_dollar_vol(closeadj, volume) / 1e6
    cov = ret.rolling(63, min_periods=21).cov(dv)
    var = dv.rolling(63, min_periods=21).var().replace(0, np.nan)
    g = -(cov / var)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rollspreadsm 63d/42d
def f14lq_f14_liquidity_profile_rollspreadsm_63d_jerk_v136_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    g = np.sqrt((-cov).clip(lower=0))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rollspreadzsm 126d/42d
def f14lq_f14_liquidity_profile_rollspreadzsm_126d_jerk_v137_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    g = _z(np.sqrt((-cov).clip(lower=0)), 126)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk hlspreadsm 21d/26d
def f14lq_f14_liquidity_profile_hlspreadsm_21d_jerk_v138_signal(high, low):
    beta = (np.log(high / low.replace(0, np.nan)) ** 2)
    beta2 = beta.rolling(2, min_periods=2).sum()
    hl2 = (np.maximum(high, high.shift(1)) / np.minimum(low, low.shift(1)).replace(0, np.nan))
    gamma = np.log(hl2) ** 2
    alpha = (np.sqrt(2 * beta2) - np.sqrt(beta2)) / (3 - 2 * np.sqrt(2)) - np.sqrt(gamma / (3 - 2 * np.sqrt(2)))
    spread = 2 * (np.exp(alpha) - 1) / (1 + np.exp(alpha))
    g = spread.rolling(21, min_periods=10).mean()
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk rangeilliqsm 63d/42d
def f14lq_f14_liquidity_profile_rangeilliqsm_63d_jerk_v139_signal(high, low, volume):
    spr = (high - low)
    il = np.log1p(((spr / volume.replace(0, np.nan)) * 1e6).clip(lower=0))
    g = _z(il.rolling(63, min_periods=21).mean(), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk spreadcostsm 21d/26d
def f14lq_f14_liquidity_profile_spreadcostsm_21d_jerk_v140_signal(high, low, closeadj):
    spr = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    aret = closeadj.pct_change().abs().rolling(21, min_periods=10).mean().replace(0, np.nan)
    g = np.log((spr / aret).replace(0, np.nan))
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk fragilitysm 63d/42d
def f14lq_f14_liquidity_profile_fragilitysm_63d_jerk_v141_signal(closeadj, volume):
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    g = tz + az
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk tradabilitysm 63d/42d
def f14lq_f14_liquidity_profile_tradabilitysm_63d_jerk_v142_signal(high, low, closeadj, volume):
    liq = _z(np.log(_mean(_f14_dollar_vol(closeadj, volume), 63).replace(0, np.nan)), 252)
    illiq = _z(np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0)), 252)
    slip = _z(_f14_vwap_dev(high, low, closeadj, volume, 21).abs().rolling(63, min_periods=21).mean(), 252)
    g = liq - illiq - slip
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk stressidxsm 126d/42d
def f14lq_f14_liquidity_profile_stressidxsm_126d_jerk_v143_signal(closeadj, volume):
    az = _z(np.log1p(_f14_amihud(closeadj, volume, 21).clip(lower=0)), 252)
    dv = np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan))
    lvz = _z(_std(dv, 63), 252)
    tz = _z(np.log(_mean(volume, 21).replace(0, np.nan)), 252)
    g = az + lvz - tz
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk costcompositesm 63d/42d
def f14lq_f14_liquidity_profile_costcompositesm_63d_jerk_v144_signal(closeadj, volume):
    a = np.log1p(_f14_amihud(closeadj, volume, 63).clip(lower=0))
    t = np.log(_mean(volume, 63).replace(0, np.nan))
    g = _z(a + 0.5 * t, 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqpxdivsm 63d/42d
def f14lq_f14_liquidity_profile_liqpxdivsm_63d_jerk_v145_signal(closeadj, volume):
    px = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    liq = _slope(np.log(_f14_dollar_vol(closeadj, volume).replace(0, np.nan)), 63)
    g = np.sign(px) * (px - liq)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqdriftsm 63d/42d
def f14lq_f14_liquidity_profile_liqdriftsm_63d_jerk_v146_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    w = dv / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    g = (ret * w).rolling(63, min_periods=21).sum() - ret.rolling(63, min_periods=21).mean()
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk realimpactsm 21d/26d
def f14lq_f14_liquidity_profile_realimpactsm_21d_jerk_v147_signal(closeadj, volume):
    ret21 = closeadj.pct_change(21).abs()
    dv = _mean(_f14_dollar_vol(closeadj, volume), 21).replace(0, np.nan)
    g = _z(np.log1p(((ret21 / dv) * 1e9).clip(lower=0)), 252)
    gg = g.ewm(span=5, min_periods=3).mean() - g.rolling(52, min_periods=26).mean()
    d = _jerk(gg, 26)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqmom63sm 63d/42d
def f14lq_f14_liquidity_profile_liqmom63sm_63d_jerk_v148_signal(closeadj, volume):
    ret = closeadj.pct_change(63)
    a = np.sqrt(_f14_amihud(closeadj, volume, 63).clip(lower=0)).replace(0, np.nan)
    g = ret / a
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqpervolsm 63d/42d
def f14lq_f14_liquidity_profile_liqpervolsm_63d_jerk_v149_signal(closeadj, volume):
    dv = _mean(_f14_dollar_vol(closeadj, volume), 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std().replace(0, np.nan)
    g = _z(np.log((dv * vol).replace(0, np.nan)), 252)
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

# jerk liqherfsm 126d/42d
def f14lq_f14_liquidity_profile_liqherfsm_126d_jerk_v150_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    g = np.log(dv.rolling(126, min_periods=63).max() / dv.rolling(126, min_periods=63).median().replace(0, np.nan))
    gg = g.ewm(span=21, min_periods=10).mean() - g.rolling(84, min_periods=42).mean()
    d = _jerk(gg, 42)
    return d.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f14lq_f14_liquidity_profile_amihud_21d_jerk_v001_signal,
    f14lq_f14_liquidity_profile_amihud_63d_jerk_v002_signal,
    f14lq_f14_liquidity_profile_amihud_126d_jerk_v003_signal,
    f14lq_f14_liquidity_profile_amihud_252d_jerk_v004_signal,
    f14lq_f14_liquidity_profile_amihudz_126d_jerk_v005_signal,
    f14lq_f14_liquidity_profile_amihudratio_63d_jerk_v006_signal,
    f14lq_f14_liquidity_profile_amihudrank_63d_jerk_v007_signal,
    f14lq_f14_liquidity_profile_amihudwk_5d_jerk_v008_signal,
    f14lq_f14_liquidity_profile_amihudturn_63d_jerk_v009_signal,
    f14lq_f14_liquidity_profile_illiqema_63d_jerk_v010_signal,
    f14lq_f14_liquidity_profile_dollarliq_21d_jerk_v011_signal,
    f14lq_f14_liquidity_profile_dollarliq_63d_jerk_v012_signal,
    f14lq_f14_liquidity_profile_dollarliq_252d_jerk_v013_signal,
    f14lq_f14_liquidity_profile_liqexpand_63d_jerk_v014_signal,
    f14lq_f14_liquidity_profile_liqramp_21d_jerk_v015_signal,
    f14lq_f14_liquidity_profile_dollarliqz_126d_jerk_v016_signal,
    f14lq_f14_liquidity_profile_dollarliqrank_63d_jerk_v017_signal,
    f14lq_f14_liquidity_profile_liqfloor_63d_jerk_v018_signal,
    f14lq_f14_liquidity_profile_liqperprice_63d_jerk_v019_signal,
    f14lq_f14_liquidity_profile_liqconc_63d_jerk_v020_signal,
    f14lq_f14_liquidity_profile_turnover_21d_jerk_v021_signal,
    f14lq_f14_liquidity_profile_turnover_63d_jerk_v022_signal,
    f14lq_f14_liquidity_profile_turnoverz_63d_jerk_v023_signal,
    f14lq_f14_liquidity_profile_turnoverrank_21d_jerk_v024_signal,
    f14lq_f14_liquidity_profile_turnvol_63d_jerk_v025_signal,
    f14lq_f14_liquidity_profile_turnskew_126d_jerk_v026_signal,
    f14lq_f14_liquidity_profile_turnac1_63d_jerk_v027_signal,
    f14lq_f14_liquidity_profile_turnmom_21d_jerk_v028_signal,
    f14lq_f14_liquidity_profile_cleanturn_63d_jerk_v029_signal,
    f14lq_f14_liquidity_profile_turnregime_252d_jerk_v030_signal,
    f14lq_f14_liquidity_profile_vwapdev_21d_jerk_v031_signal,
    f14lq_f14_liquidity_profile_vwapdev_63d_jerk_v032_signal,
    f14lq_f14_liquidity_profile_vwapdev_126d_jerk_v033_signal,
    f14lq_f14_liquidity_profile_vwapdevz_252d_jerk_v034_signal,
    f14lq_f14_liquidity_profile_vwapslip_63d_jerk_v035_signal,
    f14lq_f14_liquidity_profile_vwapasym_63d_jerk_v036_signal,
    f14lq_f14_liquidity_profile_vwapdisp_63d_jerk_v037_signal,
    f14lq_f14_liquidity_profile_tpgap_21d_jerk_v038_signal,
    f14lq_f14_liquidity_profile_vwapband_21d_jerk_v039_signal,
    f14lq_f14_liquidity_profile_vwapside_63d_jerk_v040_signal,
    f14lq_f14_liquidity_profile_liqtrend_63d_jerk_v041_signal,
    f14lq_f14_liquidity_profile_liqtrend_126d_jerk_v042_signal,
    f14lq_f14_liquidity_profile_liqmom_63d_jerk_v043_signal,
    f14lq_f14_liquidity_profile_illiqtrend_126d_jerk_v044_signal,
    f14lq_f14_liquidity_profile_liqaccel_63d_jerk_v045_signal,
    f14lq_f14_liquidity_profile_amihudmom_63d_jerk_v046_signal,
    f14lq_f14_liquidity_profile_liqvol_63d_jerk_v047_signal,
    f14lq_f14_liquidity_profile_liqvol_126d_jerk_v048_signal,
    f14lq_f14_liquidity_profile_liqcv_126d_jerk_v049_signal,
    f14lq_f14_liquidity_profile_illiqvol_252d_jerk_v050_signal,
    f14lq_f14_liquidity_profile_illiqvol_126d_jerk_v051_signal,
    f14lq_f14_liquidity_profile_liqvov_126d_jerk_v052_signal,
    f14lq_f14_liquidity_profile_liqvolratio_63d_jerk_v053_signal,
    f14lq_f14_liquidity_profile_liqdownvol_63d_jerk_v054_signal,
    f14lq_f14_liquidity_profile_flowimb_21d_jerk_v055_signal,
    f14lq_f14_liquidity_profile_flowimb_63d_jerk_v056_signal,
    f14lq_f14_liquidity_profile_liqflowvol_63d_jerk_v057_signal,
    f14lq_f14_liquidity_profile_liqhitrate_63d_jerk_v058_signal,
    f14lq_f14_liquidity_profile_volretelast_63d_jerk_v059_signal,
    f14lq_f14_liquidity_profile_kyle_63d_jerk_v060_signal,
    f14lq_f14_liquidity_profile_rollspread_63d_jerk_v061_signal,
    f14lq_f14_liquidity_profile_rollspreadz_126d_jerk_v062_signal,
    f14lq_f14_liquidity_profile_hlspread_21d_jerk_v063_signal,
    f14lq_f14_liquidity_profile_rangeilliq_63d_jerk_v064_signal,
    f14lq_f14_liquidity_profile_spreadcost_21d_jerk_v065_signal,
    f14lq_f14_liquidity_profile_fragility_63d_jerk_v066_signal,
    f14lq_f14_liquidity_profile_tradability_63d_jerk_v067_signal,
    f14lq_f14_liquidity_profile_stressidx_126d_jerk_v068_signal,
    f14lq_f14_liquidity_profile_costcomposite_63d_jerk_v069_signal,
    f14lq_f14_liquidity_profile_liqpxdiv_63d_jerk_v070_signal,
    f14lq_f14_liquidity_profile_liqdrift_63d_jerk_v071_signal,
    f14lq_f14_liquidity_profile_realimpact_21d_jerk_v072_signal,
    f14lq_f14_liquidity_profile_liqmom63_63d_jerk_v073_signal,
    f14lq_f14_liquidity_profile_liqpervol_63d_jerk_v074_signal,
    f14lq_f14_liquidity_profile_liqherf_126d_jerk_v075_signal,
    f14lq_f14_liquidity_profile_amihudsm_21d_jerk_v076_signal,
    f14lq_f14_liquidity_profile_amihudsm_63d_jerk_v077_signal,
    f14lq_f14_liquidity_profile_amihudsm_126d_jerk_v078_signal,
    f14lq_f14_liquidity_profile_amihudsm_252d_jerk_v079_signal,
    f14lq_f14_liquidity_profile_amihudzsm_126d_jerk_v080_signal,
    f14lq_f14_liquidity_profile_amihudratiosm_63d_jerk_v081_signal,
    f14lq_f14_liquidity_profile_amihudranksm_63d_jerk_v082_signal,
    f14lq_f14_liquidity_profile_amihudwksm_5d_jerk_v083_signal,
    f14lq_f14_liquidity_profile_amihudturnsm_63d_jerk_v084_signal,
    f14lq_f14_liquidity_profile_illiqemasm_63d_jerk_v085_signal,
    f14lq_f14_liquidity_profile_dollarliqsm_21d_jerk_v086_signal,
    f14lq_f14_liquidity_profile_dollarliqsm_63d_jerk_v087_signal,
    f14lq_f14_liquidity_profile_dollarliqsm_252d_jerk_v088_signal,
    f14lq_f14_liquidity_profile_liqexpandsm_63d_jerk_v089_signal,
    f14lq_f14_liquidity_profile_liqrampsm_21d_jerk_v090_signal,
    f14lq_f14_liquidity_profile_dollarliqzsm_126d_jerk_v091_signal,
    f14lq_f14_liquidity_profile_dollarliqranksm_63d_jerk_v092_signal,
    f14lq_f14_liquidity_profile_liqfloorsm_63d_jerk_v093_signal,
    f14lq_f14_liquidity_profile_liqperpricesm_63d_jerk_v094_signal,
    f14lq_f14_liquidity_profile_liqconcsm_63d_jerk_v095_signal,
    f14lq_f14_liquidity_profile_turnoversm_21d_jerk_v096_signal,
    f14lq_f14_liquidity_profile_turnoversm_63d_jerk_v097_signal,
    f14lq_f14_liquidity_profile_turnoverzsm_63d_jerk_v098_signal,
    f14lq_f14_liquidity_profile_turnoverranksm_21d_jerk_v099_signal,
    f14lq_f14_liquidity_profile_turnvolsm_63d_jerk_v100_signal,
    f14lq_f14_liquidity_profile_turnskewsm_126d_jerk_v101_signal,
    f14lq_f14_liquidity_profile_turnac1sm_63d_jerk_v102_signal,
    f14lq_f14_liquidity_profile_turnmomsm_21d_jerk_v103_signal,
    f14lq_f14_liquidity_profile_cleanturnsm_63d_jerk_v104_signal,
    f14lq_f14_liquidity_profile_turnregimesm_252d_jerk_v105_signal,
    f14lq_f14_liquidity_profile_vwapdevsm_21d_jerk_v106_signal,
    f14lq_f14_liquidity_profile_vwapdevsm_63d_jerk_v107_signal,
    f14lq_f14_liquidity_profile_vwapdevsm_126d_jerk_v108_signal,
    f14lq_f14_liquidity_profile_vwapdevzsm_252d_jerk_v109_signal,
    f14lq_f14_liquidity_profile_vwapslipsm_63d_jerk_v110_signal,
    f14lq_f14_liquidity_profile_vwapasymsm_63d_jerk_v111_signal,
    f14lq_f14_liquidity_profile_vwapdispsm_63d_jerk_v112_signal,
    f14lq_f14_liquidity_profile_tpgapsm_21d_jerk_v113_signal,
    f14lq_f14_liquidity_profile_vwapbandsm_21d_jerk_v114_signal,
    f14lq_f14_liquidity_profile_vwapsidesm_63d_jerk_v115_signal,
    f14lq_f14_liquidity_profile_liqtrendsm_63d_jerk_v116_signal,
    f14lq_f14_liquidity_profile_liqtrendsm_126d_jerk_v117_signal,
    f14lq_f14_liquidity_profile_liqmomsm_63d_jerk_v118_signal,
    f14lq_f14_liquidity_profile_illiqtrendsm_126d_jerk_v119_signal,
    f14lq_f14_liquidity_profile_liqaccelsm_63d_jerk_v120_signal,
    f14lq_f14_liquidity_profile_amihudmomsm_63d_jerk_v121_signal,
    f14lq_f14_liquidity_profile_liqvolsm_63d_jerk_v122_signal,
    f14lq_f14_liquidity_profile_liqvolsm_126d_jerk_v123_signal,
    f14lq_f14_liquidity_profile_liqcvsm_126d_jerk_v124_signal,
    f14lq_f14_liquidity_profile_illiqvolsm_252d_jerk_v125_signal,
    f14lq_f14_liquidity_profile_illiqvolsm_126d_jerk_v126_signal,
    f14lq_f14_liquidity_profile_liqvovsm_126d_jerk_v127_signal,
    f14lq_f14_liquidity_profile_liqvolratiosm_63d_jerk_v128_signal,
    f14lq_f14_liquidity_profile_liqdownvolsm_63d_jerk_v129_signal,
    f14lq_f14_liquidity_profile_flowimbsm_21d_jerk_v130_signal,
    f14lq_f14_liquidity_profile_flowimbsm_63d_jerk_v131_signal,
    f14lq_f14_liquidity_profile_liqflowvolsm_63d_jerk_v132_signal,
    f14lq_f14_liquidity_profile_liqhitratesm_63d_jerk_v133_signal,
    f14lq_f14_liquidity_profile_volretelastsm_63d_jerk_v134_signal,
    f14lq_f14_liquidity_profile_kylesm_63d_jerk_v135_signal,
    f14lq_f14_liquidity_profile_rollspreadsm_63d_jerk_v136_signal,
    f14lq_f14_liquidity_profile_rollspreadzsm_126d_jerk_v137_signal,
    f14lq_f14_liquidity_profile_hlspreadsm_21d_jerk_v138_signal,
    f14lq_f14_liquidity_profile_rangeilliqsm_63d_jerk_v139_signal,
    f14lq_f14_liquidity_profile_spreadcostsm_21d_jerk_v140_signal,
    f14lq_f14_liquidity_profile_fragilitysm_63d_jerk_v141_signal,
    f14lq_f14_liquidity_profile_tradabilitysm_63d_jerk_v142_signal,
    f14lq_f14_liquidity_profile_stressidxsm_126d_jerk_v143_signal,
    f14lq_f14_liquidity_profile_costcompositesm_63d_jerk_v144_signal,
    f14lq_f14_liquidity_profile_liqpxdivsm_63d_jerk_v145_signal,
    f14lq_f14_liquidity_profile_liqdriftsm_63d_jerk_v146_signal,
    f14lq_f14_liquidity_profile_realimpactsm_21d_jerk_v147_signal,
    f14lq_f14_liquidity_profile_liqmom63sm_63d_jerk_v148_signal,
    f14lq_f14_liquidity_profile_liqpervolsm_63d_jerk_v149_signal,
    f14lq_f14_liquidity_profile_liqherfsm_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_LIQUIDITY_PROFILE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f14_liquidity_profile_3rd_derivatives_001_150_claude: %d features pass" % n_features)
