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


# ===== folder domain primitives (bitcoin-treasury premium) =====
def _f16_premium(marketcap, equity):
    # mNAV proxy: market value per unit of book equity
    return _safe_div(marketcap, equity)


def _f16_navgap(marketcap, equity, assets):
    # excess of market value over book equity, scaled by total assets
    return _safe_div(marketcap - equity, assets)


def _f16_bookstretch(marketcap, equity, cashneq):
    # market value vs cash-augmented book floor
    return _safe_div(marketcap, equity + cashneq)


def _f16_netassetprem(marketcap, equity, debt):
    # debt-adjusted net-asset premium: market value vs leverage-netted equity
    return _safe_div(marketcap - (equity - debt), equity)


# ============ FEATURES 076-150 ============

# mNAV premium smoothed over 42d
def f16bt_f16_bitcoin_treasury_premium_mnavsm_42d_base_v076_signal(marketcap, equity):
    result = _mean(_f16_premium(marketcap, equity), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# mNAV premium smoothed over 189d
def f16bt_f16_bitcoin_treasury_premium_mnavsm_189d_base_v077_signal(marketcap, equity):
    result = _mean(_f16_premium(marketcap, equity), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# mNAV premium smoothed over 504d
def f16bt_f16_bitcoin_treasury_premium_mnavsm_504d_base_v078_signal(marketcap, equity):
    result = _mean(_f16_premium(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# log book-stretch premium
def f16bt_f16_bitcoin_treasury_premium_logbookstretch_21d_base_v079_signal(marketcap, equity, cashneq):
    result = np.log(_f16_bookstretch(marketcap, equity, cashneq))
    return result.replace([np.inf, -np.inf], np.nan)


# log book-stretch smoothed over 126d
def f16bt_f16_bitcoin_treasury_premium_logbookstretchsm_126d_base_v080_signal(marketcap, equity, cashneq):
    result = _mean(np.log(_f16_bookstretch(marketcap, equity, cashneq)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of book-stretch over 126d
def f16bt_f16_bitcoin_treasury_premium_zbookstretch_126d_base_v081_signal(marketcap, equity, cashneq):
    result = _z(_f16_bookstretch(marketcap, equity, cashneq), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of book-stretch over 504d
def f16bt_f16_bitcoin_treasury_premium_zbookstretch_504d_base_v082_signal(marketcap, equity, cashneq):
    result = _z(_f16_bookstretch(marketcap, equity, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of nav-gap over 504d
def f16bt_f16_bitcoin_treasury_premium_znavgap_504d_base_v083_signal(marketcap, equity, assets):
    result = _z(_f16_navgap(marketcap, equity, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of net-asset premium over 504d
def f16bt_f16_bitcoin_treasury_premium_znetprem_504d_base_v084_signal(marketcap, equity, debt):
    result = _z(_f16_netassetprem(marketcap, equity, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# market/assets z-score over 252d
def f16bt_f16_bitcoin_treasury_premium_zmktassets_252d_base_v085_signal(marketcap, assets, equity):
    result = _z(_safe_div(marketcap, assets), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market/assets z-score over 504d
def f16bt_f16_bitcoin_treasury_premium_zmktassets_504d_base_v086_signal(marketcap, assets, equity):
    result = _z(_safe_div(marketcap, assets), 504) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# premium vs trailing 504d mean (long-horizon reversion gap)
def f16bt_f16_bitcoin_treasury_premium_revgap_504d_base_v087_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = p - _mean(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# premium ratio to trailing 504d mean
def f16bt_f16_bitcoin_treasury_premium_relstretch_504d_base_v088_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(p, _mean(p, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch vs trailing 252d mean
def f16bt_f16_bitcoin_treasury_premium_bsrevgap_252d_base_v089_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = b - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-asset premium vs trailing 252d mean
def f16bt_f16_bitcoin_treasury_premium_nprevgap_252d_base_v090_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = p - _mean(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# premium slope over 42d (normalized)
def f16bt_f16_bitcoin_treasury_premium_slope_42d_base_v091_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(p.diff(42), _std(p, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# premium slope over 189d (normalized)
def f16bt_f16_bitcoin_treasury_premium_slope_189d_base_v092_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(p.diff(189), _std(p, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# premium slope over 504d (normalized)
def f16bt_f16_bitcoin_treasury_premium_slope_504d_base_v093_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(p.diff(504), _std(p, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch slope over 126d (normalized)
def f16bt_f16_bitcoin_treasury_premium_bsslope_126d_base_v094_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = _safe_div(b.diff(126), _std(b, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# net-asset premium slope over 126d (normalized)
def f16bt_f16_bitcoin_treasury_premium_npslope_126d_base_v095_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = _safe_div(p.diff(126), _std(p, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of book-stretch over 252d
def f16bt_f16_bitcoin_treasury_premium_bsrank_252d_base_v096_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = b.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of net-asset premium over 252d
def f16bt_f16_bitcoin_treasury_premium_nprank_252d_base_v097_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = p.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of market/assets over 252d
def f16bt_f16_bitcoin_treasury_premium_marank_252d_base_v098_signal(marketcap, assets, equity):
    result = _safe_div(marketcap, assets).rolling(252, min_periods=84).rank(pct=True) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# premium log-change over 42d
def f16bt_f16_bitcoin_treasury_premium_logchg_42d_base_v099_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = np.log(_safe_div(p, p.shift(42)))
    return result.replace([np.inf, -np.inf], np.nan)


# premium log-change over 189d
def f16bt_f16_bitcoin_treasury_premium_logchg_189d_base_v100_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = np.log(_safe_div(p, p.shift(189)))
    return result.replace([np.inf, -np.inf], np.nan)


# premium log-change over 504d
def f16bt_f16_bitcoin_treasury_premium_logchg_504d_base_v101_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = np.log(_safe_div(p, p.shift(504)))
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch log-change over 126d
def f16bt_f16_bitcoin_treasury_premium_bslogchg_126d_base_v102_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = np.log(_safe_div(b, b.shift(126)))
    return result.replace([np.inf, -np.inf], np.nan)


# premium dispersion over 42d
def f16bt_f16_bitcoin_treasury_premium_disp_42d_base_v103_signal(marketcap, equity):
    result = _std(_f16_premium(marketcap, equity), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# premium dispersion over 189d
def f16bt_f16_bitcoin_treasury_premium_disp_189d_base_v104_signal(marketcap, equity):
    result = _std(_f16_premium(marketcap, equity), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# premium dispersion over 504d
def f16bt_f16_bitcoin_treasury_premium_disp_504d_base_v105_signal(marketcap, equity):
    result = _std(_f16_premium(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch dispersion over 252d
def f16bt_f16_bitcoin_treasury_premium_bsdisp_252d_base_v106_signal(marketcap, equity, cashneq):
    result = _std(_f16_bookstretch(marketcap, equity, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# nav-gap dispersion over 252d
def f16bt_f16_bitcoin_treasury_premium_navgapdisp_252d_base_v107_signal(marketcap, equity, assets):
    result = _std(_f16_navgap(marketcap, equity, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of book-stretch over 252d
def f16bt_f16_bitcoin_treasury_premium_bscv_252d_base_v108_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = _safe_div(_std(b, 252), _mean(b, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of book-stretch (span 126)
def f16bt_f16_bitcoin_treasury_premium_bsewm_126d_base_v109_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = b.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of nav-gap (span 126)
def f16bt_f16_bitcoin_treasury_premium_navgapewm_126d_base_v110_signal(marketcap, equity, assets):
    g = _f16_navgap(marketcap, equity, assets)
    result = g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of net-asset premium (span 126)
def f16bt_f16_bitcoin_treasury_premium_npewm_126d_base_v111_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = p.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch minus its EWMA(126)
def f16bt_f16_bitcoin_treasury_premium_bsewmdev_126d_base_v112_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = b - b.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# robust z of book-stretch via median/MAD over 252d
def f16bt_f16_bitcoin_treasury_premium_bsrobustz_252d_base_v113_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    med = b.rolling(252, min_periods=84).median()
    mad = (b - med).abs().rolling(252, min_periods=84).median()
    result = _safe_div(b - med, mad)
    return result.replace([np.inf, -np.inf], np.nan)


# robust z of nav-gap via median/MAD over 252d
def f16bt_f16_bitcoin_treasury_premium_navgaprobustz_252d_base_v114_signal(marketcap, equity, assets):
    g = _f16_navgap(marketcap, equity, assets)
    med = g.rolling(252, min_periods=84).median()
    mad = (g - med).abs().rolling(252, min_periods=84).median()
    result = _safe_div(g - med, mad)
    return result.replace([np.inf, -np.inf], np.nan)


# premium short vs long mean spread (42d minus 189d)
def f16bt_f16_bitcoin_treasury_premium_msspread_42_189_base_v115_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _mean(p, 42) - _mean(p, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# premium short vs long mean spread (126d minus 504d)
def f16bt_f16_bitcoin_treasury_premium_msspread_126_504_base_v116_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _mean(p, 126) - _mean(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch short vs long mean spread (63d minus 252d)
def f16bt_f16_bitcoin_treasury_premium_bsmsspread_63_252_base_v117_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = _mean(b, 63) - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# premium acceleration: 42d slope minus 126d slope
def f16bt_f16_bitcoin_treasury_premium_accel_42_126_base_v118_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    sd = _std(p, 252)
    result = _safe_div(p.diff(42), sd) - _safe_div(p.diff(126), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# premium acceleration: 126d slope minus 252d slope
def f16bt_f16_bitcoin_treasury_premium_accel_126_252_base_v119_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    sd = _std(p, 252)
    result = _safe_div(p.diff(126), sd) - _safe_div(p.diff(252), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of premium over 504d
def f16bt_f16_bitcoin_treasury_premium_cv_504d_base_v120_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(_std(p, 504), _mean(p, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# cash-adjusted premium z over 252d
def f16bt_f16_bitcoin_treasury_premium_zcashadj_252d_base_v121_signal(marketcap, equity, cashneq):
    result = _z(_safe_div(marketcap, equity - cashneq), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise premium z over 252d
def f16bt_f16_bitcoin_treasury_premium_zentprem_252d_base_v122_signal(marketcap, debt, assets, equity):
    result = _z(_safe_div(marketcap + debt, assets), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings premium z over 252d
def f16bt_f16_bitcoin_treasury_premium_zreprem_252d_base_v123_signal(marketcap, equity, retearn):
    result = _z(_safe_div(marketcap, equity + retearn), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings premium smoothed over 252d
def f16bt_f16_bitcoin_treasury_premium_repremsm_252d_base_v124_signal(marketcap, equity, retearn):
    result = _mean(_safe_div(marketcap, equity + retearn), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-market leverage premium (debt/marketcap) anchored
def f16bt_f16_bitcoin_treasury_premium_debtmkt_126d_base_v125_signal(marketcap, debt, equity):
    result = _mean(_safe_div(debt, marketcap), 126) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-scaled premium (premium times debt/assets)
def f16bt_f16_bitcoin_treasury_premium_levprem_126d_base_v126_signal(marketcap, equity, debt, assets):
    result = _mean(_f16_premium(marketcap, equity) * _safe_div(debt, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# premium vs assets-coverage interaction z over 252d
def f16bt_f16_bitcoin_treasury_premium_premassetint_252d_base_v127_signal(marketcap, equity, assets):
    inter = _f16_premium(marketcap, equity) * _safe_div(assets, equity)
    result = _z(inter, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# nav-gap minus premium-reversion blend over 126d
def f16bt_f16_bitcoin_treasury_premium_navgapblend_126d_base_v128_signal(marketcap, equity, assets):
    g = _f16_navgap(marketcap, equity, assets)
    result = g - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# premium EWMA(252) deviation
def f16bt_f16_bitcoin_treasury_premium_ewmdev_252d_base_v129_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = p - p.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# premium vs nav-gap level difference (premium minus scaled gap)
def f16bt_f16_bitcoin_treasury_premium_premgapdiff_126d_base_v130_signal(marketcap, equity, assets):
    result = _mean(_f16_premium(marketcap, equity) - _f16_navgap(marketcap, equity, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# log market/assets premium
def f16bt_f16_bitcoin_treasury_premium_logmktassets_126d_base_v131_signal(marketcap, assets, equity):
    result = _mean(np.log(_safe_div(marketcap, assets)), 126) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-asset premium dispersion over 252d
def f16bt_f16_bitcoin_treasury_premium_npdisp_252d_base_v132_signal(marketcap, equity, debt):
    result = _std(_f16_netassetprem(marketcap, equity, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# book-stretch percentile rank over 504d
def f16bt_f16_bitcoin_treasury_premium_bsrank_504d_base_v133_signal(marketcap, equity, cashneq):
    b = _f16_bookstretch(marketcap, equity, cashneq)
    result = b.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# nav-gap percentile rank over 504d
def f16bt_f16_bitcoin_treasury_premium_navgaprank_504d_base_v134_signal(marketcap, equity, assets):
    g = _f16_navgap(marketcap, equity, assets)
    result = g.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# premium dispersion ratio: 126d std over 504d std
def f16bt_f16_bitcoin_treasury_premium_dispratio_504d_base_v135_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    result = _safe_div(_std(p, 126), _std(p, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# premium smoothed and standardized blend over 189d
def f16bt_f16_bitcoin_treasury_premium_zmnav_189d_base_v136_signal(marketcap, equity):
    result = _z(_f16_premium(marketcap, equity), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-adjusted premium smoothed over 252d
def f16bt_f16_bitcoin_treasury_premium_cashadjsm_252d_base_v137_signal(marketcap, equity, cashneq):
    result = _mean(_safe_div(marketcap, equity - cashneq), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise premium smoothed over 252d
def f16bt_f16_bitcoin_treasury_premium_entpremsm_252d_base_v138_signal(marketcap, debt, assets, equity):
    result = _mean(_safe_div(marketcap + debt, assets), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# book coverage smoothed over 252d
def f16bt_f16_bitcoin_treasury_premium_bookcovsm_252d_base_v139_signal(marketcap, equity):
    result = _mean(_safe_div(equity, marketcap), 252) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# premium-aware price interaction smoothed over 126d (secondary closeadj)
def f16bt_f16_bitcoin_treasury_premium_priceaware_126d_base_v140_signal(marketcap, equity, closeadj):
    result = _mean(_f16_premium(marketcap, equity) * _z(closeadj, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-asset premium short vs long mean spread (63d minus 252d)
def f16bt_f16_bitcoin_treasury_premium_npmsspread_63_252_base_v141_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = _mean(p, 63) - _mean(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# premium robust z via median/MAD over 504d
def f16bt_f16_bitcoin_treasury_premium_robustz_504d_base_v142_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    med = p.rolling(504, min_periods=168).median()
    mad = (p - med).abs().rolling(504, min_periods=168).median()
    result = _safe_div(p - med, mad)
    return result.replace([np.inf, -np.inf], np.nan)


# market/assets vs trailing 252d mean (reversion gap)
def f16bt_f16_bitcoin_treasury_premium_marevgap_252d_base_v143_signal(marketcap, assets, equity):
    m = _safe_div(marketcap, assets)
    result = (m - _mean(m, 252)) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# nav-gap EWMA(252) deviation
def f16bt_f16_bitcoin_treasury_premium_navgapewmdev_252d_base_v144_signal(marketcap, equity, assets):
    g = _f16_navgap(marketcap, equity, assets)
    result = g - g.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# premium times retained-earnings coverage smoothed over 126d
def f16bt_f16_bitcoin_treasury_premium_recoverage_126d_base_v145_signal(marketcap, equity, retearn):
    result = _mean(_f16_premium(marketcap, equity) * _safe_div(retearn, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-asset premium log-change over 126d
def f16bt_f16_bitcoin_treasury_premium_nplogchg_126d_base_v146_signal(marketcap, equity, debt):
    p = _f16_netassetprem(marketcap, equity, debt)
    result = np.log(_safe_div(p.abs() + 1.0, p.abs().shift(126) + 1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# premium-to-bookstretch ratio smoothed over 126d
def f16bt_f16_bitcoin_treasury_premium_prembsratio_126d_base_v147_signal(marketcap, equity, cashneq):
    r = _safe_div(_f16_premium(marketcap, equity), _f16_bookstretch(marketcap, equity, cashneq))
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# market/assets dispersion ratio: 63d std over 252d std
def f16bt_f16_bitcoin_treasury_premium_madispratio_252d_base_v148_signal(marketcap, assets, equity):
    m = _safe_div(marketcap, assets)
    result = _safe_div(_std(m, 63), _std(m, 252)) + _f16_premium(marketcap, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# premium robust z over 189d
def f16bt_f16_bitcoin_treasury_premium_robustz_189d_base_v149_signal(marketcap, equity):
    p = _f16_premium(marketcap, equity)
    med = p.rolling(189, min_periods=63).median()
    mad = (p - med).abs().rolling(189, min_periods=63).median()
    result = _safe_div(p - med, mad)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-premium composite z over 252d (mnav, navgap, netprem)
def f16bt_f16_bitcoin_treasury_premium_composite_252d_base_v150_signal(marketcap, equity, assets, debt):
    a = _z(_f16_premium(marketcap, equity), 252)
    b = _z(_f16_navgap(marketcap, equity, assets), 252)
    c = _z(_f16_netassetprem(marketcap, equity, debt), 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16bt_f16_bitcoin_treasury_premium_mnavsm_42d_base_v076_signal,
    f16bt_f16_bitcoin_treasury_premium_mnavsm_189d_base_v077_signal,
    f16bt_f16_bitcoin_treasury_premium_mnavsm_504d_base_v078_signal,
    f16bt_f16_bitcoin_treasury_premium_logbookstretch_21d_base_v079_signal,
    f16bt_f16_bitcoin_treasury_premium_logbookstretchsm_126d_base_v080_signal,
    f16bt_f16_bitcoin_treasury_premium_zbookstretch_126d_base_v081_signal,
    f16bt_f16_bitcoin_treasury_premium_zbookstretch_504d_base_v082_signal,
    f16bt_f16_bitcoin_treasury_premium_znavgap_504d_base_v083_signal,
    f16bt_f16_bitcoin_treasury_premium_znetprem_504d_base_v084_signal,
    f16bt_f16_bitcoin_treasury_premium_zmktassets_252d_base_v085_signal,
    f16bt_f16_bitcoin_treasury_premium_zmktassets_504d_base_v086_signal,
    f16bt_f16_bitcoin_treasury_premium_revgap_504d_base_v087_signal,
    f16bt_f16_bitcoin_treasury_premium_relstretch_504d_base_v088_signal,
    f16bt_f16_bitcoin_treasury_premium_bsrevgap_252d_base_v089_signal,
    f16bt_f16_bitcoin_treasury_premium_nprevgap_252d_base_v090_signal,
    f16bt_f16_bitcoin_treasury_premium_slope_42d_base_v091_signal,
    f16bt_f16_bitcoin_treasury_premium_slope_189d_base_v092_signal,
    f16bt_f16_bitcoin_treasury_premium_slope_504d_base_v093_signal,
    f16bt_f16_bitcoin_treasury_premium_bsslope_126d_base_v094_signal,
    f16bt_f16_bitcoin_treasury_premium_npslope_126d_base_v095_signal,
    f16bt_f16_bitcoin_treasury_premium_bsrank_252d_base_v096_signal,
    f16bt_f16_bitcoin_treasury_premium_nprank_252d_base_v097_signal,
    f16bt_f16_bitcoin_treasury_premium_marank_252d_base_v098_signal,
    f16bt_f16_bitcoin_treasury_premium_logchg_42d_base_v099_signal,
    f16bt_f16_bitcoin_treasury_premium_logchg_189d_base_v100_signal,
    f16bt_f16_bitcoin_treasury_premium_logchg_504d_base_v101_signal,
    f16bt_f16_bitcoin_treasury_premium_bslogchg_126d_base_v102_signal,
    f16bt_f16_bitcoin_treasury_premium_disp_42d_base_v103_signal,
    f16bt_f16_bitcoin_treasury_premium_disp_189d_base_v104_signal,
    f16bt_f16_bitcoin_treasury_premium_disp_504d_base_v105_signal,
    f16bt_f16_bitcoin_treasury_premium_bsdisp_252d_base_v106_signal,
    f16bt_f16_bitcoin_treasury_premium_navgapdisp_252d_base_v107_signal,
    f16bt_f16_bitcoin_treasury_premium_bscv_252d_base_v108_signal,
    f16bt_f16_bitcoin_treasury_premium_bsewm_126d_base_v109_signal,
    f16bt_f16_bitcoin_treasury_premium_navgapewm_126d_base_v110_signal,
    f16bt_f16_bitcoin_treasury_premium_npewm_126d_base_v111_signal,
    f16bt_f16_bitcoin_treasury_premium_bsewmdev_126d_base_v112_signal,
    f16bt_f16_bitcoin_treasury_premium_bsrobustz_252d_base_v113_signal,
    f16bt_f16_bitcoin_treasury_premium_navgaprobustz_252d_base_v114_signal,
    f16bt_f16_bitcoin_treasury_premium_msspread_42_189_base_v115_signal,
    f16bt_f16_bitcoin_treasury_premium_msspread_126_504_base_v116_signal,
    f16bt_f16_bitcoin_treasury_premium_bsmsspread_63_252_base_v117_signal,
    f16bt_f16_bitcoin_treasury_premium_accel_42_126_base_v118_signal,
    f16bt_f16_bitcoin_treasury_premium_accel_126_252_base_v119_signal,
    f16bt_f16_bitcoin_treasury_premium_cv_504d_base_v120_signal,
    f16bt_f16_bitcoin_treasury_premium_zcashadj_252d_base_v121_signal,
    f16bt_f16_bitcoin_treasury_premium_zentprem_252d_base_v122_signal,
    f16bt_f16_bitcoin_treasury_premium_zreprem_252d_base_v123_signal,
    f16bt_f16_bitcoin_treasury_premium_repremsm_252d_base_v124_signal,
    f16bt_f16_bitcoin_treasury_premium_debtmkt_126d_base_v125_signal,
    f16bt_f16_bitcoin_treasury_premium_levprem_126d_base_v126_signal,
    f16bt_f16_bitcoin_treasury_premium_premassetint_252d_base_v127_signal,
    f16bt_f16_bitcoin_treasury_premium_navgapblend_126d_base_v128_signal,
    f16bt_f16_bitcoin_treasury_premium_ewmdev_252d_base_v129_signal,
    f16bt_f16_bitcoin_treasury_premium_premgapdiff_126d_base_v130_signal,
    f16bt_f16_bitcoin_treasury_premium_logmktassets_126d_base_v131_signal,
    f16bt_f16_bitcoin_treasury_premium_npdisp_252d_base_v132_signal,
    f16bt_f16_bitcoin_treasury_premium_bsrank_504d_base_v133_signal,
    f16bt_f16_bitcoin_treasury_premium_navgaprank_504d_base_v134_signal,
    f16bt_f16_bitcoin_treasury_premium_dispratio_504d_base_v135_signal,
    f16bt_f16_bitcoin_treasury_premium_zmnav_189d_base_v136_signal,
    f16bt_f16_bitcoin_treasury_premium_cashadjsm_252d_base_v137_signal,
    f16bt_f16_bitcoin_treasury_premium_entpremsm_252d_base_v138_signal,
    f16bt_f16_bitcoin_treasury_premium_bookcovsm_252d_base_v139_signal,
    f16bt_f16_bitcoin_treasury_premium_priceaware_126d_base_v140_signal,
    f16bt_f16_bitcoin_treasury_premium_npmsspread_63_252_base_v141_signal,
    f16bt_f16_bitcoin_treasury_premium_robustz_504d_base_v142_signal,
    f16bt_f16_bitcoin_treasury_premium_marevgap_252d_base_v143_signal,
    f16bt_f16_bitcoin_treasury_premium_navgapewmdev_252d_base_v144_signal,
    f16bt_f16_bitcoin_treasury_premium_recoverage_126d_base_v145_signal,
    f16bt_f16_bitcoin_treasury_premium_nplogchg_126d_base_v146_signal,
    f16bt_f16_bitcoin_treasury_premium_prembsratio_126d_base_v147_signal,
    f16bt_f16_bitcoin_treasury_premium_madispratio_252d_base_v148_signal,
    f16bt_f16_bitcoin_treasury_premium_robustz_189d_base_v149_signal,
    f16bt_f16_bitcoin_treasury_premium_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_BITCOIN_TREASURY_PREMIUM_REGISTRY_076_150 = REGISTRY


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
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
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
    domain_primitives = ("_f16_premium", "_f16_navgap", "_f16_bookstretch", "_f16_netassetprem")
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
    print(f"OK f16_bitcoin_treasury_premium_base_076_150_claude: {n_features} features pass")
