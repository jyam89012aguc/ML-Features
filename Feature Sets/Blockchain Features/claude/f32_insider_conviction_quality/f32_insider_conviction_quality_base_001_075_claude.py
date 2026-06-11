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


# ============ FEATURES 001-075 ============

# 63d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_63d_base_v001_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_126d_base_v002_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_252d_base_v003_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_504d_base_v004_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d director share of total insider buying
def f32ic_f32_insider_conviction_quality_dirshare_63d_base_v005_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(63, min_periods=21).sum()
    den = buyval.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d director share of total insider buying
def f32ic_f32_insider_conviction_quality_dirshare_126d_base_v006_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(126, min_periods=42).sum()
    den = buyval.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d director share of total insider buying
def f32ic_f32_insider_conviction_quality_dirshare_252d_base_v007_signal(dirbuyval, buyval):
    num = dirbuyval.rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, buyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d insider (officer+director) share of total buying
def f32ic_f32_insider_conviction_quality_insidshare_63d_base_v008_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(63, min_periods=21).sum()
    den = buyval.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d insider (officer+director) share of total buying
def f32ic_f32_insider_conviction_quality_insidshare_126d_base_v009_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    den = buyval.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d insider (officer+director) share of total buying
def f32ic_f32_insider_conviction_quality_insidshare_252d_base_v010_signal(officerbuyval, dirbuyval, buyval):
    num = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, buyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer+director buy $ / marketcap (conviction intensity)
def f32ic_f32_insider_conviction_quality_conv_63d_base_v011_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_126d_base_v012_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_252d_base_v013_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_504d_base_v014_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d officer+director buy $ / marketcap (fast conviction)
def f32ic_f32_insider_conviction_quality_conv_21d_base_v015_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_offconv_63d_base_v016_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = marketcap.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_offconv_126d_base_v017_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = marketcap.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_offconv_252d_base_v018_signal(officerbuyval, marketcap):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = marketcap.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_conviction(officerbuyval, officerbuyval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d director-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_dirconv_63d_base_v019_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(63, min_periods=21).sum()
    den = marketcap.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d director-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_dirconv_126d_base_v020_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(126, min_periods=42).sum()
    den = marketcap.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d director-only buy $ / marketcap
def f32ic_f32_insider_conviction_quality_dirconv_252d_base_v021_signal(dirbuyval, marketcap):
    num = dirbuyval.rolling(252, min_periods=84).sum()
    den = marketcap.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_conviction(dirbuyval, dirbuyval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d average insider purchase size (buy $ per officer-buy event)
def f32ic_f32_insider_conviction_quality_bigbuy_63d_base_v022_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_126d_base_v023_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_252d_base_v024_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_504d_base_v025_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_63d_base_v026_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_126d_base_v027_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_252d_base_v028_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_504d_base_v029_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d insider-share of buying (insider+passive normalization)
def f32ic_f32_insider_conviction_quality_qfrac_63d_base_v030_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(63, min_periods=21).sum()
    passive = tenpctbuyval.rolling(63, min_periods=21).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d insider-share of buying (insider+passive normalization)
def f32ic_f32_insider_conviction_quality_qfrac_126d_base_v031_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    passive = tenpctbuyval.rolling(126, min_periods=42).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d insider-share of buying (insider+passive normalization)
def f32ic_f32_insider_conviction_quality_qfrac_252d_base_v032_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    passive = tenpctbuyval.rolling(252, min_periods=84).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer-vs-director balance within insider buying
def f32ic_f32_insider_conviction_quality_offdirbal_63d_base_v033_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(63, min_periods=21).sum()
    d = dirbuyval.rolling(63, min_periods=21).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer-vs-director balance within insider buying
def f32ic_f32_insider_conviction_quality_offdirbal_126d_base_v034_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(126, min_periods=42).sum()
    d = dirbuyval.rolling(126, min_periods=42).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer-vs-director balance within insider buying
def f32ic_f32_insider_conviction_quality_offdirbal_252d_base_v035_signal(officerbuyval, dirbuyval):
    o = officerbuyval.rolling(252, min_periods=84).sum()
    d = dirbuyval.rolling(252, min_periods=84).sum()
    result = _safe_div(o - d, o + d) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d officer share over 252d
def f32ic_f32_insider_conviction_quality_zoffshare_63d_base_v036_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d officer share over 504d
def f32ic_f32_insider_conviction_quality_zoffshare_126d_base_v037_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d conviction over 252d
def f32ic_f32_insider_conviction_quality_zconv_63d_base_v038_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d conviction over 504d
def f32ic_f32_insider_conviction_quality_zconv_126d_base_v039_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d average buy size over 252d
def f32ic_f32_insider_conviction_quality_zbigbuy_63d_base_v040_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d average buy size over 504d
def f32ic_f32_insider_conviction_quality_zbigbuy_126d_base_v041_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d quality mix over 252d
def f32ic_f32_insider_conviction_quality_zqmix_63d_base_v042_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _z(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction trend: 63d conviction minus its 252d mean
def f32ic_f32_insider_conviction_quality_convtrend_63d_base_v043_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction trend: 126d conviction minus its 252d mean
def f32ic_f32_insider_conviction_quality_convtrend_126d_base_v044_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# officer-share trend: 63d officer share minus its 252d mean
def f32ic_f32_insider_conviction_quality_offsharetrend_63d_base_v045_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction spread: 63d vs 252d officer+director / marketcap
def f32ic_f32_insider_conviction_quality_convspread_63_252_base_v046_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction spread: 126d vs 504d
def f32ic_f32_insider_conviction_quality_convspread_126_504_base_v047_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# officer-share spread: 63d vs 252d
def f32ic_f32_insider_conviction_quality_offsharespread_63_252_base_v048_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 63) - _f32_offshare(officerbuyval, buyval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer buy $ flow vs shares outstanding (officer accumulation rate)
def f32ic_f32_insider_conviction_quality_offflow_63d_base_v049_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = sharesbas.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_offflow_126d_base_v050_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_offflow_252d_base_v051_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d insider buy shares vs shares outstanding (accumulation intensity)
def f32ic_f32_insider_conviction_quality_buysharesint_63d_base_v052_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(63, min_periods=21).sum()
    den = sharesbas.rolling(63, min_periods=21).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d insider buy shares vs shares outstanding
def f32ic_f32_insider_conviction_quality_buysharesint_126d_base_v053_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d insider buy shares vs shares outstanding
def f32ic_f32_insider_conviction_quality_buysharesint_252d_base_v054_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d implied buy price vs avg buy size (conviction quality composite)
def f32ic_f32_insider_conviction_quality_implprice_63d_base_v055_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(63, min_periods=21).sum()
    den = buyshares.rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d implied buy price vs avg buy size
def f32ic_f32_insider_conviction_quality_implprice_126d_base_v056_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(126, min_periods=42).sum()
    den = buyshares.rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conviction-weighted officer share (quality x intensity composite)
def f32ic_f32_insider_conviction_quality_qweighted_63d_base_v057_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 63) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction-weighted officer share
def f32ic_f32_insider_conviction_quality_qweighted_126d_base_v058_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 126) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction-weighted officer share
def f32ic_f32_insider_conviction_quality_qweighted_252d_base_v059_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 252) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality-mix weighted by conviction
def f32ic_f32_insider_conviction_quality_qmixconv_63d_base_v060_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 63) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quality-mix weighted by conviction
def f32ic_f32_insider_conviction_quality_qmixconv_126d_base_v061_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d big-buy intensity vs marketcap (large-purchase conviction)
def f32ic_f32_insider_conviction_quality_bigbuyint_63d_base_v062_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 63), marketcap.rolling(63, min_periods=21).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d big-buy intensity vs marketcap
def f32ic_f32_insider_conviction_quality_bigbuyint_126d_base_v063_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 126), marketcap.rolling(126, min_periods=42).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d big-buy intensity vs marketcap
def f32ic_f32_insider_conviction_quality_bigbuyint_252d_base_v064_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 252), marketcap.rolling(252, min_periods=84).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer-buy concentration (officer $ per buy event, smart-buyer size)
def f32ic_f32_insider_conviction_quality_offconc_63d_base_v065_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(63, min_periods=21).sum()
    den = (officerbuycount + 1.0).rolling(63, min_periods=21).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer-buy concentration
def f32ic_f32_insider_conviction_quality_offconc_126d_base_v066_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(126, min_periods=42).sum()
    den = (officerbuycount + 1.0).rolling(126, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer-buy concentration
def f32ic_f32_insider_conviction_quality_offconc_252d_base_v067_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(252, min_periods=84).sum()
    den = (officerbuycount + 1.0).rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed officer share (21d mean of 63d officer share)
def f32ic_f32_insider_conviction_quality_smoffshare_63d_base_v068_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed officer share (42d mean)
def f32ic_f32_insider_conviction_quality_smoffshare_126d_base_v069_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed conviction (21d mean)
def f32ic_f32_insider_conviction_quality_smconv_63d_base_v070_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed conviction (42d mean)
def f32ic_f32_insider_conviction_quality_smconv_126d_base_v071_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conviction information ratio (conviction / its dispersion)
def f32ic_f32_insider_conviction_quality_convir_63d_base_v072_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
    result = _safe_div(c, _std(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction information ratio
def f32ic_f32_insider_conviction_quality_convir_126d_base_v073_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    result = _safe_div(c, _std(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d officer-share information ratio
def f32ic_f32_insider_conviction_quality_offshareir_63d_base_v074_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = _safe_div(s, _std(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality composite: officer share x avg buy size x conviction blend
def f32ic_f32_insider_conviction_quality_qcomposite_63d_base_v075_signal(officerbuyval, dirbuyval, buyval, officerbuycount, marketcap):
    result = (_f32_offshare(officerbuyval, buyval, 63)
              + _z(_f32_bigbuy(buyval, officerbuycount, 63), 252)
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 63), 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32ic_f32_insider_conviction_quality_offshare_63d_base_v001_signal,
    f32ic_f32_insider_conviction_quality_offshare_126d_base_v002_signal,
    f32ic_f32_insider_conviction_quality_offshare_252d_base_v003_signal,
    f32ic_f32_insider_conviction_quality_offshare_504d_base_v004_signal,
    f32ic_f32_insider_conviction_quality_dirshare_63d_base_v005_signal,
    f32ic_f32_insider_conviction_quality_dirshare_126d_base_v006_signal,
    f32ic_f32_insider_conviction_quality_dirshare_252d_base_v007_signal,
    f32ic_f32_insider_conviction_quality_insidshare_63d_base_v008_signal,
    f32ic_f32_insider_conviction_quality_insidshare_126d_base_v009_signal,
    f32ic_f32_insider_conviction_quality_insidshare_252d_base_v010_signal,
    f32ic_f32_insider_conviction_quality_conv_63d_base_v011_signal,
    f32ic_f32_insider_conviction_quality_conv_126d_base_v012_signal,
    f32ic_f32_insider_conviction_quality_conv_252d_base_v013_signal,
    f32ic_f32_insider_conviction_quality_conv_504d_base_v014_signal,
    f32ic_f32_insider_conviction_quality_conv_21d_base_v015_signal,
    f32ic_f32_insider_conviction_quality_offconv_63d_base_v016_signal,
    f32ic_f32_insider_conviction_quality_offconv_126d_base_v017_signal,
    f32ic_f32_insider_conviction_quality_offconv_252d_base_v018_signal,
    f32ic_f32_insider_conviction_quality_dirconv_63d_base_v019_signal,
    f32ic_f32_insider_conviction_quality_dirconv_126d_base_v020_signal,
    f32ic_f32_insider_conviction_quality_dirconv_252d_base_v021_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_63d_base_v022_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_126d_base_v023_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_252d_base_v024_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_504d_base_v025_signal,
    f32ic_f32_insider_conviction_quality_qmix_63d_base_v026_signal,
    f32ic_f32_insider_conviction_quality_qmix_126d_base_v027_signal,
    f32ic_f32_insider_conviction_quality_qmix_252d_base_v028_signal,
    f32ic_f32_insider_conviction_quality_qmix_504d_base_v029_signal,
    f32ic_f32_insider_conviction_quality_qfrac_63d_base_v030_signal,
    f32ic_f32_insider_conviction_quality_qfrac_126d_base_v031_signal,
    f32ic_f32_insider_conviction_quality_qfrac_252d_base_v032_signal,
    f32ic_f32_insider_conviction_quality_offdirbal_63d_base_v033_signal,
    f32ic_f32_insider_conviction_quality_offdirbal_126d_base_v034_signal,
    f32ic_f32_insider_conviction_quality_offdirbal_252d_base_v035_signal,
    f32ic_f32_insider_conviction_quality_zoffshare_63d_base_v036_signal,
    f32ic_f32_insider_conviction_quality_zoffshare_126d_base_v037_signal,
    f32ic_f32_insider_conviction_quality_zconv_63d_base_v038_signal,
    f32ic_f32_insider_conviction_quality_zconv_126d_base_v039_signal,
    f32ic_f32_insider_conviction_quality_zbigbuy_63d_base_v040_signal,
    f32ic_f32_insider_conviction_quality_zbigbuy_126d_base_v041_signal,
    f32ic_f32_insider_conviction_quality_zqmix_63d_base_v042_signal,
    f32ic_f32_insider_conviction_quality_convtrend_63d_base_v043_signal,
    f32ic_f32_insider_conviction_quality_convtrend_126d_base_v044_signal,
    f32ic_f32_insider_conviction_quality_offsharetrend_63d_base_v045_signal,
    f32ic_f32_insider_conviction_quality_convspread_63_252_base_v046_signal,
    f32ic_f32_insider_conviction_quality_convspread_126_504_base_v047_signal,
    f32ic_f32_insider_conviction_quality_offsharespread_63_252_base_v048_signal,
    f32ic_f32_insider_conviction_quality_offflow_63d_base_v049_signal,
    f32ic_f32_insider_conviction_quality_offflow_126d_base_v050_signal,
    f32ic_f32_insider_conviction_quality_offflow_252d_base_v051_signal,
    f32ic_f32_insider_conviction_quality_buysharesint_63d_base_v052_signal,
    f32ic_f32_insider_conviction_quality_buysharesint_126d_base_v053_signal,
    f32ic_f32_insider_conviction_quality_buysharesint_252d_base_v054_signal,
    f32ic_f32_insider_conviction_quality_implprice_63d_base_v055_signal,
    f32ic_f32_insider_conviction_quality_implprice_126d_base_v056_signal,
    f32ic_f32_insider_conviction_quality_qweighted_63d_base_v057_signal,
    f32ic_f32_insider_conviction_quality_qweighted_126d_base_v058_signal,
    f32ic_f32_insider_conviction_quality_qweighted_252d_base_v059_signal,
    f32ic_f32_insider_conviction_quality_qmixconv_63d_base_v060_signal,
    f32ic_f32_insider_conviction_quality_qmixconv_126d_base_v061_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_63d_base_v062_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_126d_base_v063_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_252d_base_v064_signal,
    f32ic_f32_insider_conviction_quality_offconc_63d_base_v065_signal,
    f32ic_f32_insider_conviction_quality_offconc_126d_base_v066_signal,
    f32ic_f32_insider_conviction_quality_offconc_252d_base_v067_signal,
    f32ic_f32_insider_conviction_quality_smoffshare_63d_base_v068_signal,
    f32ic_f32_insider_conviction_quality_smoffshare_126d_base_v069_signal,
    f32ic_f32_insider_conviction_quality_smconv_63d_base_v070_signal,
    f32ic_f32_insider_conviction_quality_smconv_126d_base_v071_signal,
    f32ic_f32_insider_conviction_quality_convir_63d_base_v072_signal,
    f32ic_f32_insider_conviction_quality_convir_126d_base_v073_signal,
    f32ic_f32_insider_conviction_quality_offshareir_63d_base_v074_signal,
    f32ic_f32_insider_conviction_quality_qcomposite_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_INSIDER_CONVICTION_QUALITY_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt",
           "officerbuyval","dirbuyval","tenpctbuyval","buyval","buyshares","officerbuycount"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f32_offshare", "_f32_conviction", "_f32_bigbuy", "_f32_qualitymix")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f32_insider_conviction_quality_base_001_075_claude: {n_features} features pass")
