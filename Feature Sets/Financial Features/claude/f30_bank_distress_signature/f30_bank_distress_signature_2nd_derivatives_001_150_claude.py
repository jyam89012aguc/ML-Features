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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f30_distress_proxy(equity, assets, w):
    eqr = equity / assets.replace(0, np.nan)
    return eqr - eqr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_roa_collapse(roa, w):
    return roa - roa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_distress_score(roa, de, w):
    score = roa - de / 10.0
    return score - score.rolling(w, min_periods=max(1, w // 2)).mean()


def f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v001_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v002_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v003_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v004_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v005_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v006_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v007_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v008_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v009_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v010_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v011_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v012_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v013_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v014_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v015_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v016_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v017_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v018_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v019_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v020_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v021_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v022_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v023_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v024_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v025_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v026_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v027_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v028_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v029_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v030_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v031_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v032_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v033_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v034_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v035_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v036_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v037_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v038_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v039_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v040_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v041_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v042_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v043_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v044_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v045_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v046_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v047_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v048_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v049_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v050_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v051_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v052_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v053_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v054_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v055_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v056_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v057_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v058_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v059_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v060_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v061_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v062_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v063_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v064_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v065_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v066_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v067_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v068_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v069_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v070_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v071_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v072_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v073_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v074_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v075_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v076_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v077_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v078_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v079_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v080_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v081_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v082_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v083_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v084_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v085_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v086_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v087_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v088_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v089_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v090_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v091_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v092_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v093_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v094_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v095_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v096_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v097_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v098_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v099_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v100_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v101_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v102_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v103_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v104_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v105_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v106_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v107_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v108_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v109_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v110_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v111_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v112_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v113_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v114_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v115_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v116_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v117_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v118_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v119_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v120_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v121_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v122_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v123_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v124_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v125_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v126_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v127_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v128_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v129_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v130_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v131_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v132_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v133_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v134_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v135_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v136_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v137_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v138_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v139_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v140_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v141_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v142_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v143_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v144_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v145_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v146_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v147_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v148_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v149_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v150_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v001_signal,
    f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v002_signal,
    f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v003_signal,
    f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v004_signal,
    f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v005_signal,
    f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v006_signal,
    f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v007_signal,
    f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v008_signal,
    f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v009_signal,
    f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v010_signal,
    f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v011_signal,
    f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v012_signal,
    f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v013_signal,
    f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v014_signal,
    f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v015_signal,
    f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v016_signal,
    f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v017_signal,
    f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v018_signal,
    f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v019_signal,
    f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v020_signal,
    f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v021_signal,
    f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v022_signal,
    f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v023_signal,
    f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v024_signal,
    f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v025_signal,
    f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v026_signal,
    f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v027_signal,
    f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v028_signal,
    f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v029_signal,
    f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v030_signal,
    f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v031_signal,
    f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v032_signal,
    f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v033_signal,
    f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v034_signal,
    f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v035_signal,
    f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v036_signal,
    f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v037_signal,
    f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v038_signal,
    f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v039_signal,
    f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v040_signal,
    f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v041_signal,
    f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v042_signal,
    f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v043_signal,
    f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v044_signal,
    f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v045_signal,
    f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v046_signal,
    f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v047_signal,
    f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v048_signal,
    f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v049_signal,
    f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v050_signal,
    f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v051_signal,
    f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v052_signal,
    f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v053_signal,
    f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v054_signal,
    f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v055_signal,
    f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v056_signal,
    f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v057_signal,
    f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v058_signal,
    f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v059_signal,
    f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v060_signal,
    f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v061_signal,
    f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v062_signal,
    f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v063_signal,
    f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v064_signal,
    f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v065_signal,
    f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v066_signal,
    f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v067_signal,
    f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v068_signal,
    f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v069_signal,
    f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v070_signal,
    f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v071_signal,
    f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v072_signal,
    f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v073_signal,
    f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v074_signal,
    f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v075_signal,
    f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v076_signal,
    f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v077_signal,
    f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v078_signal,
    f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v079_signal,
    f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v080_signal,
    f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v081_signal,
    f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v082_signal,
    f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v083_signal,
    f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v084_signal,
    f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v085_signal,
    f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v086_signal,
    f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v087_signal,
    f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v088_signal,
    f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v089_signal,
    f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v090_signal,
    f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v091_signal,
    f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v092_signal,
    f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v093_signal,
    f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v094_signal,
    f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v095_signal,
    f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v096_signal,
    f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v097_signal,
    f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v098_signal,
    f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v099_signal,
    f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v100_signal,
    f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v101_signal,
    f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v102_signal,
    f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v103_signal,
    f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v104_signal,
    f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v105_signal,
    f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v106_signal,
    f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v107_signal,
    f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v108_signal,
    f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v109_signal,
    f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v110_signal,
    f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v111_signal,
    f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v112_signal,
    f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v113_signal,
    f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v114_signal,
    f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v115_signal,
    f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v116_signal,
    f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v117_signal,
    f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v118_signal,
    f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v119_signal,
    f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v120_signal,
    f30bds_f30_bank_distress_signature_distproxrawsdn_21d_slope_v121_signal,
    f30bds_f30_bank_distress_signature_distproxsmsdn_21d_slope_v122_signal,
    f30bds_f30_bank_distress_signature_distproxzsdn_21d_slope_v123_signal,
    f30bds_f30_bank_distress_signature_distproxabssdn_21d_slope_v124_signal,
    f30bds_f30_bank_distress_signature_distproxscaledsdn_21d_slope_v125_signal,
    f30bds_f30_bank_distress_signature_distproxrawpct_21d_slope_v126_signal,
    f30bds_f30_bank_distress_signature_distproxsmpct_21d_slope_v127_signal,
    f30bds_f30_bank_distress_signature_distproxzpct_21d_slope_v128_signal,
    f30bds_f30_bank_distress_signature_distproxabspct_21d_slope_v129_signal,
    f30bds_f30_bank_distress_signature_distproxscaledpct_21d_slope_v130_signal,
    f30bds_f30_bank_distress_signature_roacollrawsdn_21d_slope_v131_signal,
    f30bds_f30_bank_distress_signature_roacollsmsdn_21d_slope_v132_signal,
    f30bds_f30_bank_distress_signature_roacollzsdn_21d_slope_v133_signal,
    f30bds_f30_bank_distress_signature_roacollabssdn_21d_slope_v134_signal,
    f30bds_f30_bank_distress_signature_roacollscaledsdn_21d_slope_v135_signal,
    f30bds_f30_bank_distress_signature_roacollrawpct_21d_slope_v136_signal,
    f30bds_f30_bank_distress_signature_roacollsmpct_21d_slope_v137_signal,
    f30bds_f30_bank_distress_signature_roacollzpct_21d_slope_v138_signal,
    f30bds_f30_bank_distress_signature_roacollabspct_21d_slope_v139_signal,
    f30bds_f30_bank_distress_signature_roacollscaledpct_21d_slope_v140_signal,
    f30bds_f30_bank_distress_signature_distscrawsdn_21d_slope_v141_signal,
    f30bds_f30_bank_distress_signature_distscsmsdn_21d_slope_v142_signal,
    f30bds_f30_bank_distress_signature_distsczsdn_21d_slope_v143_signal,
    f30bds_f30_bank_distress_signature_distscabssdn_21d_slope_v144_signal,
    f30bds_f30_bank_distress_signature_distscscaledsdn_21d_slope_v145_signal,
    f30bds_f30_bank_distress_signature_distscrawpct_21d_slope_v146_signal,
    f30bds_f30_bank_distress_signature_distscsmpct_21d_slope_v147_signal,
    f30bds_f30_bank_distress_signature_distsczpct_21d_slope_v148_signal,
    f30bds_f30_bank_distress_signature_distscabspct_21d_slope_v149_signal,
    f30bds_f30_bank_distress_signature_distscscaledpct_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_BANK_DISTRESS_SIGNATURE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"roa": roa, "de": de, "equity": equity, "assets": assets, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_distress_proxy", "_f30_roa_collapse", "_f30_distress_score")
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_bank_distress_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
