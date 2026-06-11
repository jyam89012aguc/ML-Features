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


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f34_distress_proxy(debt, ebitda, w):
    ratio = debt / ebitda.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()

def _f34_collapse_risk(de, ebitdamargin, w):
    de_z = (de - de.rolling(w, min_periods=max(1, w // 2)).mean()) / de.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    m_drop = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).max() - ebitdamargin
    return de_z + m_drop

def _f34_cyclical_stress(debt, fcf, ebitda, w):
    cover = fcf / debt.replace(0, np.nan).abs()
    cover_m = cover.rolling(w, min_periods=max(1, w // 2)).mean()
    e_ratio = ebitda / debt.replace(0, np.nan).abs()
    return e_ratio.rolling(w, min_periods=max(1, w // 2)).mean() - cover_m


def f34cds_f34_commodity_distress_signature_distprx_ident_xc_5d_base_v001_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_5d_base_v002_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_5d_base_v003_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_5d_base_v004_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_5d_base_v005_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_5d_base_v006_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_10d_base_v007_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_10d_base_v008_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_10d_base_v009_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_10d_base_v010_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_10d_base_v011_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_10d_base_v012_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_21d_base_v013_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_21d_base_v014_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_21d_base_v015_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_21d_base_v016_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_21d_base_v017_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_21d_base_v018_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_42d_base_v019_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_42d_base_v020_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_42d_base_v021_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_42d_base_v022_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_42d_base_v023_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_42d_base_v024_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_63d_base_v025_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_63d_base_v026_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_63d_base_v027_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_63d_base_v028_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_63d_base_v029_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_63d_base_v030_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 63)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_126d_base_v031_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_126d_base_v032_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_126d_base_v033_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_126d_base_v034_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_126d_base_v035_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_126d_base_v036_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 126)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_189d_base_v037_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_189d_base_v038_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_189d_base_v039_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_189d_base_v040_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_189d_base_v041_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_189d_base_v042_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 189)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_252d_base_v043_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_252d_base_v044_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_252d_base_v045_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_252d_base_v046_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_252d_base_v047_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_252d_base_v048_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 252)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xc_378d_base_v049_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_378d_base_v050_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_378d_base_v051_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_378d_base_v052_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_378d_base_v053_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_378d_base_v054_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 378)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xc_5d_base_v055_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_5d_base_v056_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_5d_base_v057_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_5d_base_v058_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_5d_base_v059_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_5d_base_v060_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 5)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xc_10d_base_v061_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_10d_base_v062_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_10d_base_v063_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_10d_base_v064_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_10d_base_v065_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_10d_base_v066_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 10)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xc_21d_base_v067_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_21d_base_v068_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_21d_base_v069_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_21d_base_v070_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_21d_base_v071_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_21d_base_v072_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 21)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xc_42d_base_v073_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_42d_base_v074_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_42d_base_v075_signal(debt, ebitda, closeadj):
    base = _f34_distress_proxy(debt, ebitda, 42)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_5d_base_v001_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_5d_base_v002_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_5d_base_v003_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_5d_base_v004_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_5d_base_v005_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_5d_base_v006_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_10d_base_v007_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_10d_base_v008_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_10d_base_v009_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_10d_base_v010_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_10d_base_v011_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_10d_base_v012_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_21d_base_v013_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_21d_base_v014_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_21d_base_v015_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_21d_base_v016_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_21d_base_v017_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_21d_base_v018_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_42d_base_v019_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_42d_base_v020_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_42d_base_v021_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_42d_base_v022_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_42d_base_v023_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_42d_base_v024_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_63d_base_v025_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_63d_base_v026_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_63d_base_v027_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_63d_base_v028_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_63d_base_v029_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_63d_base_v030_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_126d_base_v031_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_126d_base_v032_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_126d_base_v033_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_126d_base_v034_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_126d_base_v035_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_126d_base_v036_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_189d_base_v037_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_189d_base_v038_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_189d_base_v039_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_189d_base_v040_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_189d_base_v041_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_189d_base_v042_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_252d_base_v043_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_252d_base_v044_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_252d_base_v045_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_252d_base_v046_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_252d_base_v047_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_252d_base_v048_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xc_378d_base_v049_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc21_378d_base_v050_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc63_378d_base_v051_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xmc252_378d_base_v052_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema21c_378d_base_v053_signal,
    f34cds_f34_commodity_distress_signature_distprx_ident_xema63c_378d_base_v054_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xc_5d_base_v055_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_5d_base_v056_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_5d_base_v057_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_5d_base_v058_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_5d_base_v059_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_5d_base_v060_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xc_10d_base_v061_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_10d_base_v062_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_10d_base_v063_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_10d_base_v064_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_10d_base_v065_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_10d_base_v066_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xc_21d_base_v067_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_21d_base_v068_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_21d_base_v069_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc252_21d_base_v070_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema21c_21d_base_v071_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xema63c_21d_base_v072_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xc_42d_base_v073_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc21_42d_base_v074_signal,
    f34cds_f34_commodity_distress_signature_distprx_absv_xmc63_42d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_COMMODITY_DISTRESS_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "netinc": netinc,
        "fcf": fcf,
        "capex": capex,
        "debt": debt,
        "ebitdamargin": ebitdamargin,
        "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_distress_proxy", "_f34_collapse_risk", "_f34_cyclical_stress",)
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
    print(f"OK f34_commodity_distress_signature_001_075_claude: {n_features} features pass")
