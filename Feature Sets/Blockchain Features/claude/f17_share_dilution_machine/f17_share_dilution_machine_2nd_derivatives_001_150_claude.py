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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f17sd_f17_share_dilution_machine_dil_63d_slope_v001_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_126d_slope_v002_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_252d_slope_v003_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_504d_slope_v004_signal(sharesbas):
    result = _f17_dilution(sharesbas, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_21d_slope_v005_signal(sharesbas):
    result = _f17_dilution(sharesbas, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_42d_slope_v006_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_84d_slope_v007_signal(sharesbas):
    result = _f17_dilution(sharesbas, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_189d_slope_v008_signal(sharesbas):
    result = _f17_dilution(sharesbas, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_63d_slope_v009_signal(shareswa):
    result = _f17_dilution(shareswa, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_126d_slope_v010_signal(shareswa):
    result = _f17_dilution(shareswa, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_252d_slope_v011_signal(shareswa):
    result = _f17_dilution(shareswa, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_504d_slope_v012_signal(shareswa):
    result = _f17_dilution(shareswa, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_21d_slope_v013_signal(shareswa):
    result = _f17_dilution(shareswa, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_63_126d_slope_v014_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63) - _f17_dilution(sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_126_252d_slope_v015_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126) - _f17_dilution(sharesbas, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_21_63d_slope_v016_signal(sharesbas):
    result = _f17_dilution(sharesbas, 21) - _f17_dilution(sharesbas, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_252_504d_slope_v017_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252) - _f17_dilution(sharesbas, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_126d_slope_v018_signal(sharesbas):
    result = _f17_dilz(sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_252d_slope_v019_signal(sharesbas):
    result = _f17_dilz(sharesbas, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_504d_slope_v020_signal(sharesbas):
    result = _f17_dilz(sharesbas, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_63d_slope_v021_signal(sharesbas):
    result = _f17_dilz(sharesbas, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_63d_slope_v022_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_126d_slope_v023_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_252d_slope_v024_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_504d_slope_v025_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_21d_slope_v026_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cumdil_252d_slope_v027_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cumdil_504d_slope_v028_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cumdil_126d_slope_v029_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcdil_63d_slope_v030_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 63) + _f17_dilution(sharesbas, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcdil_126d_slope_v031_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcdil_252d_slope_v032_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcps_126d_slope_v033_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcps_252d_slope_v034_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issint_63d_slope_v035_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issint_126d_slope_v036_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issint_252d_slope_v037_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_isseq_126d_slope_v038_signal(ncfcommon, equity, sharesbas):
    raw = _safe_div(ncfcommon, equity)
    result = _mean(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_isseq_252d_slope_v039_signal(ncfcommon, equity, sharesbas):
    raw = _safe_div(ncfcommon, equity)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank_252d_slope_v040_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank_504d_slope_v041_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank126_504d_slope_v042_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_gvb_252d_slope_v043_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 252) - revenue.pct_change(periods=252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_gvb_126d_slope_v044_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 126) - revenue.pct_change(periods=126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_gvb_63d_slope_v045_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 63) - revenue.pct_change(periods=63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_rps_252d_slope_v046_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_rps_126d_slope_v047_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_eps_252d_slope_v048_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_eps_126d_slope_v049_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilir_63d_slope_v050_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilir_126d_slope_v051_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_smdil_63d_slope_v052_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_smdil_126d_slope_v053_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_smdil_252d_slope_v054_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 63), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_ewmdil_63d_slope_v055_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_ewmdil_126d_slope_v056_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dildisp_126d_slope_v057_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dildisp_252d_slope_v058_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_anndil_63d_slope_v059_signal(sharesbas):
    result = _f17_dilution(sharesbas, 63) * (252.0 / 63.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_anndil_126d_slope_v060_signal(sharesbas):
    result = _f17_dilution(sharesbas, 126) * (252.0 / 126.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_basgap_252d_slope_v061_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 252) - _f17_dilution(shareswa, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_basgap_126d_slope_v062_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 126) - _f17_dilution(shareswa, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_baswa_252d_slope_v063_signal(sharesbas, shareswa):
    ratio = _safe_div(sharesbas, shareswa)
    result = np.log(ratio / ratio.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_watrend_252d_slope_v064_signal(shareswa):
    result = _f17_sharetrend(shareswa, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_watrend_126d_slope_v065_signal(shareswa):
    result = _f17_sharetrend(shareswa, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadilz_252d_slope_v066_signal(shareswa):
    result = _f17_dilz(shareswa, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dileqs_252d_slope_v067_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - eqg
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dileqs_126d_slope_v068_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=126)
    result = _f17_dilution(sharesbas, 126) - eqg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issintz_252d_slope_v069_signal(ncfcommon, sharesbas):
    raw = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _z(raw, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcz_252d_slope_v070_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _z(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_blend_252d_slope_v071_signal(sharesbas, ncfcommon):
    cum = np.log(sharesbas / sharesbas.shift(252))
    iss = _f17_issintensity(ncfcommon, sharesbas, 126)
    result = cum + iss * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trratio_63_252d_slope_v072_signal(sharesbas):
    result = _safe_div(_f17_sharetrend(sharesbas, 63), _f17_sharetrend(sharesbas, 252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilsurp_126d_slope_v073_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g - _mean(g, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilsurp_63d_slope_v074_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g - _mean(g, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_bvgap_252d_slope_v075_signal(sharesbas, equity):
    eqps = _safe_div(equity, sharesbas)
    eqpsg = eqps.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - eqpsg
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_315d_slope_v076_signal(sharesbas):
    result = _f17_dilution(sharesbas, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_378d_slope_v077_signal(sharesbas):
    result = _f17_dilution(sharesbas, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dil_10d_slope_v078_signal(sharesbas):
    result = _f17_dilution(sharesbas, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_189d_slope_v079_signal(shareswa):
    result = _f17_dilution(shareswa, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadil_84d_slope_v080_signal(shareswa):
    result = _f17_dilution(shareswa, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cumdil_189d_slope_v081_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(189)) + _f17_dilution(sharesbas, 189) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cumdil_378d_slope_v082_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(378)) + _f17_dilution(sharesbas, 378) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_84_189d_slope_v083_signal(sharesbas):
    result = _f17_dilution(sharesbas, 84) - _f17_dilution(sharesbas, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_accel_42_126d_slope_v084_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42) - _f17_dilution(sharesbas, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_189d_slope_v085_signal(sharesbas):
    result = _f17_dilz(sharesbas, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_315d_slope_v086_signal(sharesbas):
    result = _f17_dilz(sharesbas, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_189d_slope_v087_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_315d_slope_v088_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_84d_slope_v089_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcdil_189d_slope_v090_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 189) + _f17_dilution(sharesbas, 189) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcps_63d_slope_v091_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 63) + _f17_dilution(sharesbas, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcrev_252d_slope_v092_signal(sbcomp, revenue, sharesbas):
    raw = _safe_div(sbcomp, revenue)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcrevtr_252d_slope_v093_signal(sbcomp, revenue, sharesbas):
    raw = _safe_div(sbcomp, revenue)
    result = np.log(raw / raw.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issint_189d_slope_v094_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issint_42d_slope_v095_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issrev_252d_slope_v096_signal(ncfcommon, revenue, sharesbas):
    raw = _safe_div(ncfcommon, revenue)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank252_504d_slope_v097_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank21_252d_slope_v098_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_gvb_504d_slope_v099_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 504) - revenue.pct_change(periods=504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_gvbratio_252d_slope_v100_signal(sharesbas, revenue):
    result = _safe_div(_f17_dilution(sharesbas, 252), revenue.pct_change(periods=252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_rps_504d_slope_v101_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_eps_504d_slope_v102_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilir_252d_slope_v103_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = _safe_div(g, _std(g, 504))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilir_21d_slope_v104_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_smdil21_252d_slope_v105_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_smdil63_126d_slope_v106_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_ewmdil_252d_slope_v107_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.ewm(span=252, min_periods=63).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_ewmdil_42d_slope_v108_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=42, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dildisp_504d_slope_v109_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dildisp63_252d_slope_v110_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 63), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_anndil_252d_slope_v111_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252) * (252.0 / 252.0)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_anndil_189d_slope_v112_signal(sharesbas):
    result = _f17_dilution(sharesbas, 189) * (252.0 / 189.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_anndil_42d_slope_v113_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42) * (252.0 / 42.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_basgap_504d_slope_v114_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 504) - _f17_dilution(shareswa, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_basgap_63d_slope_v115_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 63) - _f17_dilution(shareswa, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_baswa_126d_slope_v116_signal(sharesbas, shareswa):
    ratio = _safe_div(sharesbas, shareswa)
    result = np.log(ratio / ratio.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_watrend_504d_slope_v117_signal(shareswa):
    result = _f17_sharetrend(shareswa, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadilz_504d_slope_v118_signal(shareswa):
    result = _f17_dilz(shareswa, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_wadilz_126d_slope_v119_signal(shareswa):
    result = _f17_dilz(shareswa, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dileqs_504d_slope_v120_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=504)
    result = _f17_dilution(sharesbas, 504) - eqg
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dileqs_63d_slope_v121_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=63)
    result = _f17_dilution(sharesbas, 63) - eqg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issintz_126d_slope_v122_signal(ncfcommon, sharesbas):
    raw = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _z(raw, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcz_126d_slope_v123_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _z(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trratio_126_504d_slope_v124_signal(sharesbas):
    result = _safe_div(_f17_sharetrend(sharesbas, 126), _f17_sharetrend(sharesbas, 504).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilsurp_252d_slope_v125_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = g - _mean(g, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilsurp_21d_slope_v126_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g - _mean(g, 63)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_bvgap_126d_slope_v127_signal(sharesbas, equity):
    eqps = _safe_div(equity, sharesbas)
    eqpsg = eqps.pct_change(periods=126)
    result = _f17_dilution(sharesbas, 126) - eqpsg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_baddil_252d_slope_v128_signal(sharesbas, revenue):
    rps = _safe_div(revenue, sharesbas)
    rpsg = rps.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) * (1.0 - rpsg.clip(-1, 1))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilxsbc_252d_slope_v129_signal(sharesbas, sbcomp, equity):
    sbc = _safe_div(sbcomp, equity)
    result = _f17_dilution(sharesbas, 252) * _z(sbc, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilxiss_126d_slope_v130_signal(sharesbas, ncfcommon):
    iss = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _f17_dilution(sharesbas, 126) * _z(iss, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_lvlz_252d_slope_v131_signal(sharesbas):
    result = _z(sharesbas, 252) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_lvlz_504d_slope_v132_signal(sharesbas):
    result = _z(sharesbas, 504) + _f17_dilution(sharesbas, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_elev_252d_slope_v133_signal(sharesbas):
    result = _safe_div(sharesbas, _mean(sharesbas, 252)) - 1.0 + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_elev_126d_slope_v134_signal(sharesbas):
    result = _safe_div(sharesbas, _mean(sharesbas, 126)) - 1.0 + _f17_dilution(sharesbas, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilacc_63d_slope_v135_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g - g.shift(63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilacc_126d_slope_v136_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g - g.shift(126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilacc_21d_slope_v137_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g - g.shift(21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_watrratio_84_252d_slope_v138_signal(shareswa):
    result = _safe_div(_f17_sharetrend(shareswa, 84), _f17_sharetrend(shareswa, 252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_cashpaper_252d_slope_v139_signal(ncfcommon, sbcomp, sharesbas):
    cash = _f17_issintensity(ncfcommon, sharesbas, 126)
    paper = _safe_div(sbcomp, sharesbas)
    result = _z(cash, 252) - _z(paper, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_zxcum_252d_slope_v140_signal(sharesbas):
    cum = np.log(sharesbas / sharesbas.shift(252))
    result = _f17_dilz(sharesbas, 252) * cum.abs()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_relent_252d_slope_v141_signal(sharesbas):
    short = np.log(sharesbas / sharesbas.shift(63)) * 4.0
    long = np.log(sharesbas / sharesbas.shift(252))
    result = short - long + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_qualdil_252d_slope_v142_signal(sharesbas, revenue, equity):
    rpsg = _safe_div(revenue, sharesbas).pct_change(periods=252)
    epsg = _safe_div(equity, sharesbas).pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - 0.5 * (rpsg + epsg)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcgrow_252d_slope_v143_signal(sbcomp, sharesbas):
    result = np.log(sbcomp / sbcomp.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_issgrow_252d_slope_v144_signal(ncfcommon, sharesbas):
    result = np.log(ncfcommon.abs() + 1.0) - np.log(ncfcommon.abs().shift(252) + 1.0) + _f17_dilution(sharesbas, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilz_84d_slope_v145_signal(sharesbas):
    result = _f17_dilz(sharesbas, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_trend_42d_slope_v146_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilrank_378d_slope_v147_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(378, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_sbcz_504d_slope_v148_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _z(raw, 504) + _f17_dilution(sharesbas, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_dilir_84d_slope_v149_signal(sharesbas):
    g = _f17_dilution(sharesbas, 84)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17sd_f17_share_dilution_machine_blendmulti_slope_v150_signal(sharesbas):
    result = (_f17_dilution(sharesbas, 63) + _f17_dilution(sharesbas, 126)
              + _f17_dilution(sharesbas, 252) + _f17_dilution(sharesbas, 504)) / 4.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f17sd_f17_share_dilution_machine_dil_63d_slope_v001_signal,    f17sd_f17_share_dilution_machine_dil_126d_slope_v002_signal,    f17sd_f17_share_dilution_machine_dil_252d_slope_v003_signal,    f17sd_f17_share_dilution_machine_dil_504d_slope_v004_signal,    f17sd_f17_share_dilution_machine_dil_21d_slope_v005_signal,    f17sd_f17_share_dilution_machine_dil_42d_slope_v006_signal,    f17sd_f17_share_dilution_machine_dil_84d_slope_v007_signal,    f17sd_f17_share_dilution_machine_dil_189d_slope_v008_signal,    f17sd_f17_share_dilution_machine_wadil_63d_slope_v009_signal,    f17sd_f17_share_dilution_machine_wadil_126d_slope_v010_signal,    f17sd_f17_share_dilution_machine_wadil_252d_slope_v011_signal,    f17sd_f17_share_dilution_machine_wadil_504d_slope_v012_signal,    f17sd_f17_share_dilution_machine_wadil_21d_slope_v013_signal,    f17sd_f17_share_dilution_machine_accel_63_126d_slope_v014_signal,    f17sd_f17_share_dilution_machine_accel_126_252d_slope_v015_signal,    f17sd_f17_share_dilution_machine_accel_21_63d_slope_v016_signal,    f17sd_f17_share_dilution_machine_accel_252_504d_slope_v017_signal,    f17sd_f17_share_dilution_machine_dilz_126d_slope_v018_signal,    f17sd_f17_share_dilution_machine_dilz_252d_slope_v019_signal,    f17sd_f17_share_dilution_machine_dilz_504d_slope_v020_signal,    f17sd_f17_share_dilution_machine_dilz_63d_slope_v021_signal,    f17sd_f17_share_dilution_machine_trend_63d_slope_v022_signal,    f17sd_f17_share_dilution_machine_trend_126d_slope_v023_signal,    f17sd_f17_share_dilution_machine_trend_252d_slope_v024_signal,    f17sd_f17_share_dilution_machine_trend_504d_slope_v025_signal,    f17sd_f17_share_dilution_machine_trend_21d_slope_v026_signal,    f17sd_f17_share_dilution_machine_cumdil_252d_slope_v027_signal,    f17sd_f17_share_dilution_machine_cumdil_504d_slope_v028_signal,    f17sd_f17_share_dilution_machine_cumdil_126d_slope_v029_signal,    f17sd_f17_share_dilution_machine_sbcdil_63d_slope_v030_signal,    f17sd_f17_share_dilution_machine_sbcdil_126d_slope_v031_signal,    f17sd_f17_share_dilution_machine_sbcdil_252d_slope_v032_signal,    f17sd_f17_share_dilution_machine_sbcps_126d_slope_v033_signal,    f17sd_f17_share_dilution_machine_sbcps_252d_slope_v034_signal,    f17sd_f17_share_dilution_machine_issint_63d_slope_v035_signal,    f17sd_f17_share_dilution_machine_issint_126d_slope_v036_signal,    f17sd_f17_share_dilution_machine_issint_252d_slope_v037_signal,    f17sd_f17_share_dilution_machine_isseq_126d_slope_v038_signal,    f17sd_f17_share_dilution_machine_isseq_252d_slope_v039_signal,    f17sd_f17_share_dilution_machine_dilrank_252d_slope_v040_signal,    f17sd_f17_share_dilution_machine_dilrank_504d_slope_v041_signal,    f17sd_f17_share_dilution_machine_dilrank126_504d_slope_v042_signal,    f17sd_f17_share_dilution_machine_gvb_252d_slope_v043_signal,    f17sd_f17_share_dilution_machine_gvb_126d_slope_v044_signal,    f17sd_f17_share_dilution_machine_gvb_63d_slope_v045_signal,    f17sd_f17_share_dilution_machine_rps_252d_slope_v046_signal,    f17sd_f17_share_dilution_machine_rps_126d_slope_v047_signal,    f17sd_f17_share_dilution_machine_eps_252d_slope_v048_signal,    f17sd_f17_share_dilution_machine_eps_126d_slope_v049_signal,    f17sd_f17_share_dilution_machine_dilir_63d_slope_v050_signal,    f17sd_f17_share_dilution_machine_dilir_126d_slope_v051_signal,    f17sd_f17_share_dilution_machine_smdil_63d_slope_v052_signal,    f17sd_f17_share_dilution_machine_smdil_126d_slope_v053_signal,    f17sd_f17_share_dilution_machine_smdil_252d_slope_v054_signal,    f17sd_f17_share_dilution_machine_ewmdil_63d_slope_v055_signal,    f17sd_f17_share_dilution_machine_ewmdil_126d_slope_v056_signal,    f17sd_f17_share_dilution_machine_dildisp_126d_slope_v057_signal,    f17sd_f17_share_dilution_machine_dildisp_252d_slope_v058_signal,    f17sd_f17_share_dilution_machine_anndil_63d_slope_v059_signal,    f17sd_f17_share_dilution_machine_anndil_126d_slope_v060_signal,    f17sd_f17_share_dilution_machine_basgap_252d_slope_v061_signal,    f17sd_f17_share_dilution_machine_basgap_126d_slope_v062_signal,    f17sd_f17_share_dilution_machine_baswa_252d_slope_v063_signal,    f17sd_f17_share_dilution_machine_watrend_252d_slope_v064_signal,    f17sd_f17_share_dilution_machine_watrend_126d_slope_v065_signal,    f17sd_f17_share_dilution_machine_wadilz_252d_slope_v066_signal,    f17sd_f17_share_dilution_machine_dileqs_252d_slope_v067_signal,    f17sd_f17_share_dilution_machine_dileqs_126d_slope_v068_signal,    f17sd_f17_share_dilution_machine_issintz_252d_slope_v069_signal,    f17sd_f17_share_dilution_machine_sbcz_252d_slope_v070_signal,    f17sd_f17_share_dilution_machine_blend_252d_slope_v071_signal,    f17sd_f17_share_dilution_machine_trratio_63_252d_slope_v072_signal,    f17sd_f17_share_dilution_machine_dilsurp_126d_slope_v073_signal,    f17sd_f17_share_dilution_machine_dilsurp_63d_slope_v074_signal,    f17sd_f17_share_dilution_machine_bvgap_252d_slope_v075_signal,    f17sd_f17_share_dilution_machine_dil_315d_slope_v076_signal,    f17sd_f17_share_dilution_machine_dil_378d_slope_v077_signal,    f17sd_f17_share_dilution_machine_dil_10d_slope_v078_signal,    f17sd_f17_share_dilution_machine_wadil_189d_slope_v079_signal,    f17sd_f17_share_dilution_machine_wadil_84d_slope_v080_signal,    f17sd_f17_share_dilution_machine_cumdil_189d_slope_v081_signal,    f17sd_f17_share_dilution_machine_cumdil_378d_slope_v082_signal,    f17sd_f17_share_dilution_machine_accel_84_189d_slope_v083_signal,    f17sd_f17_share_dilution_machine_accel_42_126d_slope_v084_signal,    f17sd_f17_share_dilution_machine_dilz_189d_slope_v085_signal,    f17sd_f17_share_dilution_machine_dilz_315d_slope_v086_signal,    f17sd_f17_share_dilution_machine_trend_189d_slope_v087_signal,    f17sd_f17_share_dilution_machine_trend_315d_slope_v088_signal,    f17sd_f17_share_dilution_machine_trend_84d_slope_v089_signal,    f17sd_f17_share_dilution_machine_sbcdil_189d_slope_v090_signal,    f17sd_f17_share_dilution_machine_sbcps_63d_slope_v091_signal,    f17sd_f17_share_dilution_machine_sbcrev_252d_slope_v092_signal,    f17sd_f17_share_dilution_machine_sbcrevtr_252d_slope_v093_signal,    f17sd_f17_share_dilution_machine_issint_189d_slope_v094_signal,    f17sd_f17_share_dilution_machine_issint_42d_slope_v095_signal,    f17sd_f17_share_dilution_machine_issrev_252d_slope_v096_signal,    f17sd_f17_share_dilution_machine_dilrank252_504d_slope_v097_signal,    f17sd_f17_share_dilution_machine_dilrank21_252d_slope_v098_signal,    f17sd_f17_share_dilution_machine_gvb_504d_slope_v099_signal,    f17sd_f17_share_dilution_machine_gvbratio_252d_slope_v100_signal,    f17sd_f17_share_dilution_machine_rps_504d_slope_v101_signal,    f17sd_f17_share_dilution_machine_eps_504d_slope_v102_signal,    f17sd_f17_share_dilution_machine_dilir_252d_slope_v103_signal,    f17sd_f17_share_dilution_machine_dilir_21d_slope_v104_signal,    f17sd_f17_share_dilution_machine_smdil21_252d_slope_v105_signal,    f17sd_f17_share_dilution_machine_smdil63_126d_slope_v106_signal,    f17sd_f17_share_dilution_machine_ewmdil_252d_slope_v107_signal,    f17sd_f17_share_dilution_machine_ewmdil_42d_slope_v108_signal,    f17sd_f17_share_dilution_machine_dildisp_504d_slope_v109_signal,    f17sd_f17_share_dilution_machine_dildisp63_252d_slope_v110_signal,    f17sd_f17_share_dilution_machine_anndil_252d_slope_v111_signal,    f17sd_f17_share_dilution_machine_anndil_189d_slope_v112_signal,    f17sd_f17_share_dilution_machine_anndil_42d_slope_v113_signal,    f17sd_f17_share_dilution_machine_basgap_504d_slope_v114_signal,    f17sd_f17_share_dilution_machine_basgap_63d_slope_v115_signal,    f17sd_f17_share_dilution_machine_baswa_126d_slope_v116_signal,    f17sd_f17_share_dilution_machine_watrend_504d_slope_v117_signal,    f17sd_f17_share_dilution_machine_wadilz_504d_slope_v118_signal,    f17sd_f17_share_dilution_machine_wadilz_126d_slope_v119_signal,    f17sd_f17_share_dilution_machine_dileqs_504d_slope_v120_signal,    f17sd_f17_share_dilution_machine_dileqs_63d_slope_v121_signal,    f17sd_f17_share_dilution_machine_issintz_126d_slope_v122_signal,    f17sd_f17_share_dilution_machine_sbcz_126d_slope_v123_signal,    f17sd_f17_share_dilution_machine_trratio_126_504d_slope_v124_signal,    f17sd_f17_share_dilution_machine_dilsurp_252d_slope_v125_signal,    f17sd_f17_share_dilution_machine_dilsurp_21d_slope_v126_signal,    f17sd_f17_share_dilution_machine_bvgap_126d_slope_v127_signal,    f17sd_f17_share_dilution_machine_baddil_252d_slope_v128_signal,    f17sd_f17_share_dilution_machine_dilxsbc_252d_slope_v129_signal,    f17sd_f17_share_dilution_machine_dilxiss_126d_slope_v130_signal,    f17sd_f17_share_dilution_machine_lvlz_252d_slope_v131_signal,    f17sd_f17_share_dilution_machine_lvlz_504d_slope_v132_signal,    f17sd_f17_share_dilution_machine_elev_252d_slope_v133_signal,    f17sd_f17_share_dilution_machine_elev_126d_slope_v134_signal,    f17sd_f17_share_dilution_machine_dilacc_63d_slope_v135_signal,    f17sd_f17_share_dilution_machine_dilacc_126d_slope_v136_signal,    f17sd_f17_share_dilution_machine_dilacc_21d_slope_v137_signal,    f17sd_f17_share_dilution_machine_watrratio_84_252d_slope_v138_signal,    f17sd_f17_share_dilution_machine_cashpaper_252d_slope_v139_signal,    f17sd_f17_share_dilution_machine_zxcum_252d_slope_v140_signal,    f17sd_f17_share_dilution_machine_relent_252d_slope_v141_signal,    f17sd_f17_share_dilution_machine_qualdil_252d_slope_v142_signal,    f17sd_f17_share_dilution_machine_sbcgrow_252d_slope_v143_signal,    f17sd_f17_share_dilution_machine_issgrow_252d_slope_v144_signal,    f17sd_f17_share_dilution_machine_dilz_84d_slope_v145_signal,    f17sd_f17_share_dilution_machine_trend_42d_slope_v146_signal,    f17sd_f17_share_dilution_machine_dilrank_378d_slope_v147_signal,    f17sd_f17_share_dilution_machine_sbcz_504d_slope_v148_signal,    f17sd_f17_share_dilution_machine_dilir_84d_slope_v149_signal,    f17sd_f17_share_dilution_machine_blendmulti_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_SHARE_DILUTION_MACHINE_REGISTRY_SLOPE = REGISTRY

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
    domain_primitives = ('_f17_dilution', '_f17_sharetrend', '_f17_dilz', '_f17_issintensity')
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
    print("OK f17_share_dilution_machine_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
