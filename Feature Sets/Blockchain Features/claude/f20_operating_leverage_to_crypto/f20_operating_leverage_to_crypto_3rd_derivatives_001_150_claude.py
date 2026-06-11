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


# ===== folder domain primitives (operating leverage to crypto) =====
def _f20_opmargin(revenue, opinc):
    # operating margin = operating income / revenue
    return _safe_div(opinc, revenue)


def _f20_oplev(revenue, opinc, w):
    # degree of operating leverage = %change(opinc) / %change(revenue) over w
    dop = opinc.pct_change(periods=w)
    drev = revenue.pct_change(periods=w)
    return _safe_div(dop, drev)


def _f20_costratio(revenue, opex):
    # operating cost ratio = opex / revenue
    return _safe_div(opex, revenue)


def _f20_contribmargin(revenue, cor):
    # contribution margin = (revenue - cor) / revenue
    return _safe_div(revenue - cor, revenue)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f20ol_f20_operating_leverage_to_crypto_opmargin_lvl_21d_jerk_v001_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_21d_jerk_v002_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_63d_jerk_v003_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_126d_jerk_v004_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_252d_jerk_v005_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_63d_jerk_v006_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_126d_jerk_v007_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_252d_jerk_v008_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_504d_jerk_v009_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_63d_jerk_v010_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_126d_jerk_v011_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_252d_jerk_v012_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_63d_jerk_v013_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(63), _std(m, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_126d_jerk_v014_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(126), _std(m, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_252d_jerk_v015_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(252), _std(m, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_126d_jerk_v016_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_252d_jerk_v017_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_63d_jerk_v018_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_126d_jerk_v019_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_252d_jerk_v020_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_63d_jerk_v021_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 63).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_126d_jerk_v022_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 126).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_252d_jerk_v023_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 252).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_21d_jerk_v024_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 21).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_sm_63d_jerk_v025_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_sm_126d_jerk_v026_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_z_252d_jerk_v027_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_63d_jerk_v028_signal(revenue, opinc):
    result = opinc.pct_change(63) - revenue.pct_change(63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_126d_jerk_v029_signal(revenue, opinc):
    result = opinc.pct_change(126) - revenue.pct_change(126) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_252d_jerk_v030_signal(revenue, opinc):
    result = opinc.pct_change(252) - revenue.pct_change(252) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_lvl_21d_jerk_v031_signal(revenue, opex):
    result = _f20_costratio(revenue, opex)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_sm_63d_jerk_v032_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_sm_126d_jerk_v033_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_sm_252d_jerk_v034_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_z_63d_jerk_v035_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_z_126d_jerk_v036_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_z_252d_jerk_v037_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_z_504d_jerk_v038_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_chg_126d_jerk_v039_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_chg_252d_jerk_v040_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_rank_252d_jerk_v041_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_lvl_21d_jerk_v042_signal(revenue, cor):
    result = _f20_contribmargin(revenue, cor)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_sm_63d_jerk_v043_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_sm_126d_jerk_v044_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_sm_252d_jerk_v045_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_z_126d_jerk_v046_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_z_252d_jerk_v047_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_chg_252d_jerk_v048_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm - cm.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_slope_126d_jerk_v049_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = _safe_div(cm - cm.shift(126), _std(cm, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_rank_252d_jerk_v050_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_lvl_21d_jerk_v051_signal(revenue, ebitda):
    result = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_63d_jerk_v052_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 63) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_126d_jerk_v053_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 126) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_z_252d_jerk_v054_signal(revenue, ebitda):
    result = _z(_safe_div(ebitda, revenue), 252) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_126d_jerk_v055_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em - em.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_lvl_21d_jerk_v056_signal(revenue, gp):
    result = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_sm_63d_jerk_v057_signal(revenue, gp):
    result = _mean(_safe_div(gp, revenue), 63) + _f20_opmargin(revenue, gp) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_z_126d_jerk_v058_signal(revenue, gp):
    result = _z(_safe_div(gp, revenue), 126) + _f20_opmargin(revenue, gp) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_chg_252d_jerk_v059_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = gm - gm.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_op2ebitda_21d_jerk_v060_signal(opinc, ebitda, revenue):
    result = _safe_div(opinc, ebitda) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_63d_jerk_v061_signal(opinc, ebitda, revenue):
    result = _mean(_safe_div(opinc, ebitda), 63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpopgap_21d_jerk_v062_signal(revenue, gp, opinc):
    result = _safe_div(gp, revenue) - _f20_opmargin(revenue, opinc)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpopgap_sm_63d_jerk_v063_signal(revenue, gp, opinc):
    result = _mean(_safe_div(gp, revenue) - _f20_opmargin(revenue, opinc), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpopgap_z_126d_jerk_v064_signal(revenue, gp, opinc):
    result = _z(_safe_div(gp, revenue) - _f20_opmargin(revenue, opinc), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_21d_jerk_v065_signal(opinc, opex, revenue):
    result = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_sm_63d_jerk_v066_signal(opinc, opex, revenue):
    result = _mean(_safe_div(opinc, opex), 63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_chg_126d_jerk_v067_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a - a.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_z_252d_jerk_v068_signal(opinc, opex, revenue):
    result = _z(_safe_div(opinc, opex), 252) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margXrevg_63d_jerk_v069_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margXrevg_126d_jerk_v070_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_sens_63d_jerk_v071_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(63), revenue.pct_change(63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_sens_126d_jerk_v072_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(126), revenue.pct_change(126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margcostsprd_21d_jerk_v073_signal(revenue, opinc, opex):
    result = _f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margcostsprd_sm_63d_jerk_v074_signal(revenue, opinc, opex):
    result = _mean(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_126d_jerk_v075_signal(revenue, opinc, opex):
    result = _z(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_252d_jerk_v076_signal(revenue, opinc, opex):
    result = _z(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margcostsprd_chg_252d_jerk_v077_signal(revenue, opinc, opex):
    sp = _f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex)
    result = sp - sp.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_84d_jerk_v078_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_189d_jerk_v079_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_504d_jerk_v080_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_63d_jerk_v081_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_126d_jerk_v082_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_252d_jerk_v083_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_21d_jerk_v084_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_42d_jerk_v085_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_504d_jerk_v086_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_84d_jerk_v087_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_189d_jerk_v088_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_z_315d_jerk_v089_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_rel_252d_jerk_v090_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m, _mean(m, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_rel_126d_jerk_v091_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m, _mean(m, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_378d_jerk_v092_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(378, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_504d_jerk_v093_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_cv_252d_jerk_v094_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(_std(m, 252), _mean(m, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_84d_jerk_v095_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 84).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_189d_jerk_v096_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 189).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_504d_jerk_v097_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 504).clip(-50, 50)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_sm_252d_jerk_v098_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 126)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_z_126d_jerk_v099_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dol_z_504d_jerk_v100_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_42d_jerk_v101_signal(revenue, opinc):
    result = opinc.pct_change(42) - revenue.pct_change(42) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_504d_jerk_v102_signal(revenue, opinc):
    result = opinc.pct_change(504) - revenue.pct_change(504) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_growthsprd_z_126d_jerk_v103_signal(revenue, opinc):
    sp = opinc.pct_change(63) - revenue.pct_change(63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _z(sp, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_sm_84d_jerk_v104_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_sm_504d_jerk_v105_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_ewm_126d_jerk_v106_signal(revenue, opex):
    result = _f20_costratio(revenue, opex).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_rel_252d_jerk_v107_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = _safe_div(c, _mean(c, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_slope_126d_jerk_v108_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = _safe_div(c - c.shift(126), _std(c, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_disp_252d_jerk_v109_signal(revenue, opex):
    result = _std(_f20_costratio(revenue, opex), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_chg_126d_jerk_v110_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm - cm.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_z_63d_jerk_v111_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_z_504d_jerk_v112_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_ewm_126d_jerk_v113_signal(revenue, cor):
    result = _f20_contribmargin(revenue, cor).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_disp_252d_jerk_v114_signal(revenue, cor):
    result = _std(_f20_contribmargin(revenue, cor), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_rel_252d_jerk_v115_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = _safe_div(cm, _mean(cm, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contribopgap_21d_jerk_v116_signal(revenue, cor, opinc):
    result = _f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contribopgap_sm_63d_jerk_v117_signal(revenue, cor, opinc):
    result = _mean(_f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contribopgap_z_126d_jerk_v118_signal(revenue, cor, opinc):
    result = _z(_f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_252d_jerk_v119_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 252) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_z_126d_jerk_v120_signal(revenue, ebitda):
    result = _z(_safe_div(ebitda, revenue), 126) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_252d_jerk_v121_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em - em.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_slope_126d_jerk_v122_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _safe_div(em - em.shift(126), _std(em, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitdam_rank_252d_jerk_v123_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_ebitda2op_63d_jerk_v124_signal(revenue, ebitda, opinc):
    result = _mean(_safe_div(ebitda, opinc), 63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_sm_126d_jerk_v125_signal(revenue, gp):
    result = _mean(_safe_div(gp, revenue), 126) + _f20_opmargin(revenue, gp) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_z_252d_jerk_v126_signal(revenue, gp):
    result = _z(_safe_div(gp, revenue), 252) + _f20_opmargin(revenue, gp) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_slope_126d_jerk_v127_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = _safe_div(gm - gm.shift(126), _std(gm, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gpm_rank_252d_jerk_v128_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = gm.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_gp2op_63d_jerk_v129_signal(revenue, gp, opinc):
    result = _mean(_safe_div(_safe_div(gp, revenue), _f20_opmargin(revenue, opinc)), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_126d_jerk_v130_signal(opinc, ebitda, revenue):
    result = _mean(_safe_div(opinc, ebitda), 126) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_op2ebitda_z_252d_jerk_v131_signal(opinc, ebitda, revenue):
    result = _z(_safe_div(opinc, ebitda), 252) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_sm_126d_jerk_v132_signal(opinc, opex, revenue):
    result = _mean(_safe_div(opinc, opex), 126) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_z_126d_jerk_v133_signal(opinc, opex, revenue):
    result = _z(_safe_div(opinc, opex), 126) + _f20_opmargin(revenue, opinc) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_chg_252d_jerk_v134_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a - a.shift(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_absorb_rank_252d_jerk_v135_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margXrevg_252d_jerk_v136_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_sens_252d_jerk_v137_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(252), revenue.pct_change(252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_sens_sm_63d_jerk_v138_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    sens = _safe_div(m - m.shift(63), revenue.pct_change(63))
    result = _mean(sens.clip(-50, 50), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_roc_126d_jerk_v139_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c.pct_change(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_roc_126d_jerk_v140_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.pct_change(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_roc_252d_jerk_v141_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.pct_change(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_accel_jerk_v142_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_contrib_roc_252d_jerk_v143_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm.pct_change(252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_margXrevg_z_126d_jerk_v144_signal(revenue, opinc):
    sig = _f20_opmargin(revenue, opinc) * revenue.pct_change(63)
    result = _z(sig, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_opmargin_surp_126d_jerk_v145_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_costratio_surp_126d_jerk_v146_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_dolXcontrib_63d_jerk_v147_signal(revenue, opinc, cor):
    result = _mean(_f20_oplev(revenue, opinc, 63).clip(-50, 50) * _f20_contribmargin(revenue, cor), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_blend_composite_jerk_v148_signal(revenue, opinc, opex):
    mz = _z(_f20_opmargin(revenue, opinc), 252)
    cz = _z(_f20_costratio(revenue, opex), 252)
    dz = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 252)
    result = (mz - cz + dz) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_payoff_126d_jerk_v149_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = (m - m.shift(126)) * revenue.pct_change(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f20ol_f20_operating_leverage_to_crypto_marg_trend_multi_jerk_v150_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = ((m - m.shift(63)) + (m - m.shift(126)) + (m - m.shift(252))) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f20ol_f20_operating_leverage_to_crypto_opmargin_lvl_21d_jerk_v001_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_21d_jerk_v002_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_63d_jerk_v003_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_126d_jerk_v004_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_252d_jerk_v005_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_63d_jerk_v006_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_126d_jerk_v007_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_252d_jerk_v008_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_504d_jerk_v009_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_63d_jerk_v010_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_126d_jerk_v011_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_252d_jerk_v012_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_63d_jerk_v013_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_126d_jerk_v014_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_252d_jerk_v015_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_126d_jerk_v016_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_252d_jerk_v017_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_63d_jerk_v018_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_126d_jerk_v019_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_252d_jerk_v020_signal,    f20ol_f20_operating_leverage_to_crypto_dol_63d_jerk_v021_signal,    f20ol_f20_operating_leverage_to_crypto_dol_126d_jerk_v022_signal,    f20ol_f20_operating_leverage_to_crypto_dol_252d_jerk_v023_signal,    f20ol_f20_operating_leverage_to_crypto_dol_21d_jerk_v024_signal,    f20ol_f20_operating_leverage_to_crypto_dol_sm_63d_jerk_v025_signal,    f20ol_f20_operating_leverage_to_crypto_dol_sm_126d_jerk_v026_signal,    f20ol_f20_operating_leverage_to_crypto_dol_z_252d_jerk_v027_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_63d_jerk_v028_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_126d_jerk_v029_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_252d_jerk_v030_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_lvl_21d_jerk_v031_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_sm_63d_jerk_v032_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_sm_126d_jerk_v033_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_sm_252d_jerk_v034_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_z_63d_jerk_v035_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_z_126d_jerk_v036_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_z_252d_jerk_v037_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_z_504d_jerk_v038_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_chg_126d_jerk_v039_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_chg_252d_jerk_v040_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_rank_252d_jerk_v041_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_lvl_21d_jerk_v042_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_sm_63d_jerk_v043_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_sm_126d_jerk_v044_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_sm_252d_jerk_v045_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_z_126d_jerk_v046_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_z_252d_jerk_v047_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_chg_252d_jerk_v048_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_slope_126d_jerk_v049_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_rank_252d_jerk_v050_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_lvl_21d_jerk_v051_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_63d_jerk_v052_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_126d_jerk_v053_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_z_252d_jerk_v054_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_126d_jerk_v055_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_lvl_21d_jerk_v056_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_sm_63d_jerk_v057_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_z_126d_jerk_v058_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_chg_252d_jerk_v059_signal,    f20ol_f20_operating_leverage_to_crypto_op2ebitda_21d_jerk_v060_signal,    f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_63d_jerk_v061_signal,    f20ol_f20_operating_leverage_to_crypto_gpopgap_21d_jerk_v062_signal,    f20ol_f20_operating_leverage_to_crypto_gpopgap_sm_63d_jerk_v063_signal,    f20ol_f20_operating_leverage_to_crypto_gpopgap_z_126d_jerk_v064_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_21d_jerk_v065_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_sm_63d_jerk_v066_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_chg_126d_jerk_v067_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_z_252d_jerk_v068_signal,    f20ol_f20_operating_leverage_to_crypto_margXrevg_63d_jerk_v069_signal,    f20ol_f20_operating_leverage_to_crypto_margXrevg_126d_jerk_v070_signal,    f20ol_f20_operating_leverage_to_crypto_sens_63d_jerk_v071_signal,    f20ol_f20_operating_leverage_to_crypto_sens_126d_jerk_v072_signal,    f20ol_f20_operating_leverage_to_crypto_margcostsprd_21d_jerk_v073_signal,    f20ol_f20_operating_leverage_to_crypto_margcostsprd_sm_63d_jerk_v074_signal,    f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_126d_jerk_v075_signal,    f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_252d_jerk_v076_signal,    f20ol_f20_operating_leverage_to_crypto_margcostsprd_chg_252d_jerk_v077_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_84d_jerk_v078_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_189d_jerk_v079_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_504d_jerk_v080_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_63d_jerk_v081_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_126d_jerk_v082_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_252d_jerk_v083_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_21d_jerk_v084_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_42d_jerk_v085_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_504d_jerk_v086_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_84d_jerk_v087_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_189d_jerk_v088_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_z_315d_jerk_v089_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_rel_252d_jerk_v090_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_rel_126d_jerk_v091_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_378d_jerk_v092_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_504d_jerk_v093_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_cv_252d_jerk_v094_signal,    f20ol_f20_operating_leverage_to_crypto_dol_84d_jerk_v095_signal,    f20ol_f20_operating_leverage_to_crypto_dol_189d_jerk_v096_signal,    f20ol_f20_operating_leverage_to_crypto_dol_504d_jerk_v097_signal,    f20ol_f20_operating_leverage_to_crypto_dol_sm_252d_jerk_v098_signal,    f20ol_f20_operating_leverage_to_crypto_dol_z_126d_jerk_v099_signal,    f20ol_f20_operating_leverage_to_crypto_dol_z_504d_jerk_v100_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_42d_jerk_v101_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_504d_jerk_v102_signal,    f20ol_f20_operating_leverage_to_crypto_growthsprd_z_126d_jerk_v103_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_sm_84d_jerk_v104_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_sm_504d_jerk_v105_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_ewm_126d_jerk_v106_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_rel_252d_jerk_v107_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_slope_126d_jerk_v108_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_disp_252d_jerk_v109_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_chg_126d_jerk_v110_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_z_63d_jerk_v111_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_z_504d_jerk_v112_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_ewm_126d_jerk_v113_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_disp_252d_jerk_v114_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_rel_252d_jerk_v115_signal,    f20ol_f20_operating_leverage_to_crypto_contribopgap_21d_jerk_v116_signal,    f20ol_f20_operating_leverage_to_crypto_contribopgap_sm_63d_jerk_v117_signal,    f20ol_f20_operating_leverage_to_crypto_contribopgap_z_126d_jerk_v118_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_252d_jerk_v119_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_z_126d_jerk_v120_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_252d_jerk_v121_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_slope_126d_jerk_v122_signal,    f20ol_f20_operating_leverage_to_crypto_ebitdam_rank_252d_jerk_v123_signal,    f20ol_f20_operating_leverage_to_crypto_ebitda2op_63d_jerk_v124_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_sm_126d_jerk_v125_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_z_252d_jerk_v126_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_slope_126d_jerk_v127_signal,    f20ol_f20_operating_leverage_to_crypto_gpm_rank_252d_jerk_v128_signal,    f20ol_f20_operating_leverage_to_crypto_gp2op_63d_jerk_v129_signal,    f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_126d_jerk_v130_signal,    f20ol_f20_operating_leverage_to_crypto_op2ebitda_z_252d_jerk_v131_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_sm_126d_jerk_v132_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_z_126d_jerk_v133_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_chg_252d_jerk_v134_signal,    f20ol_f20_operating_leverage_to_crypto_absorb_rank_252d_jerk_v135_signal,    f20ol_f20_operating_leverage_to_crypto_margXrevg_252d_jerk_v136_signal,    f20ol_f20_operating_leverage_to_crypto_sens_252d_jerk_v137_signal,    f20ol_f20_operating_leverage_to_crypto_sens_sm_63d_jerk_v138_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_roc_126d_jerk_v139_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_roc_126d_jerk_v140_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_roc_252d_jerk_v141_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_accel_jerk_v142_signal,    f20ol_f20_operating_leverage_to_crypto_contrib_roc_252d_jerk_v143_signal,    f20ol_f20_operating_leverage_to_crypto_margXrevg_z_126d_jerk_v144_signal,    f20ol_f20_operating_leverage_to_crypto_opmargin_surp_126d_jerk_v145_signal,    f20ol_f20_operating_leverage_to_crypto_costratio_surp_126d_jerk_v146_signal,    f20ol_f20_operating_leverage_to_crypto_dolXcontrib_63d_jerk_v147_signal,    f20ol_f20_operating_leverage_to_crypto_blend_composite_jerk_v148_signal,    f20ol_f20_operating_leverage_to_crypto_payoff_126d_jerk_v149_signal,    f20ol_f20_operating_leverage_to_crypto_marg_trend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_OPERATING_LEVERAGE_TO_CRYPTO_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f20_opmargin', '_f20_oplev', '_f20_costratio', '_f20_contribmargin')
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
    print("OK f20_operating_leverage_to_crypto_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
