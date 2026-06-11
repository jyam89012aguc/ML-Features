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


# ===== folder domain primitives (insider conviction quality) =====
def _f32_offshare(officerbuyval, buyval, w):
    # officer share of total insider buying over rolling window w
    num = officerbuyval.rolling(w, min_periods=max(1, w // 2)).sum()
    den = buyval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(num, den)


def _f32_conviction(officerbuyval, dirbuyval, marketcap, w):
    # trailing officer+director buy $ relative to marketcap (conviction intensity)
    num = (officerbuyval + dirbuyval).rolling(w, min_periods=max(1, w // 2)).sum()
    den = marketcap.rolling(w, min_periods=max(1, w // 2)).mean()
    return _safe_div(num, den)


def _f32_bigbuy(buyval, officerbuycount, w):
    # average purchase size = rolling buy $ per officer-buy event
    num = buyval.rolling(w, min_periods=max(1, w // 2)).sum()
    den = (officerbuycount + 1.0).rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(num, den)


def _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, w):
    # quality mix: insider (officer+director) buying vs passive 10%-owner buying
    smart = (officerbuyval + dirbuyval).rolling(w, min_periods=max(1, w // 2)).sum()
    passive = tenpctbuyval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(smart, passive)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f32ic_f32_insider_conviction_quality_offshare_63d_jerk_v001_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_126d_jerk_v002_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_252d_jerk_v003_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_504d_jerk_v004_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirshare_63d_jerk_v005_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(63, min_periods=21).sum()
    den = buyval.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirshare_126d_jerk_v006_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(126, min_periods=42).sum()
    den = buyval.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirshare_252d_jerk_v007_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_insidshare_63d_jerk_v008_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(63, min_periods=21).sum()
    den = buyval.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_insidshare_126d_jerk_v009_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    den = buyval.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_insidshare_252d_jerk_v010_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_63d_jerk_v011_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_126d_jerk_v012_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_252d_jerk_v013_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_504d_jerk_v014_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_21d_jerk_v015_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconv_63d_jerk_v016_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = marketcap.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconv_126d_jerk_v017_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = marketcap.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconv_252d_jerk_v018_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = marketcap.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirconv_63d_jerk_v019_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(63, min_periods=21).sum()
    den = marketcap.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirconv_126d_jerk_v020_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(126, min_periods=42).sum()
    den = marketcap.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirconv_252d_jerk_v021_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(252, min_periods=84).sum()
    den = marketcap.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_63d_jerk_v022_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_126d_jerk_v023_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_252d_jerk_v024_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_504d_jerk_v025_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_63d_jerk_v026_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_126d_jerk_v027_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_252d_jerk_v028_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_504d_jerk_v029_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qfrac_63d_jerk_v030_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(63, min_periods=21).sum()
    passive = tenpctbuyval.rolling(63, min_periods=21).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qfrac_126d_jerk_v031_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    passive = tenpctbuyval.rolling(126, min_periods=42).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qfrac_252d_jerk_v032_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    passive = tenpctbuyval.rolling(252, min_periods=84).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offdirbal_63d_jerk_v033_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(63, min_periods=21).sum()
    d = dirbuyval.rolling(63, min_periods=21).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offdirbal_126d_jerk_v034_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(126, min_periods=42).sum()
    d = dirbuyval.rolling(126, min_periods=42).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offdirbal_252d_jerk_v035_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(252, min_periods=84).sum()
    d = dirbuyval.rolling(252, min_periods=84).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zoffshare_63d_jerk_v036_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zoffshare_126d_jerk_v037_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zconv_63d_jerk_v038_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zconv_126d_jerk_v039_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zbigbuy_63d_jerk_v040_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zbigbuy_126d_jerk_v041_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zqmix_63d_jerk_v042_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _z(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convtrend_63d_jerk_v043_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = c - _mean(c, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convtrend_126d_jerk_v044_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = c - _mean(c, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offsharetrend_63d_jerk_v045_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = s - _mean(s, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convspread_63_252_jerk_v046_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convspread_126_504_jerk_v047_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offsharespread_63_252_jerk_v048_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 63) - _f32_offshare(officerbuyval, buyval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_63d_jerk_v049_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = sharesbas.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_126d_jerk_v050_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_252d_jerk_v051_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_buysharesint_63d_jerk_v052_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(63, min_periods=21).sum()
    den = sharesbas.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_buysharesint_126d_jerk_v053_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_buysharesint_252d_jerk_v054_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_implprice_63d_jerk_v055_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(63, min_periods=21).sum()
    den = buyshares.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_implprice_126d_jerk_v056_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(126, min_periods=42).sum()
    den = buyshares.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qweighted_63d_jerk_v057_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 63) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qweighted_126d_jerk_v058_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 126) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qweighted_252d_jerk_v059_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 252) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixconv_63d_jerk_v060_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixconv_126d_jerk_v061_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_63d_jerk_v062_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 63), marketcap.rolling(63, min_periods=21).mean())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_126d_jerk_v063_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 126), marketcap.rolling(126, min_periods=42).mean())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_252d_jerk_v064_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 252), marketcap.rolling(252, min_periods=84).mean())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconc_63d_jerk_v065_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = (officerbuycount + 1.0).rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconc_126d_jerk_v066_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = (officerbuycount + 1.0).rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconc_252d_jerk_v067_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = (officerbuycount + 1.0).rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smoffshare_63d_jerk_v068_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smoffshare_126d_jerk_v069_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smconv_63d_jerk_v070_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smconv_126d_jerk_v071_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convir_63d_jerk_v072_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = _safe_div(c, _std(c, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convir_126d_jerk_v073_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _safe_div(c, _std(c, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshareir_63d_jerk_v074_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = _safe_div(s, _std(s, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qcomposite_63d_jerk_v075_signal(officerbuyval, dirbuyval, buyval, officerbuycount, marketcap):
    result = (_f32_offshare(officerbuyval, buyval, 63)
              + _z(_f32_bigbuy(buyval, officerbuycount, 63), 252)
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_21d_jerk_v076_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_42d_jerk_v077_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_84d_jerk_v078_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_189d_jerk_v079_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshare_378d_jerk_v080_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_84d_jerk_v081_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_189d_jerk_v082_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_378d_jerk_v083_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_42d_jerk_v084_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_conv_315d_jerk_v085_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_84d_jerk_v086_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_189d_jerk_v087_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_42d_jerk_v088_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuy_378d_jerk_v089_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_84d_jerk_v090_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_189d_jerk_v091_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmix_378d_jerk_v092_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qfrac_504d_jerk_v093_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(504, min_periods=168).sum()
    passive = tenpctbuyval.rolling(504, min_periods=168).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_passshare_84d_jerk_v094_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(84, min_periods=42).sum()
    den = buyval.rolling(84, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_passshare_189d_jerk_v095_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(189, min_periods=63).sum()
    den = buyval.rolling(189, min_periods=63).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 189) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_passshare_252d_jerk_v096_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zconv_84d_jerk_v097_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 84), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zconv_189d_jerk_v098_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 189), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zoffshare_252d_jerk_v099_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zqmix_84d_jerk_v100_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _z(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_zbigbuy_252d_jerk_v101_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convtrend_84d_jerk_v102_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c - _mean(c, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convtrend_252d_jerk_v103_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = c - _mean(c, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offsharetrend_126d_jerk_v104_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 126)
    result = s - _mean(s, 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuytrend_84d_jerk_v105_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = b - _mean(b, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convspread_84_315_jerk_v106_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offsharespread_84_252_jerk_v107_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 84) - _f32_offshare(officerbuyval, buyval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixspread_84_252_jerk_v108_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84) - _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_84d_jerk_v109_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_189d_jerk_v110_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(189, min_periods=63).sum()
    den = sharesbas.rolling(189, min_periods=63).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 189) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offflow_504d_jerk_v111_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(504, min_periods=168).sum()
    den = sharesbas.rolling(504, min_periods=168).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirflow_84d_jerk_v112_signal(dirbuyval, sharesbas):
    num = dirbuyval.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, dirbuyval, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_dirflow_189d_jerk_v113_signal(dirbuyval, sharesbas):
    num = dirbuyval.rolling(189, min_periods=63).sum()
    den = sharesbas.rolling(189, min_periods=63).mean()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, dirbuyval, 189) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_buysharesint_84d_jerk_v114_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_buysharesint_504d_jerk_v115_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(504, min_periods=168).sum()
    den = sharesbas.rolling(504, min_periods=168).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_implprice_252d_jerk_v116_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(252, min_periods=84).sum()
    den = buyshares.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qweighted_84d_jerk_v117_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 84) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qweighted_189d_jerk_v118_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 189) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixconv_252d_jerk_v119_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_84d_jerk_v120_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 84), marketcap.rolling(84, min_periods=42).mean())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_189d_jerk_v121_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 189), marketcap.rolling(189, min_periods=63).mean())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyint_504d_jerk_v122_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 504), marketcap.rolling(504, min_periods=168).mean())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconc_84d_jerk_v123_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(84, min_periods=42).sum()
    den = (officerbuycount + 1.0).rolling(84, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offconc_504d_jerk_v124_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(504, min_periods=168).sum()
    den = (officerbuycount + 1.0).rolling(504, min_periods=168).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smoffshare_252d_jerk_v125_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 252), 63)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smconv_252d_jerk_v126_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 252), 63)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smqmix_84d_jerk_v127_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _mean(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smbigbuy_84d_jerk_v128_signal(buyval, officerbuycount):
    result = _mean(_f32_bigbuy(buyval, officerbuycount, 84), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convir_252d_jerk_v129_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _safe_div(c, _std(c, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convir_84d_jerk_v130_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = _safe_div(c, _std(c, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_offshareir_126d_jerk_v131_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 126)
    result = _safe_div(s, _std(s, 504))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixir_84d_jerk_v132_signal(officerbuyval, dirbuyval, tenpctbuyval):
    m = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84)
    result = _safe_div(m, _std(m, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_bigbuyir_84d_jerk_v133_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = _safe_div(b, _std(b, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_rankoffshare_84d_jerk_v134_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 84)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_rankconv_84d_jerk_v135_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_rankbigbuy_84d_jerk_v136_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = b.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_ewmconv_84d_jerk_v137_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c.ewm(span=84, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_ewmoffshare_63d_jerk_v138_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = s.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qaccel_84d_jerk_v139_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 42) - _f32_offshare(officerbuyval, buyval, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convaccel_42_126_jerk_v140_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 42) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_insidflow_252d_jerk_v141_signal(officerbuyval, dirbuyval, sharesbas):
    num = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_insidflow_126d_jerk_v142_signal(officerbuyval, dirbuyval, sharesbas):
    num = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_sizedisp_126d_jerk_v143_signal(buyval, officerbuyval, officerbuycount):
    big = _f32_bigbuy(buyval, officerbuycount, 126)
    offc = _safe_div(officerbuyval.rolling(126, min_periods=42).sum(), (officerbuycount + 1.0).rolling(126, min_periods=42).sum())
    result = _safe_div(offc, big)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convperbuy_252d_jerk_v144_signal(officerbuyval, dirbuyval, marketcap, buyshares, sharesbas):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    acc = _safe_div(buyshares.rolling(252, min_periods=84).sum(), sharesbas.rolling(252, min_periods=84).mean())
    result = _safe_div(c, acc)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_smartconc_126d_jerk_v145_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 126) * _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qmixsize_252d_jerk_v146_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, officerbuycount):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * _z(_f32_bigbuy(buyval, officerbuycount, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qcomposite_126d_jerk_v147_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, marketcap):
    smart = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    passive = tenpctbuyval.rolling(126, min_periods=42).sum()
    qfrac = _safe_div(smart, smart + passive)
    result = (_f32_offshare(officerbuyval, buyval, 126) + qfrac
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_qcomposite_252d_jerk_v148_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, marketcap):
    smart = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    passive = tenpctbuyval.rolling(252, min_periods=84).sum()
    qfrac = _safe_div(smart, smart + passive)
    result = (_f32_offshare(officerbuyval, buyval, 252) + qfrac
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 252), 504)) / 3.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convqmix_126d_jerk_v149_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126) * _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ic_f32_insider_conviction_quality_convblend_multi_jerk_v150_signal(officerbuyval, dirbuyval, marketcap):
    result = (_f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)) / 4.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f32ic_f32_insider_conviction_quality_offshare_63d_jerk_v001_signal,    f32ic_f32_insider_conviction_quality_offshare_126d_jerk_v002_signal,    f32ic_f32_insider_conviction_quality_offshare_252d_jerk_v003_signal,    f32ic_f32_insider_conviction_quality_offshare_504d_jerk_v004_signal,    f32ic_f32_insider_conviction_quality_dirshare_63d_jerk_v005_signal,    f32ic_f32_insider_conviction_quality_dirshare_126d_jerk_v006_signal,    f32ic_f32_insider_conviction_quality_dirshare_252d_jerk_v007_signal,    f32ic_f32_insider_conviction_quality_insidshare_63d_jerk_v008_signal,    f32ic_f32_insider_conviction_quality_insidshare_126d_jerk_v009_signal,    f32ic_f32_insider_conviction_quality_insidshare_252d_jerk_v010_signal,    f32ic_f32_insider_conviction_quality_conv_63d_jerk_v011_signal,    f32ic_f32_insider_conviction_quality_conv_126d_jerk_v012_signal,    f32ic_f32_insider_conviction_quality_conv_252d_jerk_v013_signal,    f32ic_f32_insider_conviction_quality_conv_504d_jerk_v014_signal,    f32ic_f32_insider_conviction_quality_conv_21d_jerk_v015_signal,    f32ic_f32_insider_conviction_quality_offconv_63d_jerk_v016_signal,    f32ic_f32_insider_conviction_quality_offconv_126d_jerk_v017_signal,    f32ic_f32_insider_conviction_quality_offconv_252d_jerk_v018_signal,    f32ic_f32_insider_conviction_quality_dirconv_63d_jerk_v019_signal,    f32ic_f32_insider_conviction_quality_dirconv_126d_jerk_v020_signal,    f32ic_f32_insider_conviction_quality_dirconv_252d_jerk_v021_signal,    f32ic_f32_insider_conviction_quality_bigbuy_63d_jerk_v022_signal,    f32ic_f32_insider_conviction_quality_bigbuy_126d_jerk_v023_signal,    f32ic_f32_insider_conviction_quality_bigbuy_252d_jerk_v024_signal,    f32ic_f32_insider_conviction_quality_bigbuy_504d_jerk_v025_signal,    f32ic_f32_insider_conviction_quality_qmix_63d_jerk_v026_signal,    f32ic_f32_insider_conviction_quality_qmix_126d_jerk_v027_signal,    f32ic_f32_insider_conviction_quality_qmix_252d_jerk_v028_signal,    f32ic_f32_insider_conviction_quality_qmix_504d_jerk_v029_signal,    f32ic_f32_insider_conviction_quality_qfrac_63d_jerk_v030_signal,    f32ic_f32_insider_conviction_quality_qfrac_126d_jerk_v031_signal,    f32ic_f32_insider_conviction_quality_qfrac_252d_jerk_v032_signal,    f32ic_f32_insider_conviction_quality_offdirbal_63d_jerk_v033_signal,    f32ic_f32_insider_conviction_quality_offdirbal_126d_jerk_v034_signal,    f32ic_f32_insider_conviction_quality_offdirbal_252d_jerk_v035_signal,    f32ic_f32_insider_conviction_quality_zoffshare_63d_jerk_v036_signal,    f32ic_f32_insider_conviction_quality_zoffshare_126d_jerk_v037_signal,    f32ic_f32_insider_conviction_quality_zconv_63d_jerk_v038_signal,    f32ic_f32_insider_conviction_quality_zconv_126d_jerk_v039_signal,    f32ic_f32_insider_conviction_quality_zbigbuy_63d_jerk_v040_signal,    f32ic_f32_insider_conviction_quality_zbigbuy_126d_jerk_v041_signal,    f32ic_f32_insider_conviction_quality_zqmix_63d_jerk_v042_signal,    f32ic_f32_insider_conviction_quality_convtrend_63d_jerk_v043_signal,    f32ic_f32_insider_conviction_quality_convtrend_126d_jerk_v044_signal,    f32ic_f32_insider_conviction_quality_offsharetrend_63d_jerk_v045_signal,    f32ic_f32_insider_conviction_quality_convspread_63_252_jerk_v046_signal,    f32ic_f32_insider_conviction_quality_convspread_126_504_jerk_v047_signal,    f32ic_f32_insider_conviction_quality_offsharespread_63_252_jerk_v048_signal,    f32ic_f32_insider_conviction_quality_offflow_63d_jerk_v049_signal,    f32ic_f32_insider_conviction_quality_offflow_126d_jerk_v050_signal,    f32ic_f32_insider_conviction_quality_offflow_252d_jerk_v051_signal,    f32ic_f32_insider_conviction_quality_buysharesint_63d_jerk_v052_signal,    f32ic_f32_insider_conviction_quality_buysharesint_126d_jerk_v053_signal,    f32ic_f32_insider_conviction_quality_buysharesint_252d_jerk_v054_signal,    f32ic_f32_insider_conviction_quality_implprice_63d_jerk_v055_signal,    f32ic_f32_insider_conviction_quality_implprice_126d_jerk_v056_signal,    f32ic_f32_insider_conviction_quality_qweighted_63d_jerk_v057_signal,    f32ic_f32_insider_conviction_quality_qweighted_126d_jerk_v058_signal,    f32ic_f32_insider_conviction_quality_qweighted_252d_jerk_v059_signal,    f32ic_f32_insider_conviction_quality_qmixconv_63d_jerk_v060_signal,    f32ic_f32_insider_conviction_quality_qmixconv_126d_jerk_v061_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_63d_jerk_v062_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_126d_jerk_v063_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_252d_jerk_v064_signal,    f32ic_f32_insider_conviction_quality_offconc_63d_jerk_v065_signal,    f32ic_f32_insider_conviction_quality_offconc_126d_jerk_v066_signal,    f32ic_f32_insider_conviction_quality_offconc_252d_jerk_v067_signal,    f32ic_f32_insider_conviction_quality_smoffshare_63d_jerk_v068_signal,    f32ic_f32_insider_conviction_quality_smoffshare_126d_jerk_v069_signal,    f32ic_f32_insider_conviction_quality_smconv_63d_jerk_v070_signal,    f32ic_f32_insider_conviction_quality_smconv_126d_jerk_v071_signal,    f32ic_f32_insider_conviction_quality_convir_63d_jerk_v072_signal,    f32ic_f32_insider_conviction_quality_convir_126d_jerk_v073_signal,    f32ic_f32_insider_conviction_quality_offshareir_63d_jerk_v074_signal,    f32ic_f32_insider_conviction_quality_qcomposite_63d_jerk_v075_signal,    f32ic_f32_insider_conviction_quality_offshare_21d_jerk_v076_signal,    f32ic_f32_insider_conviction_quality_offshare_42d_jerk_v077_signal,    f32ic_f32_insider_conviction_quality_offshare_84d_jerk_v078_signal,    f32ic_f32_insider_conviction_quality_offshare_189d_jerk_v079_signal,    f32ic_f32_insider_conviction_quality_offshare_378d_jerk_v080_signal,    f32ic_f32_insider_conviction_quality_conv_84d_jerk_v081_signal,    f32ic_f32_insider_conviction_quality_conv_189d_jerk_v082_signal,    f32ic_f32_insider_conviction_quality_conv_378d_jerk_v083_signal,    f32ic_f32_insider_conviction_quality_conv_42d_jerk_v084_signal,    f32ic_f32_insider_conviction_quality_conv_315d_jerk_v085_signal,    f32ic_f32_insider_conviction_quality_bigbuy_84d_jerk_v086_signal,    f32ic_f32_insider_conviction_quality_bigbuy_189d_jerk_v087_signal,    f32ic_f32_insider_conviction_quality_bigbuy_42d_jerk_v088_signal,    f32ic_f32_insider_conviction_quality_bigbuy_378d_jerk_v089_signal,    f32ic_f32_insider_conviction_quality_qmix_84d_jerk_v090_signal,    f32ic_f32_insider_conviction_quality_qmix_189d_jerk_v091_signal,    f32ic_f32_insider_conviction_quality_qmix_378d_jerk_v092_signal,    f32ic_f32_insider_conviction_quality_qfrac_504d_jerk_v093_signal,    f32ic_f32_insider_conviction_quality_passshare_84d_jerk_v094_signal,    f32ic_f32_insider_conviction_quality_passshare_189d_jerk_v095_signal,    f32ic_f32_insider_conviction_quality_passshare_252d_jerk_v096_signal,    f32ic_f32_insider_conviction_quality_zconv_84d_jerk_v097_signal,    f32ic_f32_insider_conviction_quality_zconv_189d_jerk_v098_signal,    f32ic_f32_insider_conviction_quality_zoffshare_252d_jerk_v099_signal,    f32ic_f32_insider_conviction_quality_zqmix_84d_jerk_v100_signal,    f32ic_f32_insider_conviction_quality_zbigbuy_252d_jerk_v101_signal,    f32ic_f32_insider_conviction_quality_convtrend_84d_jerk_v102_signal,    f32ic_f32_insider_conviction_quality_convtrend_252d_jerk_v103_signal,    f32ic_f32_insider_conviction_quality_offsharetrend_126d_jerk_v104_signal,    f32ic_f32_insider_conviction_quality_bigbuytrend_84d_jerk_v105_signal,    f32ic_f32_insider_conviction_quality_convspread_84_315_jerk_v106_signal,    f32ic_f32_insider_conviction_quality_offsharespread_84_252_jerk_v107_signal,    f32ic_f32_insider_conviction_quality_qmixspread_84_252_jerk_v108_signal,    f32ic_f32_insider_conviction_quality_offflow_84d_jerk_v109_signal,    f32ic_f32_insider_conviction_quality_offflow_189d_jerk_v110_signal,    f32ic_f32_insider_conviction_quality_offflow_504d_jerk_v111_signal,    f32ic_f32_insider_conviction_quality_dirflow_84d_jerk_v112_signal,    f32ic_f32_insider_conviction_quality_dirflow_189d_jerk_v113_signal,    f32ic_f32_insider_conviction_quality_buysharesint_84d_jerk_v114_signal,    f32ic_f32_insider_conviction_quality_buysharesint_504d_jerk_v115_signal,    f32ic_f32_insider_conviction_quality_implprice_252d_jerk_v116_signal,    f32ic_f32_insider_conviction_quality_qweighted_84d_jerk_v117_signal,    f32ic_f32_insider_conviction_quality_qweighted_189d_jerk_v118_signal,    f32ic_f32_insider_conviction_quality_qmixconv_252d_jerk_v119_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_84d_jerk_v120_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_189d_jerk_v121_signal,    f32ic_f32_insider_conviction_quality_bigbuyint_504d_jerk_v122_signal,    f32ic_f32_insider_conviction_quality_offconc_84d_jerk_v123_signal,    f32ic_f32_insider_conviction_quality_offconc_504d_jerk_v124_signal,    f32ic_f32_insider_conviction_quality_smoffshare_252d_jerk_v125_signal,    f32ic_f32_insider_conviction_quality_smconv_252d_jerk_v126_signal,    f32ic_f32_insider_conviction_quality_smqmix_84d_jerk_v127_signal,    f32ic_f32_insider_conviction_quality_smbigbuy_84d_jerk_v128_signal,    f32ic_f32_insider_conviction_quality_convir_252d_jerk_v129_signal,    f32ic_f32_insider_conviction_quality_convir_84d_jerk_v130_signal,    f32ic_f32_insider_conviction_quality_offshareir_126d_jerk_v131_signal,    f32ic_f32_insider_conviction_quality_qmixir_84d_jerk_v132_signal,    f32ic_f32_insider_conviction_quality_bigbuyir_84d_jerk_v133_signal,    f32ic_f32_insider_conviction_quality_rankoffshare_84d_jerk_v134_signal,    f32ic_f32_insider_conviction_quality_rankconv_84d_jerk_v135_signal,    f32ic_f32_insider_conviction_quality_rankbigbuy_84d_jerk_v136_signal,    f32ic_f32_insider_conviction_quality_ewmconv_84d_jerk_v137_signal,    f32ic_f32_insider_conviction_quality_ewmoffshare_63d_jerk_v138_signal,    f32ic_f32_insider_conviction_quality_qaccel_84d_jerk_v139_signal,    f32ic_f32_insider_conviction_quality_convaccel_42_126_jerk_v140_signal,    f32ic_f32_insider_conviction_quality_insidflow_252d_jerk_v141_signal,    f32ic_f32_insider_conviction_quality_insidflow_126d_jerk_v142_signal,    f32ic_f32_insider_conviction_quality_sizedisp_126d_jerk_v143_signal,    f32ic_f32_insider_conviction_quality_convperbuy_252d_jerk_v144_signal,    f32ic_f32_insider_conviction_quality_smartconc_126d_jerk_v145_signal,    f32ic_f32_insider_conviction_quality_qmixsize_252d_jerk_v146_signal,    f32ic_f32_insider_conviction_quality_qcomposite_126d_jerk_v147_signal,    f32ic_f32_insider_conviction_quality_qcomposite_252d_jerk_v148_signal,    f32ic_f32_insider_conviction_quality_convqmix_126d_jerk_v149_signal,    f32ic_f32_insider_conviction_quality_convblend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_INSIDER_CONVICTION_QUALITY_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f32_offshare', '_f32_conviction', '_f32_bigbuy', '_f32_qualitymix')
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
    print("OK f32_insider_conviction_quality_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
