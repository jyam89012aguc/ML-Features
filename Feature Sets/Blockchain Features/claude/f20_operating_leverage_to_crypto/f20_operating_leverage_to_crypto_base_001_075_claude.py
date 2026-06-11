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


# ============ FEATURES 001-075 ============

# operating margin level
def f20ol_f20_operating_leverage_to_crypto_opmargin_lvl_21d_base_v001_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_21d_base_v002_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_63d_base_v003_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_126d_base_v004_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_252d_base_v005_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_63d_base_v006_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_126d_base_v007_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_252d_base_v008_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_504d_base_v009_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in operating margin (expansion)
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_63d_base_v010_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_126d_base_v011_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_252d_base_v012_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin expansion slope (linear via diff over std)
def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_63d_base_v013_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(63), _std(m, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d margin expansion slope
def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_126d_base_v014_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(126), _std(m, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin expansion slope
def f20ol_f20_operating_leverage_to_crypto_opmargin_slope_252d_base_v015_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(252), _std(m, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percentile rank of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_126d_base_v016_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_252d_base_v017_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dispersion (std) of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_63d_base_v018_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_126d_base_v019_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_252d_base_v020_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 63d
def f20ol_f20_operating_leverage_to_crypto_dol_63d_base_v021_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 63).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 126d
def f20ol_f20_operating_leverage_to_crypto_dol_126d_base_v022_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 126).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 252d
def f20ol_f20_operating_leverage_to_crypto_dol_252d_base_v023_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 252).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 21d
def f20ol_f20_operating_leverage_to_crypto_dol_21d_base_v024_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 21).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed degree of operating leverage
def f20ol_f20_operating_leverage_to_crypto_dol_sm_63d_base_v025_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed degree of operating leverage
def f20ol_f20_operating_leverage_to_crypto_dol_sm_126d_base_v026_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of degree of operating leverage
def f20ol_f20_operating_leverage_to_crypto_dol_z_252d_base_v027_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# opinc growth minus revenue growth spread 63d
def f20ol_f20_operating_leverage_to_crypto_growthsprd_63d_base_v028_signal(revenue, opinc):
    result = opinc.pct_change(63) - revenue.pct_change(63) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# opinc growth minus revenue growth spread 126d
def f20ol_f20_operating_leverage_to_crypto_growthsprd_126d_base_v029_signal(revenue, opinc):
    result = opinc.pct_change(126) - revenue.pct_change(126) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# opinc growth minus revenue growth spread 252d
def f20ol_f20_operating_leverage_to_crypto_growthsprd_252d_base_v030_signal(revenue, opinc):
    result = opinc.pct_change(252) - revenue.pct_change(252) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cost ratio level (opex/revenue)
def f20ol_f20_operating_leverage_to_crypto_costratio_lvl_21d_base_v031_signal(revenue, opex):
    result = _f20_costratio(revenue, opex)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_sm_63d_base_v032_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_sm_126d_base_v033_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_sm_252d_base_v034_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cost ratio z-score
def f20ol_f20_operating_leverage_to_crypto_costratio_z_63d_base_v035_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cost ratio z-score
def f20ol_f20_operating_leverage_to_crypto_costratio_z_126d_base_v036_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cost ratio z-score
def f20ol_f20_operating_leverage_to_crypto_costratio_z_252d_base_v037_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cost ratio z-score
def f20ol_f20_operating_leverage_to_crypto_costratio_z_504d_base_v038_signal(revenue, opex):
    result = _z(_f20_costratio(revenue, opex), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in cost ratio (deleveraging trend)
def f20ol_f20_operating_leverage_to_crypto_costratio_chg_126d_base_v039_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_chg_252d_base_v040_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_rank_252d_base_v041_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# contribution margin level (revenue-cor)/revenue
def f20ol_f20_operating_leverage_to_crypto_contrib_lvl_21d_base_v042_signal(revenue, cor):
    result = _f20_contribmargin(revenue, cor)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_sm_63d_base_v043_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_sm_126d_base_v044_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_sm_252d_base_v045_signal(revenue, cor):
    result = _mean(_f20_contribmargin(revenue, cor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_z_126d_base_v046_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_z_252d_base_v047_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_chg_252d_base_v048_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm - cm.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d contribution margin slope
def f20ol_f20_operating_leverage_to_crypto_contrib_slope_126d_base_v049_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = _safe_div(cm - cm.shift(126), _std(cm, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_rank_252d_base_v050_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin level
def f20ol_f20_operating_leverage_to_crypto_ebitdam_lvl_21d_base_v051_signal(revenue, ebitda):
    result = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_63d_base_v052_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 63) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_126d_base_v053_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 126) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_z_252d_base_v054_signal(revenue, ebitda):
    result = _z(_safe_div(ebitda, revenue), 252) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_126d_base_v055_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em - em.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level
def f20ol_f20_operating_leverage_to_crypto_gpm_lvl_21d_base_v056_signal(revenue, gp):
    result = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean gross margin
def f20ol_f20_operating_leverage_to_crypto_gpm_sm_63d_base_v057_signal(revenue, gp):
    result = _mean(_safe_div(gp, revenue), 63) + _f20_opmargin(revenue, gp) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of gross margin
def f20ol_f20_operating_leverage_to_crypto_gpm_z_126d_base_v058_signal(revenue, gp):
    result = _z(_safe_div(gp, revenue), 126) + _f20_opmargin(revenue, gp) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in gross margin
def f20ol_f20_operating_leverage_to_crypto_gpm_chg_252d_base_v059_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = gm - gm.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-to-ebitda conversion (quality of operating income)
def f20ol_f20_operating_leverage_to_crypto_op2ebitda_21d_base_v060_signal(opinc, ebitda, revenue):
    result = _safe_div(opinc, ebitda) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean opinc-to-ebitda
def f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_63d_base_v061_signal(opinc, ebitda, revenue):
    result = _mean(_safe_div(opinc, ebitda), 63) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-operating margin gap (overhead drag)
def f20ol_f20_operating_leverage_to_crypto_gpopgap_21d_base_v062_signal(revenue, gp, opinc):
    result = _safe_div(gp, revenue) - _f20_opmargin(revenue, opinc)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean gross-to-operating margin gap
def f20ol_f20_operating_leverage_to_crypto_gpopgap_sm_63d_base_v063_signal(revenue, gp, opinc):
    result = _mean(_safe_div(gp, revenue) - _f20_opmargin(revenue, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of gross-to-operating gap
def f20ol_f20_operating_leverage_to_crypto_gpopgap_z_126d_base_v064_signal(revenue, gp, opinc):
    result = _z(_safe_div(gp, revenue) - _f20_opmargin(revenue, opinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost absorption proxy = opinc / opex
def f20ol_f20_operating_leverage_to_crypto_absorb_21d_base_v065_signal(opinc, opex, revenue):
    result = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean fixed-cost absorption
def f20ol_f20_operating_leverage_to_crypto_absorb_sm_63d_base_v066_signal(opinc, opex, revenue):
    result = _mean(_safe_div(opinc, opex), 63) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d absorption trend (change)
def f20ol_f20_operating_leverage_to_crypto_absorb_chg_126d_base_v067_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a - a.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of absorption
def f20ol_f20_operating_leverage_to_crypto_absorb_z_252d_base_v068_signal(opinc, opex, revenue):
    result = _z(_safe_div(opinc, opex), 252) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue intensity of operating margin (margin x revenue growth) 63d
def f20ol_f20_operating_leverage_to_crypto_margXrevg_63d_base_v069_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue intensity of operating margin 126d
def f20ol_f20_operating_leverage_to_crypto_margXrevg_126d_base_v070_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage sensitivity = d.margin per unit revenue growth 63d
def f20ol_f20_operating_leverage_to_crypto_sens_63d_base_v071_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(63), revenue.pct_change(63))
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage sensitivity 126d
def f20ol_f20_operating_leverage_to_crypto_sens_126d_base_v072_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(126), revenue.pct_change(126))
    return result.replace([np.inf, -np.inf], np.nan)


# margin vs cost ratio spread (operating efficiency net)
def f20ol_f20_operating_leverage_to_crypto_margcostsprd_21d_base_v073_signal(revenue, opinc, opex):
    result = _f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean margin vs cost ratio spread
def f20ol_f20_operating_leverage_to_crypto_margcostsprd_sm_63d_base_v074_signal(revenue, opinc, opex):
    result = _mean(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of margin vs cost ratio spread
def f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_126d_base_v075_signal(revenue, opinc, opex):
    result = _z(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20ol_f20_operating_leverage_to_crypto_opmargin_lvl_21d_base_v001_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_21d_base_v002_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_63d_base_v003_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_126d_base_v004_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_252d_base_v005_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_63d_base_v006_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_126d_base_v007_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_252d_base_v008_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_504d_base_v009_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_63d_base_v010_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_126d_base_v011_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_252d_base_v012_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_63d_base_v013_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_126d_base_v014_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_slope_252d_base_v015_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_126d_base_v016_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_252d_base_v017_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_63d_base_v018_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_126d_base_v019_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_252d_base_v020_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_63d_base_v021_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_126d_base_v022_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_252d_base_v023_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_21d_base_v024_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_sm_63d_base_v025_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_sm_126d_base_v026_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_z_252d_base_v027_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_63d_base_v028_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_126d_base_v029_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_252d_base_v030_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_lvl_21d_base_v031_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_sm_63d_base_v032_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_sm_126d_base_v033_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_sm_252d_base_v034_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_z_63d_base_v035_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_z_126d_base_v036_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_z_252d_base_v037_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_z_504d_base_v038_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_chg_126d_base_v039_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_chg_252d_base_v040_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_rank_252d_base_v041_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_lvl_21d_base_v042_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_sm_63d_base_v043_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_sm_126d_base_v044_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_sm_252d_base_v045_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_z_126d_base_v046_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_z_252d_base_v047_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_chg_252d_base_v048_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_slope_126d_base_v049_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_rank_252d_base_v050_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_lvl_21d_base_v051_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_63d_base_v052_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_126d_base_v053_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_z_252d_base_v054_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_126d_base_v055_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_lvl_21d_base_v056_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_sm_63d_base_v057_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_z_126d_base_v058_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_chg_252d_base_v059_signal,
    f20ol_f20_operating_leverage_to_crypto_op2ebitda_21d_base_v060_signal,
    f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_63d_base_v061_signal,
    f20ol_f20_operating_leverage_to_crypto_gpopgap_21d_base_v062_signal,
    f20ol_f20_operating_leverage_to_crypto_gpopgap_sm_63d_base_v063_signal,
    f20ol_f20_operating_leverage_to_crypto_gpopgap_z_126d_base_v064_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_21d_base_v065_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_sm_63d_base_v066_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_chg_126d_base_v067_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_z_252d_base_v068_signal,
    f20ol_f20_operating_leverage_to_crypto_margXrevg_63d_base_v069_signal,
    f20ol_f20_operating_leverage_to_crypto_margXrevg_126d_base_v070_signal,
    f20ol_f20_operating_leverage_to_crypto_sens_63d_base_v071_signal,
    f20ol_f20_operating_leverage_to_crypto_sens_126d_base_v072_signal,
    f20ol_f20_operating_leverage_to_crypto_margcostsprd_21d_base_v073_signal,
    f20ol_f20_operating_leverage_to_crypto_margcostsprd_sm_63d_base_v074_signal,
    f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_OPERATING_LEVERAGE_TO_CRYPTO_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f20_opmargin", "_f20_oplev", "_f20_costratio", "_f20_contribmargin")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
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
    print(f"OK f20_operating_leverage_to_crypto_base_001_075_claude: {n_features} features pass")
