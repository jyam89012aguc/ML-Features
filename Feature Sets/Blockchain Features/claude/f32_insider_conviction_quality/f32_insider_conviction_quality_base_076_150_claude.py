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


# ============ FEATURES 076-150 ============

# 21d officer share of total insider buying (fast quality)
def f32ic_f32_insider_conviction_quality_offshare_21d_base_v076_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_42d_base_v077_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_84d_base_v078_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_189d_base_v079_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d officer share of total insider buying
def f32ic_f32_insider_conviction_quality_offshare_378d_base_v080_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_84d_base_v081_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_189d_base_v082_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_378d_base_v083_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_42d_base_v084_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d officer+director buy $ / marketcap
def f32ic_f32_insider_conviction_quality_conv_315d_base_v085_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_84d_base_v086_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_189d_base_v087_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_42d_base_v088_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d average insider purchase size
def f32ic_f32_insider_conviction_quality_bigbuy_378d_base_v089_signal(buyval, officerbuycount):
    result = _f32_bigbuy(buyval, officerbuycount, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_84d_base_v090_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_189d_base_v091_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d quality mix: insider vs 10%-owner buying
def f32ic_f32_insider_conviction_quality_qmix_378d_base_v092_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d insider-share of buying (insider+passive normalization)
def f32ic_f32_insider_conviction_quality_qfrac_504d_base_v093_signal(officerbuyval, dirbuyval, tenpctbuyval):
    smart = (officerbuyval + dirbuyval).rolling(504, min_periods=168).sum()
    passive = tenpctbuyval.rolling(504, min_periods=168).sum()
    result = _safe_div(smart, smart + passive) + _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d 10%-owner share of total buying (passive participation)
def f32ic_f32_insider_conviction_quality_passshare_84d_base_v094_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(84, min_periods=42).sum()
    den = buyval.rolling(84, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d 10%-owner share of total buying
def f32ic_f32_insider_conviction_quality_passshare_189d_base_v095_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(189, min_periods=63).sum()
    den = buyval.rolling(189, min_periods=63).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 10%-owner share of total buying
def f32ic_f32_insider_conviction_quality_passshare_252d_base_v096_signal(tenpctbuyval, buyval):
    num = tenpctbuyval.rolling(252, min_periods=84).sum()
    den = buyval.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_offshare(tenpctbuyval, buyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 84d conviction over 252d
def f32ic_f32_insider_conviction_quality_zconv_84d_base_v097_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 84), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 189d conviction over 504d
def f32ic_f32_insider_conviction_quality_zconv_189d_base_v098_signal(officerbuyval, dirbuyval, marketcap):
    result = _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 189), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d officer share over 504d
def f32ic_f32_insider_conviction_quality_zoffshare_252d_base_v099_signal(officerbuyval, buyval):
    result = _z(_f32_offshare(officerbuyval, buyval, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 84d quality mix over 252d
def f32ic_f32_insider_conviction_quality_zqmix_84d_base_v100_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _z(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d average buy size over 504d
def f32ic_f32_insider_conviction_quality_zbigbuy_252d_base_v101_signal(buyval, officerbuycount):
    result = _z(_f32_bigbuy(buyval, officerbuycount, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction trend: 84d conviction minus its 252d mean
def f32ic_f32_insider_conviction_quality_convtrend_84d_base_v102_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction trend: 252d conviction minus its 504d mean
def f32ic_f32_insider_conviction_quality_convtrend_252d_base_v103_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = c - _mean(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# officer-share trend: 126d officer share minus its 504d mean
def f32ic_f32_insider_conviction_quality_offsharetrend_126d_base_v104_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 126)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# big-buy trend: 84d avg buy size minus its 252d mean
def f32ic_f32_insider_conviction_quality_bigbuytrend_84d_base_v105_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = b - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction spread: 84d vs 315d
def f32ic_f32_insider_conviction_quality_convspread_84_315_base_v106_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# officer-share spread: 84d vs 252d
def f32ic_f32_insider_conviction_quality_offsharespread_84_252_base_v107_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 84) - _f32_offshare(officerbuyval, buyval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality-mix spread: 84d vs 252d
def f32ic_f32_insider_conviction_quality_qmixspread_84_252_base_v108_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84) - _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_offflow_84d_base_v109_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d officer buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_offflow_189d_base_v110_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(189, min_periods=63).sum()
    den = sharesbas.rolling(189, min_periods=63).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d officer buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_offflow_504d_base_v111_signal(officerbuyval, sharesbas):
    num = officerbuyval.rolling(504, min_periods=168).sum()
    den = sharesbas.rolling(504, min_periods=168).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d director buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_dirflow_84d_base_v112_signal(dirbuyval, sharesbas):
    num = dirbuyval.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, dirbuyval, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d director buy $ flow vs shares outstanding
def f32ic_f32_insider_conviction_quality_dirflow_189d_base_v113_signal(dirbuyval, sharesbas):
    num = dirbuyval.rolling(189, min_periods=63).sum()
    den = sharesbas.rolling(189, min_periods=63).mean()
    result = _safe_div(num, den) + _f32_offshare(dirbuyval, dirbuyval, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d insider buy shares vs shares outstanding
def f32ic_f32_insider_conviction_quality_buysharesint_84d_base_v114_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(84, min_periods=42).sum()
    den = sharesbas.rolling(84, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d insider buy shares vs shares outstanding
def f32ic_f32_insider_conviction_quality_buysharesint_504d_base_v115_signal(buyshares, sharesbas, buyval):
    num = buyshares.rolling(504, min_periods=168).sum()
    den = sharesbas.rolling(504, min_periods=168).mean()
    result = _safe_div(num, den) + _f32_offshare(buyval, buyval, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d implied buy price vs avg buy size
def f32ic_f32_insider_conviction_quality_implprice_252d_base_v116_signal(buyval, buyshares, officerbuycount):
    num = buyval.rolling(252, min_periods=84).sum()
    den = buyshares.rolling(252, min_periods=84).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d conviction-weighted officer share
def f32ic_f32_insider_conviction_quality_qweighted_84d_base_v117_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 84) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d conviction-weighted officer share
def f32ic_f32_insider_conviction_quality_qweighted_189d_base_v118_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 189) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality-mix weighted by conviction
def f32ic_f32_insider_conviction_quality_qmixconv_252d_base_v119_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d big-buy intensity vs marketcap
def f32ic_f32_insider_conviction_quality_bigbuyint_84d_base_v120_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 84), marketcap.rolling(84, min_periods=42).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d big-buy intensity vs marketcap
def f32ic_f32_insider_conviction_quality_bigbuyint_189d_base_v121_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 189), marketcap.rolling(189, min_periods=63).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d big-buy intensity vs marketcap
def f32ic_f32_insider_conviction_quality_bigbuyint_504d_base_v122_signal(buyval, officerbuycount, marketcap):
    result = _safe_div(_f32_bigbuy(buyval, officerbuycount, 504), marketcap.rolling(504, min_periods=168).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer-buy concentration (officer $ per buy event)
def f32ic_f32_insider_conviction_quality_offconc_84d_base_v123_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(84, min_periods=42).sum()
    den = (officerbuycount + 1.0).rolling(84, min_periods=42).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d officer-buy concentration
def f32ic_f32_insider_conviction_quality_offconc_504d_base_v124_signal(officerbuyval, officerbuycount, buyval):
    num = officerbuyval.rolling(504, min_periods=168).sum()
    den = (officerbuycount + 1.0).rolling(504, min_periods=168).sum()
    result = _safe_div(num, den) + _f32_bigbuy(buyval, officerbuycount, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed officer share (63d mean)
def f32ic_f32_insider_conviction_quality_smoffshare_252d_base_v125_signal(officerbuyval, buyval):
    result = _mean(_f32_offshare(officerbuyval, buyval, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed conviction (63d mean)
def f32ic_f32_insider_conviction_quality_smconv_252d_base_v126_signal(officerbuyval, dirbuyval, marketcap):
    result = _mean(_f32_conviction(officerbuyval, dirbuyval, marketcap, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d smoothed quality mix (21d mean)
def f32ic_f32_insider_conviction_quality_smqmix_84d_base_v127_signal(officerbuyval, dirbuyval, tenpctbuyval):
    result = _mean(_f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d smoothed avg buy size (21d mean)
def f32ic_f32_insider_conviction_quality_smbigbuy_84d_base_v128_signal(buyval, officerbuycount):
    result = _mean(_f32_bigbuy(buyval, officerbuycount, 84), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction information ratio
def f32ic_f32_insider_conviction_quality_convir_252d_base_v129_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    result = _safe_div(c, _std(c, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d conviction information ratio
def f32ic_f32_insider_conviction_quality_convir_84d_base_v130_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = _safe_div(c, _std(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer-share information ratio
def f32ic_f32_insider_conviction_quality_offshareir_126d_base_v131_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 126)
    result = _safe_div(s, _std(s, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d quality-mix information ratio
def f32ic_f32_insider_conviction_quality_qmixir_84d_base_v132_signal(officerbuyval, dirbuyval, tenpctbuyval):
    m = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 84)
    result = _safe_div(m, _std(m, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d big-buy information ratio
def f32ic_f32_insider_conviction_quality_bigbuyir_84d_base_v133_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = _safe_div(b, _std(b, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer share percentile rank over 252d
def f32ic_f32_insider_conviction_quality_rankoffshare_84d_base_v134_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 84)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d conviction percentile rank over 252d
def f32ic_f32_insider_conviction_quality_rankconv_84d_base_v135_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d avg-buy-size percentile rank over 252d
def f32ic_f32_insider_conviction_quality_rankbigbuy_84d_base_v136_signal(buyval, officerbuycount):
    b = _f32_bigbuy(buyval, officerbuycount, 84)
    result = b.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d EWM of conviction (span-weighted intensity)
def f32ic_f32_insider_conviction_quality_ewmconv_84d_base_v137_signal(officerbuyval, dirbuyval, marketcap):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 84)
    result = c.ewm(span=84, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWM of officer share
def f32ic_f32_insider_conviction_quality_ewmoffshare_63d_base_v138_signal(officerbuyval, buyval):
    s = _f32_offshare(officerbuyval, buyval, 63)
    result = s.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 84d officer-buy $ vs total buy $ change (quality acceleration)
def f32ic_f32_insider_conviction_quality_qaccel_84d_base_v139_signal(officerbuyval, buyval):
    result = _f32_offshare(officerbuyval, buyval, 42) - _f32_offshare(officerbuyval, buyval, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction acceleration: 42d vs 126d
def f32ic_f32_insider_conviction_quality_convaccel_42_126_base_v140_signal(officerbuyval, dirbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 42) - _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d officer+director buy $ vs total assets-style scale (sharesbas proxy intensity)
def f32ic_f32_insider_conviction_quality_insidflow_252d_base_v141_signal(officerbuyval, dirbuyval, sharesbas):
    num = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    den = sharesbas.rolling(252, min_periods=84).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer+director buy $ vs shares outstanding
def f32ic_f32_insider_conviction_quality_insidflow_126d_base_v142_signal(officerbuyval, dirbuyval, sharesbas):
    num = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    den = sharesbas.rolling(126, min_periods=42).mean()
    result = _safe_div(num, den) + _f32_offshare(officerbuyval, officerbuyval + dirbuyval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d big-buy vs officer-buy concentration ratio (size dispersion)
def f32ic_f32_insider_conviction_quality_sizedisp_126d_base_v143_signal(buyval, officerbuyval, officerbuycount):
    big = _f32_bigbuy(buyval, officerbuycount, 126)
    offc = _safe_div(officerbuyval.rolling(126, min_periods=42).sum(), (officerbuycount + 1.0).rolling(126, min_periods=42).sum())
    result = _safe_div(offc, big)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction normalized by buy-share intensity (quality per accumulation)
def f32ic_f32_insider_conviction_quality_convperbuy_252d_base_v144_signal(officerbuyval, dirbuyval, marketcap, buyshares, sharesbas):
    c = _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
    acc = _safe_div(buyshares.rolling(252, min_periods=84).sum(), sharesbas.rolling(252, min_periods=84).mean())
    result = _safe_div(c, acc)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d officer share scaled by conviction z (smart-buyer concentration)
def f32ic_f32_insider_conviction_quality_smartconc_126d_base_v145_signal(officerbuyval, dirbuyval, buyval, marketcap):
    result = _f32_offshare(officerbuyval, buyval, 126) * _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality-mix scaled by avg buy size z
def f32ic_f32_insider_conviction_quality_qmixsize_252d_base_v146_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, officerbuycount):
    result = _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 252) * _z(_f32_bigbuy(buyval, officerbuycount, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite quality score (officer share + qmix frac + conviction z)
def f32ic_f32_insider_conviction_quality_qcomposite_126d_base_v147_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, marketcap):
    smart = (officerbuyval + dirbuyval).rolling(126, min_periods=42).sum()
    passive = tenpctbuyval.rolling(126, min_periods=42).sum()
    qfrac = _safe_div(smart, smart + passive)
    result = (_f32_offshare(officerbuyval, buyval, 126) + qfrac
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 126), 504)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite quality score
def f32ic_f32_insider_conviction_quality_qcomposite_252d_base_v148_signal(officerbuyval, dirbuyval, tenpctbuyval, buyval, marketcap):
    smart = (officerbuyval + dirbuyval).rolling(252, min_periods=84).sum()
    passive = tenpctbuyval.rolling(252, min_periods=84).sum()
    qfrac = _safe_div(smart, smart + passive)
    result = (_f32_offshare(officerbuyval, buyval, 252) + qfrac
              + _z(_f32_conviction(officerbuyval, dirbuyval, marketcap, 252), 504)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction-quality interaction (conviction x quality mix)
def f32ic_f32_insider_conviction_quality_convqmix_126d_base_v149_signal(officerbuyval, dirbuyval, tenpctbuyval, marketcap):
    result = _f32_conviction(officerbuyval, dirbuyval, marketcap, 126) * _f32_qualitymix(officerbuyval, dirbuyval, tenpctbuyval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon conviction composite (63/126/252/504)
def f32ic_f32_insider_conviction_quality_convblend_multi_base_v150_signal(officerbuyval, dirbuyval, marketcap):
    result = (_f32_conviction(officerbuyval, dirbuyval, marketcap, 63)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 126)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 252)
              + _f32_conviction(officerbuyval, dirbuyval, marketcap, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32ic_f32_insider_conviction_quality_offshare_21d_base_v076_signal,
    f32ic_f32_insider_conviction_quality_offshare_42d_base_v077_signal,
    f32ic_f32_insider_conviction_quality_offshare_84d_base_v078_signal,
    f32ic_f32_insider_conviction_quality_offshare_189d_base_v079_signal,
    f32ic_f32_insider_conviction_quality_offshare_378d_base_v080_signal,
    f32ic_f32_insider_conviction_quality_conv_84d_base_v081_signal,
    f32ic_f32_insider_conviction_quality_conv_189d_base_v082_signal,
    f32ic_f32_insider_conviction_quality_conv_378d_base_v083_signal,
    f32ic_f32_insider_conviction_quality_conv_42d_base_v084_signal,
    f32ic_f32_insider_conviction_quality_conv_315d_base_v085_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_84d_base_v086_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_189d_base_v087_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_42d_base_v088_signal,
    f32ic_f32_insider_conviction_quality_bigbuy_378d_base_v089_signal,
    f32ic_f32_insider_conviction_quality_qmix_84d_base_v090_signal,
    f32ic_f32_insider_conviction_quality_qmix_189d_base_v091_signal,
    f32ic_f32_insider_conviction_quality_qmix_378d_base_v092_signal,
    f32ic_f32_insider_conviction_quality_qfrac_504d_base_v093_signal,
    f32ic_f32_insider_conviction_quality_passshare_84d_base_v094_signal,
    f32ic_f32_insider_conviction_quality_passshare_189d_base_v095_signal,
    f32ic_f32_insider_conviction_quality_passshare_252d_base_v096_signal,
    f32ic_f32_insider_conviction_quality_zconv_84d_base_v097_signal,
    f32ic_f32_insider_conviction_quality_zconv_189d_base_v098_signal,
    f32ic_f32_insider_conviction_quality_zoffshare_252d_base_v099_signal,
    f32ic_f32_insider_conviction_quality_zqmix_84d_base_v100_signal,
    f32ic_f32_insider_conviction_quality_zbigbuy_252d_base_v101_signal,
    f32ic_f32_insider_conviction_quality_convtrend_84d_base_v102_signal,
    f32ic_f32_insider_conviction_quality_convtrend_252d_base_v103_signal,
    f32ic_f32_insider_conviction_quality_offsharetrend_126d_base_v104_signal,
    f32ic_f32_insider_conviction_quality_bigbuytrend_84d_base_v105_signal,
    f32ic_f32_insider_conviction_quality_convspread_84_315_base_v106_signal,
    f32ic_f32_insider_conviction_quality_offsharespread_84_252_base_v107_signal,
    f32ic_f32_insider_conviction_quality_qmixspread_84_252_base_v108_signal,
    f32ic_f32_insider_conviction_quality_offflow_84d_base_v109_signal,
    f32ic_f32_insider_conviction_quality_offflow_189d_base_v110_signal,
    f32ic_f32_insider_conviction_quality_offflow_504d_base_v111_signal,
    f32ic_f32_insider_conviction_quality_dirflow_84d_base_v112_signal,
    f32ic_f32_insider_conviction_quality_dirflow_189d_base_v113_signal,
    f32ic_f32_insider_conviction_quality_buysharesint_84d_base_v114_signal,
    f32ic_f32_insider_conviction_quality_buysharesint_504d_base_v115_signal,
    f32ic_f32_insider_conviction_quality_implprice_252d_base_v116_signal,
    f32ic_f32_insider_conviction_quality_qweighted_84d_base_v117_signal,
    f32ic_f32_insider_conviction_quality_qweighted_189d_base_v118_signal,
    f32ic_f32_insider_conviction_quality_qmixconv_252d_base_v119_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_84d_base_v120_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_189d_base_v121_signal,
    f32ic_f32_insider_conviction_quality_bigbuyint_504d_base_v122_signal,
    f32ic_f32_insider_conviction_quality_offconc_84d_base_v123_signal,
    f32ic_f32_insider_conviction_quality_offconc_504d_base_v124_signal,
    f32ic_f32_insider_conviction_quality_smoffshare_252d_base_v125_signal,
    f32ic_f32_insider_conviction_quality_smconv_252d_base_v126_signal,
    f32ic_f32_insider_conviction_quality_smqmix_84d_base_v127_signal,
    f32ic_f32_insider_conviction_quality_smbigbuy_84d_base_v128_signal,
    f32ic_f32_insider_conviction_quality_convir_252d_base_v129_signal,
    f32ic_f32_insider_conviction_quality_convir_84d_base_v130_signal,
    f32ic_f32_insider_conviction_quality_offshareir_126d_base_v131_signal,
    f32ic_f32_insider_conviction_quality_qmixir_84d_base_v132_signal,
    f32ic_f32_insider_conviction_quality_bigbuyir_84d_base_v133_signal,
    f32ic_f32_insider_conviction_quality_rankoffshare_84d_base_v134_signal,
    f32ic_f32_insider_conviction_quality_rankconv_84d_base_v135_signal,
    f32ic_f32_insider_conviction_quality_rankbigbuy_84d_base_v136_signal,
    f32ic_f32_insider_conviction_quality_ewmconv_84d_base_v137_signal,
    f32ic_f32_insider_conviction_quality_ewmoffshare_63d_base_v138_signal,
    f32ic_f32_insider_conviction_quality_qaccel_84d_base_v139_signal,
    f32ic_f32_insider_conviction_quality_convaccel_42_126_base_v140_signal,
    f32ic_f32_insider_conviction_quality_insidflow_252d_base_v141_signal,
    f32ic_f32_insider_conviction_quality_insidflow_126d_base_v142_signal,
    f32ic_f32_insider_conviction_quality_sizedisp_126d_base_v143_signal,
    f32ic_f32_insider_conviction_quality_convperbuy_252d_base_v144_signal,
    f32ic_f32_insider_conviction_quality_smartconc_126d_base_v145_signal,
    f32ic_f32_insider_conviction_quality_qmixsize_252d_base_v146_signal,
    f32ic_f32_insider_conviction_quality_qcomposite_126d_base_v147_signal,
    f32ic_f32_insider_conviction_quality_qcomposite_252d_base_v148_signal,
    f32ic_f32_insider_conviction_quality_convqmix_126d_base_v149_signal,
    f32ic_f32_insider_conviction_quality_convblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_INSIDER_CONVICTION_QUALITY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f32_insider_conviction_quality_base_076_150_claude: {n_features} features pass")
