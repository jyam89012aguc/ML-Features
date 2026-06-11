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


# ===== folder domain primitives (gross-margin level and volatility) =====
def _f21_gm(gp, revenue):
    # gross margin level = gp / revenue
    return _safe_div(gp, revenue)


def _f21_gmvol(gp, revenue, w):
    # rolling volatility (std) of the gross margin series
    gm = _safe_div(gp, revenue)
    return gm.rolling(w, min_periods=max(2, w // 2)).std()


def _f21_cogratio(cor, revenue):
    # cost-of-revenue ratio = cor / revenue (1 - gross margin proxy)
    return _safe_div(cor, revenue)


def _f21_opratio(opex, revenue):
    # operating-expense intensity = opex / revenue
    return _safe_div(opex, revenue)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f21gm_f21_gross_margin_volatility_gmlevel_1d_jerk_v001_signal(gp, revenue):
    result = _f21_gm(gp, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_21d_jerk_v002_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_63d_jerk_v003_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_126d_jerk_v004_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_252d_jerk_v005_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_63d_jerk_v006_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_126d_jerk_v007_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_252d_jerk_v008_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_504d_jerk_v009_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_42d_jerk_v010_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogratio_1d_jerk_v011_signal(cor, revenue):
    result = _f21_cogratio(cor, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogsmooth_63d_jerk_v012_signal(cor, revenue):
    result = _mean(_f21_cogratio(cor, revenue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogsmooth_126d_jerk_v013_signal(cor, revenue):
    result = _mean(_f21_cogratio(cor, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogvol_252d_jerk_v014_signal(cor, revenue):
    result = _std(_f21_cogratio(cor, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogvol_126d_jerk_v015_signal(cor, revenue):
    result = _std(_f21_cogratio(cor, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_126d_jerk_v016_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_252d_jerk_v017_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_504d_jerk_v018_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_63d_jerk_v019_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogz_252d_jerk_v020_signal(cor, revenue):
    result = _z(_f21_cogratio(cor, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_63d_jerk_v021_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(63)) / 63.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_126d_jerk_v022_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(126)) / 126.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_252d_jerk_v023_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(252)) / 252.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcv_252d_jerk_v024_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 252), _mean(gm, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcv_126d_jerk_v025_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 126), _mean(gm, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcv_504d_jerk_v026_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 504), _mean(gm, 504).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcompress_252d_jerk_v027_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcompress_126d_jerk_v028_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcompress_63d_jerk_v029_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrelcomp_252d_jerk_v030_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 252)) - 1.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmskew_126d_jerk_v031_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmskew_252d_jerk_v032_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmkurt_252d_jerk_v033_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).kurt()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrank_126d_jerk_v034_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrank_252d_jerk_v035_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrank_504d_jerk_v036_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmiqr_252d_jerk_v037_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    result = q75 - q25
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmiqr_126d_jerk_v038_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(126, min_periods=42).quantile(0.75)
    q25 = gm.rolling(126, min_periods=42).quantile(0.25)
    result = q75 - q25
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_coststab_252d_jerk_v039_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 252), _std(cog, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_coststab_126d_jerk_v040_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 126), _std(cog, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmstab_252d_jerk_v041_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 252), _std(gm, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolratio_63_252_jerk_v042_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 63), _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolratio_126_504_jerk_v043_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 126), _f21_gmvol(gp, revenue, 504))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewm_63d_jerk_v044_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewm_126d_jerk_v045_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmvol_63d_jerk_v046_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=63, min_periods=21).std()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmvol_126d_jerk_v047_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=126, min_periods=42).std()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_21d_jerk_v048_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_63d_jerk_v049_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_126d_jerk_v050_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_252d_jerk_v051_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchgscaled_63d_jerk_v052_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(63), _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchgscaled_126d_jerk_v053_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(126), _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opratio_1d_jerk_v054_signal(opex, revenue):
    result = _f21_opratio(opex, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opsmooth_126d_jerk_v055_signal(opex, revenue):
    result = _mean(_f21_opratio(opex, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opvol_252d_jerk_v056_signal(opex, revenue):
    result = _std(_f21_opratio(opex, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opz_252d_jerk_v057_signal(opex, revenue):
    result = _z(_f21_opratio(opex, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmargin_1d_jerk_v058_signal(gp, revenue, opex):
    result = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmargin_126d_jerk_v059_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _mean(nm, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmarginvol_252d_jerk_v060_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _std(nm, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcogspread_1d_jerk_v061_signal(gp, revenue, cor):
    result = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_spread_1d_jerk_v062_signal(grossmargin, gp, revenue):
    result = grossmargin - _f21_gm(gp, revenue)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_z252_jerk_v063_signal(grossmargin, gp, revenue):
    result = _z(grossmargin, 252) + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_vol252_jerk_v064_signal(grossmargin, gp, revenue):
    result = _std(grossmargin, 252) + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsemidev_252d_jerk_v065_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 252)).clip(upper=0)
    result = (dev ** 2).rolling(252, min_periods=84).mean() ** 0.5
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsemidevup_252d_jerk_v066_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 252)).clip(lower=0)
    result = (dev ** 2).rolling(252, min_periods=84).mean() ** 0.5
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmad_126d_jerk_v067_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 126)).abs().rolling(126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmad_252d_jerk_v068_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 252)).abs().rolling(252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmstdmad_252d_jerk_v069_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    mad = (gm - _mean(gm, 252)).abs().rolling(252, min_periods=84).mean()
    result = _safe_div(_std(gm, 252), mad)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmtrendnoise_126d_jerk_v070_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(126)) / 126.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmtrendnoise_252d_jerk_v071_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(252)) / 252.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogchg_63d_jerk_v072_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogchg_126d_jerk_v073_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrankdev_252d_jerk_v074_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).rank(pct=True) - 0.5
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmz_126d_jerk_v075_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=126, min_periods=42).mean()
    sd = gm.ewm(span=126, min_periods=42).std()
    result = _safe_div(gm - m, sd)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_42d_jerk_v076_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_189d_jerk_v077_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsmooth_504d_jerk_v078_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_84d_jerk_v079_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_189d_jerk_v080_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_315d_jerk_v081_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvol_378d_jerk_v082_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_189d_jerk_v083_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_378d_jerk_v084_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmz_42d_jerk_v085_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_42d_jerk_v086_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(42)) / 42.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_189d_jerk_v087_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(189)) / 189.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmslope_504d_jerk_v088_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(504)) / 504.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcv_63d_jerk_v089_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 63), _mean(gm, 63).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcv_189d_jerk_v090_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 189), _mean(gm, 189).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcompress_504d_jerk_v091_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrelcomp_126d_jerk_v092_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 126)) - 1.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrelcomp_504d_jerk_v093_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 504)) - 1.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmskew_504d_jerk_v094_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmkurt_126d_jerk_v095_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmkurt_504d_jerk_v096_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).kurt()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrank_63d_jerk_v097_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(63, min_periods=21).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrank_189d_jerk_v098_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(189, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmiqr_504d_jerk_v099_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(504, min_periods=168).quantile(0.75)
    q25 = gm.rolling(504, min_periods=168).quantile(0.25)
    result = q75 - q25
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmidr_252d_jerk_v100_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q90 = gm.rolling(252, min_periods=84).quantile(0.90)
    q10 = gm.rolling(252, min_periods=84).quantile(0.10)
    result = q90 - q10
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmiqrnorm_252d_jerk_v101_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    med = gm.rolling(252, min_periods=84).median()
    result = _safe_div(q75 - q25, med.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_coststab_504d_jerk_v102_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 504), _std(cog, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmstab_126d_jerk_v103_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 126), _std(gm, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmstab_504d_jerk_v104_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 504), _std(gm, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolratio_42_126_jerk_v105_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 42), _f21_gmvol(gp, revenue, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolratio_84_252_jerk_v106_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 84), _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewm_252d_jerk_v107_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmvol_252d_jerk_v108_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=252, min_periods=84).std()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmvol_42d_jerk_v109_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=42, min_periods=21).std()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_42d_jerk_v110_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_189d_jerk_v111_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchg_504d_jerk_v112_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmchgscaled_252d_jerk_v113_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(252), _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmaccel_63_126_jerk_v114_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(63)) - (gm.shift(63) - gm.shift(126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmaccel_126_252_jerk_v115_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(126)) - (gm.shift(126) - gm.shift(252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opsmooth_252d_jerk_v116_signal(opex, revenue):
    result = _mean(_f21_opratio(opex, revenue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opvol_126d_jerk_v117_signal(opex, revenue):
    result = _std(_f21_opratio(opex, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opchg_126d_jerk_v118_signal(opex, revenue):
    op = _f21_opratio(opex, revenue)
    result = op - op.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_opcv_252d_jerk_v119_signal(opex, revenue):
    op = _f21_opratio(opex, revenue)
    result = _safe_div(_std(op, 252), _mean(op, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmarginz_252d_jerk_v120_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _z(nm, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmarginslope_126d_jerk_v121_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = (nm - nm.shift(126)) / 126.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_netmargincv_252d_jerk_v122_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _safe_div(_std(nm, 252), _mean(nm, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcogspread_126d_jerk_v123_signal(gp, revenue, cor):
    sp = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    result = _mean(sp, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcogspreadvol_252d_jerk_v124_signal(gp, revenue, cor):
    sp = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    result = _std(sp, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmcogprod_126d_jerk_v125_signal(gp, revenue, cor):
    inter = _f21_gm(gp, revenue) * _f21_cogratio(cor, revenue)
    result = _mean(inter, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_compress_252d_jerk_v126_signal(grossmargin, gp, revenue):
    result = (grossmargin - _mean(grossmargin, 252)) + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_cv_252d_jerk_v127_signal(grossmargin, gp, revenue):
    cv = _safe_div(_std(grossmargin, 252), _mean(grossmargin, 252).abs())
    result = cv + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_slope_126d_jerk_v128_signal(grossmargin, gp, revenue):
    slope = (grossmargin - grossmargin.shift(126)) / 126.0
    result = slope + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmreported_rank_252d_jerk_v129_signal(grossmargin, gp, revenue):
    rk = grossmargin.rolling(252, min_periods=84).rank(pct=True)
    result = rk + _f21_gm(gp, revenue) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsemidev_126d_jerk_v130_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 126)).clip(upper=0)
    result = (dev ** 2).rolling(126, min_periods=42).mean() ** 0.5
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmsemiasym_252d_jerk_v131_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    c = gm - _mean(gm, 252)
    up = (c.clip(lower=0) ** 2).rolling(252, min_periods=84).mean() ** 0.5
    dn = (c.clip(upper=0) ** 2).rolling(252, min_periods=84).mean() ** 0.5
    result = up - dn
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmad_63d_jerk_v132_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 63)).abs().rolling(63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmad_504d_jerk_v133_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 504)).abs().rolling(504, min_periods=168).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmtrendnoise_63d_jerk_v134_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(63)) / 63.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmtrendnoise_504d_jerk_v135_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(504)) / 504.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogz_126d_jerk_v136_signal(cor, revenue):
    result = _z(_f21_cogratio(cor, revenue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogcv_252d_jerk_v137_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_std(cog, 252), _mean(cog, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogrank_252d_jerk_v138_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_cogchg_252d_jerk_v139_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmz_63d_jerk_v140_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=63, min_periods=21).mean()
    sd = gm.ewm(span=63, min_periods=21).std()
    result = _safe_div(gm - m, sd)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmz_252d_jerk_v141_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=252, min_periods=84).mean()
    sd = gm.ewm(span=252, min_periods=84).std()
    result = _safe_div(gm - m, sd)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmrankdev_126d_jerk_v142_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolnorm_126d_jerk_v143_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_f21_gmvol(gp, revenue, 126), _mean(gm, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolnorm_252d_jerk_v144_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_f21_gmvol(gp, revenue, 252), _mean(gm, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmiqrvol_252d_jerk_v145_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    result = _safe_div(q75 - q25, _f21_gmvol(gp, revenue, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmewmcompress_126d_jerk_v146_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmeanspread_63_252_jerk_v147_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _mean(gm, 63) - _mean(gm, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmmeanspread_21_126_jerk_v148_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _mean(gm, 21) - _mean(gm, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_gmvolchg_252d_jerk_v149_signal(gp, revenue):
    v = _f21_gmvol(gp, revenue, 252)
    result = v - v.shift(126)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gm_f21_gross_margin_volatility_blend_quality_jerk_v150_signal(gp, revenue, cor):
    gm = _f21_gm(gp, revenue)
    gmz = _z(gm, 252)
    stab = _safe_div(_mean(gm, 252), _std(gm, 252))
    cog = _f21_cogratio(cor, revenue)
    cogcv = _safe_div(_std(cog, 252), _mean(cog, 252).abs())
    result = gmz + stab - cogcv
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f21gm_f21_gross_margin_volatility_gmlevel_1d_jerk_v001_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_21d_jerk_v002_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_63d_jerk_v003_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_126d_jerk_v004_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_252d_jerk_v005_signal,    f21gm_f21_gross_margin_volatility_gmvol_63d_jerk_v006_signal,    f21gm_f21_gross_margin_volatility_gmvol_126d_jerk_v007_signal,    f21gm_f21_gross_margin_volatility_gmvol_252d_jerk_v008_signal,    f21gm_f21_gross_margin_volatility_gmvol_504d_jerk_v009_signal,    f21gm_f21_gross_margin_volatility_gmvol_42d_jerk_v010_signal,    f21gm_f21_gross_margin_volatility_cogratio_1d_jerk_v011_signal,    f21gm_f21_gross_margin_volatility_cogsmooth_63d_jerk_v012_signal,    f21gm_f21_gross_margin_volatility_cogsmooth_126d_jerk_v013_signal,    f21gm_f21_gross_margin_volatility_cogvol_252d_jerk_v014_signal,    f21gm_f21_gross_margin_volatility_cogvol_126d_jerk_v015_signal,    f21gm_f21_gross_margin_volatility_gmz_126d_jerk_v016_signal,    f21gm_f21_gross_margin_volatility_gmz_252d_jerk_v017_signal,    f21gm_f21_gross_margin_volatility_gmz_504d_jerk_v018_signal,    f21gm_f21_gross_margin_volatility_gmz_63d_jerk_v019_signal,    f21gm_f21_gross_margin_volatility_cogz_252d_jerk_v020_signal,    f21gm_f21_gross_margin_volatility_gmslope_63d_jerk_v021_signal,    f21gm_f21_gross_margin_volatility_gmslope_126d_jerk_v022_signal,    f21gm_f21_gross_margin_volatility_gmslope_252d_jerk_v023_signal,    f21gm_f21_gross_margin_volatility_gmcv_252d_jerk_v024_signal,    f21gm_f21_gross_margin_volatility_gmcv_126d_jerk_v025_signal,    f21gm_f21_gross_margin_volatility_gmcv_504d_jerk_v026_signal,    f21gm_f21_gross_margin_volatility_gmcompress_252d_jerk_v027_signal,    f21gm_f21_gross_margin_volatility_gmcompress_126d_jerk_v028_signal,    f21gm_f21_gross_margin_volatility_gmcompress_63d_jerk_v029_signal,    f21gm_f21_gross_margin_volatility_gmrelcomp_252d_jerk_v030_signal,    f21gm_f21_gross_margin_volatility_gmskew_126d_jerk_v031_signal,    f21gm_f21_gross_margin_volatility_gmskew_252d_jerk_v032_signal,    f21gm_f21_gross_margin_volatility_gmkurt_252d_jerk_v033_signal,    f21gm_f21_gross_margin_volatility_gmrank_126d_jerk_v034_signal,    f21gm_f21_gross_margin_volatility_gmrank_252d_jerk_v035_signal,    f21gm_f21_gross_margin_volatility_gmrank_504d_jerk_v036_signal,    f21gm_f21_gross_margin_volatility_gmiqr_252d_jerk_v037_signal,    f21gm_f21_gross_margin_volatility_gmiqr_126d_jerk_v038_signal,    f21gm_f21_gross_margin_volatility_coststab_252d_jerk_v039_signal,    f21gm_f21_gross_margin_volatility_coststab_126d_jerk_v040_signal,    f21gm_f21_gross_margin_volatility_gmstab_252d_jerk_v041_signal,    f21gm_f21_gross_margin_volatility_gmvolratio_63_252_jerk_v042_signal,    f21gm_f21_gross_margin_volatility_gmvolratio_126_504_jerk_v043_signal,    f21gm_f21_gross_margin_volatility_gmewm_63d_jerk_v044_signal,    f21gm_f21_gross_margin_volatility_gmewm_126d_jerk_v045_signal,    f21gm_f21_gross_margin_volatility_gmewmvol_63d_jerk_v046_signal,    f21gm_f21_gross_margin_volatility_gmewmvol_126d_jerk_v047_signal,    f21gm_f21_gross_margin_volatility_gmchg_21d_jerk_v048_signal,    f21gm_f21_gross_margin_volatility_gmchg_63d_jerk_v049_signal,    f21gm_f21_gross_margin_volatility_gmchg_126d_jerk_v050_signal,    f21gm_f21_gross_margin_volatility_gmchg_252d_jerk_v051_signal,    f21gm_f21_gross_margin_volatility_gmchgscaled_63d_jerk_v052_signal,    f21gm_f21_gross_margin_volatility_gmchgscaled_126d_jerk_v053_signal,    f21gm_f21_gross_margin_volatility_opratio_1d_jerk_v054_signal,    f21gm_f21_gross_margin_volatility_opsmooth_126d_jerk_v055_signal,    f21gm_f21_gross_margin_volatility_opvol_252d_jerk_v056_signal,    f21gm_f21_gross_margin_volatility_opz_252d_jerk_v057_signal,    f21gm_f21_gross_margin_volatility_netmargin_1d_jerk_v058_signal,    f21gm_f21_gross_margin_volatility_netmargin_126d_jerk_v059_signal,    f21gm_f21_gross_margin_volatility_netmarginvol_252d_jerk_v060_signal,    f21gm_f21_gross_margin_volatility_gmcogspread_1d_jerk_v061_signal,    f21gm_f21_gross_margin_volatility_gmreported_spread_1d_jerk_v062_signal,    f21gm_f21_gross_margin_volatility_gmreported_z252_jerk_v063_signal,    f21gm_f21_gross_margin_volatility_gmreported_vol252_jerk_v064_signal,    f21gm_f21_gross_margin_volatility_gmsemidev_252d_jerk_v065_signal,    f21gm_f21_gross_margin_volatility_gmsemidevup_252d_jerk_v066_signal,    f21gm_f21_gross_margin_volatility_gmmad_126d_jerk_v067_signal,    f21gm_f21_gross_margin_volatility_gmmad_252d_jerk_v068_signal,    f21gm_f21_gross_margin_volatility_gmstdmad_252d_jerk_v069_signal,    f21gm_f21_gross_margin_volatility_gmtrendnoise_126d_jerk_v070_signal,    f21gm_f21_gross_margin_volatility_gmtrendnoise_252d_jerk_v071_signal,    f21gm_f21_gross_margin_volatility_cogchg_63d_jerk_v072_signal,    f21gm_f21_gross_margin_volatility_cogchg_126d_jerk_v073_signal,    f21gm_f21_gross_margin_volatility_gmrankdev_252d_jerk_v074_signal,    f21gm_f21_gross_margin_volatility_gmewmz_126d_jerk_v075_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_42d_jerk_v076_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_189d_jerk_v077_signal,    f21gm_f21_gross_margin_volatility_gmsmooth_504d_jerk_v078_signal,    f21gm_f21_gross_margin_volatility_gmvol_84d_jerk_v079_signal,    f21gm_f21_gross_margin_volatility_gmvol_189d_jerk_v080_signal,    f21gm_f21_gross_margin_volatility_gmvol_315d_jerk_v081_signal,    f21gm_f21_gross_margin_volatility_gmvol_378d_jerk_v082_signal,    f21gm_f21_gross_margin_volatility_gmz_189d_jerk_v083_signal,    f21gm_f21_gross_margin_volatility_gmz_378d_jerk_v084_signal,    f21gm_f21_gross_margin_volatility_gmz_42d_jerk_v085_signal,    f21gm_f21_gross_margin_volatility_gmslope_42d_jerk_v086_signal,    f21gm_f21_gross_margin_volatility_gmslope_189d_jerk_v087_signal,    f21gm_f21_gross_margin_volatility_gmslope_504d_jerk_v088_signal,    f21gm_f21_gross_margin_volatility_gmcv_63d_jerk_v089_signal,    f21gm_f21_gross_margin_volatility_gmcv_189d_jerk_v090_signal,    f21gm_f21_gross_margin_volatility_gmcompress_504d_jerk_v091_signal,    f21gm_f21_gross_margin_volatility_gmrelcomp_126d_jerk_v092_signal,    f21gm_f21_gross_margin_volatility_gmrelcomp_504d_jerk_v093_signal,    f21gm_f21_gross_margin_volatility_gmskew_504d_jerk_v094_signal,    f21gm_f21_gross_margin_volatility_gmkurt_126d_jerk_v095_signal,    f21gm_f21_gross_margin_volatility_gmkurt_504d_jerk_v096_signal,    f21gm_f21_gross_margin_volatility_gmrank_63d_jerk_v097_signal,    f21gm_f21_gross_margin_volatility_gmrank_189d_jerk_v098_signal,    f21gm_f21_gross_margin_volatility_gmiqr_504d_jerk_v099_signal,    f21gm_f21_gross_margin_volatility_gmidr_252d_jerk_v100_signal,    f21gm_f21_gross_margin_volatility_gmiqrnorm_252d_jerk_v101_signal,    f21gm_f21_gross_margin_volatility_coststab_504d_jerk_v102_signal,    f21gm_f21_gross_margin_volatility_gmstab_126d_jerk_v103_signal,    f21gm_f21_gross_margin_volatility_gmstab_504d_jerk_v104_signal,    f21gm_f21_gross_margin_volatility_gmvolratio_42_126_jerk_v105_signal,    f21gm_f21_gross_margin_volatility_gmvolratio_84_252_jerk_v106_signal,    f21gm_f21_gross_margin_volatility_gmewm_252d_jerk_v107_signal,    f21gm_f21_gross_margin_volatility_gmewmvol_252d_jerk_v108_signal,    f21gm_f21_gross_margin_volatility_gmewmvol_42d_jerk_v109_signal,    f21gm_f21_gross_margin_volatility_gmchg_42d_jerk_v110_signal,    f21gm_f21_gross_margin_volatility_gmchg_189d_jerk_v111_signal,    f21gm_f21_gross_margin_volatility_gmchg_504d_jerk_v112_signal,    f21gm_f21_gross_margin_volatility_gmchgscaled_252d_jerk_v113_signal,    f21gm_f21_gross_margin_volatility_gmaccel_63_126_jerk_v114_signal,    f21gm_f21_gross_margin_volatility_gmaccel_126_252_jerk_v115_signal,    f21gm_f21_gross_margin_volatility_opsmooth_252d_jerk_v116_signal,    f21gm_f21_gross_margin_volatility_opvol_126d_jerk_v117_signal,    f21gm_f21_gross_margin_volatility_opchg_126d_jerk_v118_signal,    f21gm_f21_gross_margin_volatility_opcv_252d_jerk_v119_signal,    f21gm_f21_gross_margin_volatility_netmarginz_252d_jerk_v120_signal,    f21gm_f21_gross_margin_volatility_netmarginslope_126d_jerk_v121_signal,    f21gm_f21_gross_margin_volatility_netmargincv_252d_jerk_v122_signal,    f21gm_f21_gross_margin_volatility_gmcogspread_126d_jerk_v123_signal,    f21gm_f21_gross_margin_volatility_gmcogspreadvol_252d_jerk_v124_signal,    f21gm_f21_gross_margin_volatility_gmcogprod_126d_jerk_v125_signal,    f21gm_f21_gross_margin_volatility_gmreported_compress_252d_jerk_v126_signal,    f21gm_f21_gross_margin_volatility_gmreported_cv_252d_jerk_v127_signal,    f21gm_f21_gross_margin_volatility_gmreported_slope_126d_jerk_v128_signal,    f21gm_f21_gross_margin_volatility_gmreported_rank_252d_jerk_v129_signal,    f21gm_f21_gross_margin_volatility_gmsemidev_126d_jerk_v130_signal,    f21gm_f21_gross_margin_volatility_gmsemiasym_252d_jerk_v131_signal,    f21gm_f21_gross_margin_volatility_gmmad_63d_jerk_v132_signal,    f21gm_f21_gross_margin_volatility_gmmad_504d_jerk_v133_signal,    f21gm_f21_gross_margin_volatility_gmtrendnoise_63d_jerk_v134_signal,    f21gm_f21_gross_margin_volatility_gmtrendnoise_504d_jerk_v135_signal,    f21gm_f21_gross_margin_volatility_cogz_126d_jerk_v136_signal,    f21gm_f21_gross_margin_volatility_cogcv_252d_jerk_v137_signal,    f21gm_f21_gross_margin_volatility_cogrank_252d_jerk_v138_signal,    f21gm_f21_gross_margin_volatility_cogchg_252d_jerk_v139_signal,    f21gm_f21_gross_margin_volatility_gmewmz_63d_jerk_v140_signal,    f21gm_f21_gross_margin_volatility_gmewmz_252d_jerk_v141_signal,    f21gm_f21_gross_margin_volatility_gmrankdev_126d_jerk_v142_signal,    f21gm_f21_gross_margin_volatility_gmvolnorm_126d_jerk_v143_signal,    f21gm_f21_gross_margin_volatility_gmvolnorm_252d_jerk_v144_signal,    f21gm_f21_gross_margin_volatility_gmiqrvol_252d_jerk_v145_signal,    f21gm_f21_gross_margin_volatility_gmewmcompress_126d_jerk_v146_signal,    f21gm_f21_gross_margin_volatility_gmmeanspread_63_252_jerk_v147_signal,    f21gm_f21_gross_margin_volatility_gmmeanspread_21_126_jerk_v148_signal,    f21gm_f21_gross_margin_volatility_gmvolchg_252d_jerk_v149_signal,    f21gm_f21_gross_margin_volatility_blend_quality_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_GROSS_MARGIN_VOLATILITY_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f21_gm', '_f21_gmvol', '_f21_cogratio', '_f21_opratio')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f21_gross_margin_volatility_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
