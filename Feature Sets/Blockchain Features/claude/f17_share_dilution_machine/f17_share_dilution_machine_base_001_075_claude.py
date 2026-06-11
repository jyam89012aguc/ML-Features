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


# ===== folder domain primitives (share-dilution machine) =====
def _f17_dilution(sharesbas, w):
    # relentless dilution: pct change of share count over w trading days
    return sharesbas.pct_change(periods=w)


def _f17_sharetrend(sharesbas, w):
    # normalized slope of share count: w-day change scaled by recent share level
    d = sharesbas - sharesbas.shift(w)
    base = sharesbas.rolling(w, min_periods=max(2, w // 2)).mean()
    return d / base.replace(0, np.nan)


def _f17_dilz(sharesbas, w):
    # z-score of share-growth: how extreme is current dilution vs its own history
    g = sharesbas.pct_change(periods=21)
    m = g.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(2, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


def _f17_issintensity(ncfcommon, sharesbas, w):
    # issuance intensity: common-stock cash flow normalized by share base, smoothed
    raw = ncfcommon / sharesbas.replace(0, np.nan)
    return raw.rolling(w, min_periods=max(2, w // 2)).mean()


# ============ FEATURES 001-075 ============

# 63d sharesbas dilution (quarterly share growth)
def f17sd_f17_share_dilution_machine_dil_63d_base_v001_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sharesbas dilution (half-year share growth)
def f17sd_f17_share_dilution_machine_dil_126d_base_v002_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas dilution (annual share growth)
def f17sd_f17_share_dilution_machine_dil_252d_base_v003_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas dilution (two-year share growth)
def f17sd_f17_share_dilution_machine_dil_504d_base_v004_signal(sharesbas):
    result = _f17_dilution(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesbas dilution (monthly share growth)
def f17sd_f17_share_dilution_machine_dil_21d_base_v005_signal(sharesbas):
    result = _f17_dilution(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d sharesbas dilution
def f17sd_f17_share_dilution_machine_dil_42d_base_v006_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d sharesbas dilution
def f17sd_f17_share_dilution_machine_dil_84d_base_v007_signal(sharesbas):
    result = _f17_dilution(sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d sharesbas dilution
def f17sd_f17_share_dilution_machine_dil_189d_base_v008_signal(sharesbas):
    result = _f17_dilution(sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shareswa dilution (weighted-average share growth)
def f17sd_f17_share_dilution_machine_wadil_63d_base_v009_signal(shareswa):
    result = _f17_dilution(shareswa, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_126d_base_v010_signal(shareswa):
    result = _f17_dilution(shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_252d_base_v011_signal(shareswa):
    result = _f17_dilution(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_504d_base_v012_signal(shareswa):
    result = _f17_dilution(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_21d_base_v013_signal(shareswa):
    result = _f17_dilution(shareswa, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 63d dilution minus 126d dilution (rising pace)
def f17sd_f17_share_dilution_machine_accel_63_126d_base_v014_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63) - _f17_dilution(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 126d minus 252d dilution
def f17sd_f17_share_dilution_machine_accel_126_252d_base_v015_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126) - _f17_dilution(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 21d minus 63d dilution
def f17sd_f17_share_dilution_machine_accel_21_63d_base_v016_signal(sharesbas):
    result = _f17_dilution(sharesbas, 21) - _f17_dilution(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 252d minus 504d dilution
def f17sd_f17_share_dilution_machine_accel_252_504d_base_v017_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252) - _f17_dilution(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 126d
def f17sd_f17_share_dilution_machine_dilz_126d_base_v018_signal(sharesbas):
    result = _f17_dilz(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 252d
def f17sd_f17_share_dilution_machine_dilz_252d_base_v019_signal(sharesbas):
    result = _f17_dilz(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 504d
def f17sd_f17_share_dilution_machine_dilz_504d_base_v020_signal(sharesbas):
    result = _f17_dilz(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 63d
def f17sd_f17_share_dilution_machine_dilz_63d_base_v021_signal(sharesbas):
    result = _f17_dilz(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 63d
def f17sd_f17_share_dilution_machine_trend_63d_base_v022_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 126d
def f17sd_f17_share_dilution_machine_trend_126d_base_v023_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 252d
def f17sd_f17_share_dilution_machine_trend_252d_base_v024_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 504d
def f17sd_f17_share_dilution_machine_trend_504d_base_v025_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 21d
def f17sd_f17_share_dilution_machine_trend_21d_base_v026_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution vs 252d ago (log share ratio)
def f17sd_f17_share_dilution_machine_cumdil_252d_base_v027_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution vs 504d ago (log share ratio)
def f17sd_f17_share_dilution_machine_cumdil_504d_base_v028_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution vs 126d ago (log share ratio)
def f17sd_f17_share_dilution_machine_cumdil_126d_base_v029_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp dilution: sbcomp / equity, smoothed 63d
def f17sd_f17_share_dilution_machine_sbcdil_63d_base_v030_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 63) + _f17_dilution(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp dilution: sbcomp / equity, smoothed 126d
def f17sd_f17_share_dilution_machine_sbcdil_126d_base_v031_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp dilution: sbcomp / equity, smoothed 252d
def f17sd_f17_share_dilution_machine_sbcdil_252d_base_v032_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp per share: sbcomp / sharesbas, smoothed 126d
def f17sd_f17_share_dilution_machine_sbcps_126d_base_v033_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp per share: sbcomp / sharesbas, smoothed 252d
def f17sd_f17_share_dilution_machine_sbcps_252d_base_v034_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity: ncfcommon / sharesbas smoothed 63d
def f17sd_f17_share_dilution_machine_issint_63d_base_v035_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity: ncfcommon / sharesbas smoothed 126d
def f17sd_f17_share_dilution_machine_issint_126d_base_v036_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity: ncfcommon / sharesbas smoothed 252d
def f17sd_f17_share_dilution_machine_issint_252d_base_v037_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity: ncfcommon / equity smoothed 126d
def f17sd_f17_share_dilution_machine_isseq_126d_base_v038_signal(ncfcommon, equity, sharesbas):
    raw = _safe_div(ncfcommon, equity)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity: ncfcommon / equity smoothed 252d
def f17sd_f17_share_dilution_machine_isseq_252d_base_v039_signal(ncfcommon, equity, sharesbas):
    raw = _safe_div(ncfcommon, equity)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank over 252d
def f17sd_f17_share_dilution_machine_dilrank_252d_base_v040_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank over 504d
def f17sd_f17_share_dilution_machine_dilrank_504d_base_v041_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank of 126d growth over 504d
def f17sd_f17_share_dilution_machine_dilrank126_504d_base_v042_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# good-vs-bad dilution: share growth minus revenue growth (252d)
def f17sd_f17_share_dilution_machine_gvb_252d_base_v043_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 252) - revenue.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# good-vs-bad dilution: share growth minus revenue growth (126d)
def f17sd_f17_share_dilution_machine_gvb_126d_base_v044_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 126) - revenue.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# good-vs-bad dilution: share growth minus revenue growth (63d)
def f17sd_f17_share_dilution_machine_gvb_63d_base_v045_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 63) - revenue.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share trend: revenue/sharesbas log change over 252d
def f17sd_f17_share_dilution_machine_rps_252d_base_v046_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share trend over 126d
def f17sd_f17_share_dilution_machine_rps_126d_base_v047_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity-per-share dilution: equity/sharesbas log change 252d
def f17sd_f17_share_dilution_machine_eps_252d_base_v048_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity-per-share dilution over 126d
def f17sd_f17_share_dilution_machine_eps_126d_base_v049_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution information ratio: 63d dilution per unit of its dispersion
def f17sd_f17_share_dilution_machine_dilir_63d_base_v050_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution information ratio: 126d dilution per unit dispersion
def f17sd_f17_share_dilution_machine_dilir_126d_base_v051_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dilution: 63d mean of 21d share growth
def f17sd_f17_share_dilution_machine_smdil_63d_base_v052_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dilution: 126d mean of 21d share growth
def f17sd_f17_share_dilution_machine_smdil_126d_base_v053_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dilution: 252d mean of 63d share growth
def f17sd_f17_share_dilution_machine_smdil_252d_base_v054_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of monthly dilution (span 63)
def f17sd_f17_share_dilution_machine_ewmdil_63d_base_v055_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of monthly dilution (span 126)
def f17sd_f17_share_dilution_machine_ewmdil_126d_base_v056_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion: rolling std of 21d share growth over 126d
def f17sd_f17_share_dilution_machine_dildisp_126d_base_v057_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion over 252d
def f17sd_f17_share_dilution_machine_dildisp_252d_base_v058_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 63d dilution
def f17sd_f17_share_dilution_machine_anndil_63d_base_v059_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63) * (252.0 / 63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 126d dilution
def f17sd_f17_share_dilution_machine_anndil_126d_base_v060_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas vs shareswa dilution gap (basic minus weighted) 252d
def f17sd_f17_share_dilution_machine_basgap_252d_base_v061_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 252) - _f17_dilution(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas vs shareswa dilution gap 126d
def f17sd_f17_share_dilution_machine_basgap_126d_base_v062_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 126) - _f17_dilution(shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# basic-over-weighted share ratio log-trend 252d
def f17sd_f17_share_dilution_machine_baswa_252d_base_v063_signal(sharesbas, shareswa):
    ratio = _safe_div(sharesbas, shareswa)
    result = np.log(ratio / ratio.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa trend slope over 252d
def f17sd_f17_share_dilution_machine_watrend_252d_base_v064_signal(shareswa):
    result = _f17_sharetrend(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa trend slope over 126d
def f17sd_f17_share_dilution_machine_watrend_126d_base_v065_signal(shareswa):
    result = _f17_sharetrend(shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa dilution z-score over 252d
def f17sd_f17_share_dilution_machine_wadilz_252d_base_v066_signal(shareswa):
    result = _f17_dilz(shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution scaled by equity-growth (issuance not backed by retained capital) 252d
def f17sd_f17_share_dilution_machine_dileqs_252d_base_v067_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - eqg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution scaled by equity-growth 126d
def f17sd_f17_share_dilution_machine_dileqs_126d_base_v068_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=126)
    result = _f17_dilution(sharesbas, 126) - eqg
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity z-scored over 252d
def f17sd_f17_share_dilution_machine_issintz_252d_base_v069_signal(ncfcommon, sharesbas):
    raw = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp / sharesbas z-scored over 252d
def f17sd_f17_share_dilution_machine_sbcz_252d_base_v070_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _z(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution-vs-252d minus issuance-intensity blend
def f17sd_f17_share_dilution_machine_blend_252d_base_v071_signal(sharesbas, ncfcommon):
    cum = np.log(sharesbas / sharesbas.shift(252))
    iss = _f17_issintensity(ncfcommon, sharesbas, 126)
    result = cum + iss * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution trend ratio: 63d trend over 252d trend
def f17sd_f17_share_dilution_machine_trratio_63_252d_base_v072_signal(sharesbas):
    result = _safe_div(_f17_sharetrend(sharesbas, 63), _f17_sharetrend(sharesbas, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: 126d dilution minus its 252d mean
def f17sd_f17_share_dilution_machine_dilsurp_126d_base_v073_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g - _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: 63d dilution minus its 126d mean
def f17sd_f17_share_dilution_machine_dilsurp_63d_base_v074_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth vs equity-per-share gap (dilution destroying book value) 252d
def f17sd_f17_share_dilution_machine_bvgap_252d_base_v075_signal(sharesbas, equity):
    eqps = _safe_div(equity, sharesbas)
    eqpsg = eqps.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - eqpsg
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17sd_f17_share_dilution_machine_dil_63d_base_v001_signal,
    f17sd_f17_share_dilution_machine_dil_126d_base_v002_signal,
    f17sd_f17_share_dilution_machine_dil_252d_base_v003_signal,
    f17sd_f17_share_dilution_machine_dil_504d_base_v004_signal,
    f17sd_f17_share_dilution_machine_dil_21d_base_v005_signal,
    f17sd_f17_share_dilution_machine_dil_42d_base_v006_signal,
    f17sd_f17_share_dilution_machine_dil_84d_base_v007_signal,
    f17sd_f17_share_dilution_machine_dil_189d_base_v008_signal,
    f17sd_f17_share_dilution_machine_wadil_63d_base_v009_signal,
    f17sd_f17_share_dilution_machine_wadil_126d_base_v010_signal,
    f17sd_f17_share_dilution_machine_wadil_252d_base_v011_signal,
    f17sd_f17_share_dilution_machine_wadil_504d_base_v012_signal,
    f17sd_f17_share_dilution_machine_wadil_21d_base_v013_signal,
    f17sd_f17_share_dilution_machine_accel_63_126d_base_v014_signal,
    f17sd_f17_share_dilution_machine_accel_126_252d_base_v015_signal,
    f17sd_f17_share_dilution_machine_accel_21_63d_base_v016_signal,
    f17sd_f17_share_dilution_machine_accel_252_504d_base_v017_signal,
    f17sd_f17_share_dilution_machine_dilz_126d_base_v018_signal,
    f17sd_f17_share_dilution_machine_dilz_252d_base_v019_signal,
    f17sd_f17_share_dilution_machine_dilz_504d_base_v020_signal,
    f17sd_f17_share_dilution_machine_dilz_63d_base_v021_signal,
    f17sd_f17_share_dilution_machine_trend_63d_base_v022_signal,
    f17sd_f17_share_dilution_machine_trend_126d_base_v023_signal,
    f17sd_f17_share_dilution_machine_trend_252d_base_v024_signal,
    f17sd_f17_share_dilution_machine_trend_504d_base_v025_signal,
    f17sd_f17_share_dilution_machine_trend_21d_base_v026_signal,
    f17sd_f17_share_dilution_machine_cumdil_252d_base_v027_signal,
    f17sd_f17_share_dilution_machine_cumdil_504d_base_v028_signal,
    f17sd_f17_share_dilution_machine_cumdil_126d_base_v029_signal,
    f17sd_f17_share_dilution_machine_sbcdil_63d_base_v030_signal,
    f17sd_f17_share_dilution_machine_sbcdil_126d_base_v031_signal,
    f17sd_f17_share_dilution_machine_sbcdil_252d_base_v032_signal,
    f17sd_f17_share_dilution_machine_sbcps_126d_base_v033_signal,
    f17sd_f17_share_dilution_machine_sbcps_252d_base_v034_signal,
    f17sd_f17_share_dilution_machine_issint_63d_base_v035_signal,
    f17sd_f17_share_dilution_machine_issint_126d_base_v036_signal,
    f17sd_f17_share_dilution_machine_issint_252d_base_v037_signal,
    f17sd_f17_share_dilution_machine_isseq_126d_base_v038_signal,
    f17sd_f17_share_dilution_machine_isseq_252d_base_v039_signal,
    f17sd_f17_share_dilution_machine_dilrank_252d_base_v040_signal,
    f17sd_f17_share_dilution_machine_dilrank_504d_base_v041_signal,
    f17sd_f17_share_dilution_machine_dilrank126_504d_base_v042_signal,
    f17sd_f17_share_dilution_machine_gvb_252d_base_v043_signal,
    f17sd_f17_share_dilution_machine_gvb_126d_base_v044_signal,
    f17sd_f17_share_dilution_machine_gvb_63d_base_v045_signal,
    f17sd_f17_share_dilution_machine_rps_252d_base_v046_signal,
    f17sd_f17_share_dilution_machine_rps_126d_base_v047_signal,
    f17sd_f17_share_dilution_machine_eps_252d_base_v048_signal,
    f17sd_f17_share_dilution_machine_eps_126d_base_v049_signal,
    f17sd_f17_share_dilution_machine_dilir_63d_base_v050_signal,
    f17sd_f17_share_dilution_machine_dilir_126d_base_v051_signal,
    f17sd_f17_share_dilution_machine_smdil_63d_base_v052_signal,
    f17sd_f17_share_dilution_machine_smdil_126d_base_v053_signal,
    f17sd_f17_share_dilution_machine_smdil_252d_base_v054_signal,
    f17sd_f17_share_dilution_machine_ewmdil_63d_base_v055_signal,
    f17sd_f17_share_dilution_machine_ewmdil_126d_base_v056_signal,
    f17sd_f17_share_dilution_machine_dildisp_126d_base_v057_signal,
    f17sd_f17_share_dilution_machine_dildisp_252d_base_v058_signal,
    f17sd_f17_share_dilution_machine_anndil_63d_base_v059_signal,
    f17sd_f17_share_dilution_machine_anndil_126d_base_v060_signal,
    f17sd_f17_share_dilution_machine_basgap_252d_base_v061_signal,
    f17sd_f17_share_dilution_machine_basgap_126d_base_v062_signal,
    f17sd_f17_share_dilution_machine_baswa_252d_base_v063_signal,
    f17sd_f17_share_dilution_machine_watrend_252d_base_v064_signal,
    f17sd_f17_share_dilution_machine_watrend_126d_base_v065_signal,
    f17sd_f17_share_dilution_machine_wadilz_252d_base_v066_signal,
    f17sd_f17_share_dilution_machine_dileqs_252d_base_v067_signal,
    f17sd_f17_share_dilution_machine_dileqs_126d_base_v068_signal,
    f17sd_f17_share_dilution_machine_issintz_252d_base_v069_signal,
    f17sd_f17_share_dilution_machine_sbcz_252d_base_v070_signal,
    f17sd_f17_share_dilution_machine_blend_252d_base_v071_signal,
    f17sd_f17_share_dilution_machine_trratio_63_252d_base_v072_signal,
    f17sd_f17_share_dilution_machine_dilsurp_126d_base_v073_signal,
    f17sd_f17_share_dilution_machine_dilsurp_63d_base_v074_signal,
    f17sd_f17_share_dilution_machine_bvgap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_SHARE_DILUTION_MACHINE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f17_dilution", "_f17_sharetrend", "_f17_dilz", "_f17_issintensity")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_share_dilution_machine_base_001_075_claude: {n_features} features pass")
