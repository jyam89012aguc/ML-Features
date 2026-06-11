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


def _slope(s, w):
    # ordinary-least-squares style slope via diff over w scaled by w (per-day trend)
    return s.diff(periods=w) / float(w)


# ===== folder domain primitives (dilution-adjusted per-share growth) =====
def _f25_ps(numer, shares):
    # per-share level: a fundamental flow/stock divided by share count
    return numer / shares.replace(0, np.nan)


def _f25_psgrowth(numer, shares, w):
    # per-share value pct change over w (dilution-adjusted growth)
    ps = numer / shares.replace(0, np.nan)
    return ps.pct_change(periods=w)


def _f25_fcfps(fcf, shares):
    # free-cash-flow per share
    return fcf / shares.replace(0, np.nan)


def _f25_bvps(equity, shares):
    # book value (equity) per share
    return equity / shares.replace(0, np.nan)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f25dg_f25_dilution_adjusted_growth_sps_level_0d_jerk_v001_signal(revenue, sharesbas):
    result = _f25_ps(revenue, sharesbas)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spswa_level_0d_jerk_v002_signal(revenue, shareswa):
    result = _f25_ps(revenue, shareswa)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfps_level_0d_jerk_v003_signal(fcf, sharesbas):
    result = _f25_fcfps(fcf, sharesbas)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpps_level_0d_jerk_v004_signal(gp, sharesbas):
    result = _f25_ps(gp, sharesbas)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvps_level_0d_jerk_v005_signal(equity, sharesbas):
    result = _f25_bvps(equity, sharesbas)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_63d_jerk_v006_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_126d_jerk_v007_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_252d_jerk_v008_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_504d_jerk_v009_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfpsg_126d_jerk_v010_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfpsg_252d_jerk_v011_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gppsg_126d_jerk_v012_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gppsg_252d_jerk_v013_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpsg_252d_jerk_v014_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_netcreate_252d_jerk_v015_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_netcreate_126d_jerk_v016_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfnetcreate_252d_jerk_v017_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_dilutiondrag_252d_jerk_v018_signal(revenue, sharesbas):
    rawg = revenue.pct_change(periods=252)
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    result = rawg - psg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zspsg_63d_jerk_v019_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zspsg_126d_jerk_v020_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zfcfpsg_126d_jerk_v021_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _z(ps.pct_change(periods=126), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsslope_126d_jerk_v022_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _slope(ps, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsslope_252d_jerk_v023_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _slope(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsnslope_126d_jerk_v024_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(_slope(ps, 126), _mean(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfnslope_252d_jerk_v025_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(_slope(ps, 252), _mean(ps.abs(), 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_logcompound_126d_jerk_v026_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_logcompound_252d_jerk_v027_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcflogcompound_252d_jerk_v028_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = np.log(_safe_div(ps.abs() + 1.0, ps.shift(252).abs() + 1.0))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgrank_63d_jerk_v029_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgrank_126d_jerk_v030_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_pslevrank_252d_jerk_v031_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = ps.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_84d_jerk_v032_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_189d_jerk_v033_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_315d_jerk_v034_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_378d_jerk_v035_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spswag_252d_jerk_v036_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpwag_252d_jerk_v037_signal(gp, shareswa):
    ps = _f25_ps(gp, shareswa)
    result = ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgsmooth_63d_jerk_v038_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgsmooth_126d_jerk_v039_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgaccel_63_126_jerk_v040_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 63) - _f25_psgrowth(revenue, sharesbas, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgaccel_126_252_jerk_v041_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 126) - _f25_psgrowth(revenue, sharesbas, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgaccel_126_252_jerk_v042_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=126) - ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_revgpspread_252d_jerk_v043_signal(revenue, gp, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    result = gg - rg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfrevspread_252d_jerk_v044_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    result = fg - rg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_pslevratio_252d_jerk_v045_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcflevratio_252d_jerk_v046_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvplevratio_252d_jerk_v047_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvplog_252d_jerk_v048_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsyield_0d_jerk_v049_signal(revenue, sharesbas, closeadj):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, closeadj)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfyield_0d_jerk_v050_signal(fcf, sharesbas, closeadj):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(ps, closeadj)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpyield_0d_jerk_v051_signal(equity, sharesbas, closeadj):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(ps, closeadj)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zspsg126w_63d_jerk_v052_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 63), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_znetcreate_252d_jerk_v053_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpnetcreate_252d_jerk_v054_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgqual_126d_jerk_v055_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgqual_252d_jerk_v056_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=252)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsslopez_252d_jerk_v057_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_lognetcompound_252d_jerk_v058_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    revlog = np.log(_safe_div(revenue, revenue.shift(252)))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = revlog - shlog + ps * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpnetcreate_252d_jerk_v059_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_42d_jerk_v060_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsg_21d_jerk_v061_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gppsg_63d_jerk_v062_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfpsg_63d_jerk_v063_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpsg_126d_jerk_v064_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psewm_63d_jerk_v065_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfewm_126d_jerk_v066_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    lr = np.log(_safe_div(ps.abs() + 1.0, ps.shift(1).abs() + 1.0))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgdisp_252d_jerk_v067_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = _std(g, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgdisp_126d_jerk_v068_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 21)
    result = _std(g, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsbvpspread_0d_jerk_v069_signal(revenue, equity, sharesbas):
    sps = _f25_ps(revenue, sharesbas)
    bvps = _f25_bvps(equity, sharesbas)
    result = _safe_div(sps, bvps)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfconv_0d_jerk_v070_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    result = _safe_div(fps, sps)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpmargin_0d_jerk_v071_signal(gp, revenue, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    result = _safe_div(gpps, sps)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgann_63d_jerk_v072_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(63))) * (252.0 / 63.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgann_504d_jerk_v073_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(504))) * (252.0 / 504.0)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_dualshare_252d_jerk_v074_signal(revenue, sharesbas, shareswa):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    wadil = shareswa.pct_change(periods=252)
    result = psg - wadil
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgblend_multi_jerk_v075_signal(revenue, sharesbas):
    result = (_f25_psgrowth(revenue, sharesbas, 63)
              + _f25_psgrowth(revenue, sharesbas, 126)
              + _f25_psgrowth(revenue, sharesbas, 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gppsg_504d_jerk_v076_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfpsg_504d_jerk_v077_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpsg_504d_jerk_v078_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spswag_21d_jerk_v079_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spswag_126d_jerk_v080_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zspsg_252d_jerk_v081_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zgppsg_126d_jerk_v082_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _z(ps.pct_change(periods=126), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zbvpsg_252d_jerk_v083_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _z(ps.pct_change(periods=252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpslope_252d_jerk_v084_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _slope(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpslope_252d_jerk_v085_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _slope(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpnslope_126d_jerk_v086_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(_slope(ps, 126), _mean(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpnslope_252d_jerk_v087_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(_slope(ps, 252), _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gplogcompound_252d_jerk_v088_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvplogcompound_126d_jerk_v089_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgrank_126d_jerk_v090_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgrank_252d_jerk_v091_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcflevrank_252d_jerk_v092_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_netcreate_504d_jerk_v093_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 504)
    shg = sharesbas.pct_change(periods=504)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_netcreate_63d_jerk_v094_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 63)
    shg = sharesbas.pct_change(periods=63)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfnetcreate_126d_jerk_v095_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpnetcreate_126d_jerk_v096_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfdilutiondrag_252d_jerk_v097_signal(fcf, sharesbas):
    rawg = fcf.pct_change(periods=252)
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    result = rawg - psg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpdilutiondrag_252d_jerk_v098_signal(gp, sharesbas):
    rawg = gp.pct_change(periods=252)
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    result = rawg - psg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgsmooth_126d_jerk_v099_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _mean(ps.pct_change(periods=126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgsmooth_126d_jerk_v100_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _mean(ps.pct_change(periods=126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgaccel_63_126_jerk_v101_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=63) - ps.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpgaccel_126_252_jerk_v102_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=126) - ps.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgaccel_21_63_jerk_v103_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 21) - _f25_psgrowth(revenue, sharesbas, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_revbvpspread_252d_jerk_v104_signal(revenue, equity, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    bvps = _f25_bvps(equity, sharesbas)
    bg = bvps.pct_change(periods=252)
    result = rg - bg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpfcfspread_252d_jerk_v105_signal(gp, fcf, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    result = gg - fg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gplevratio_252d_jerk_v106_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_pslevratio_126d_jerk_v107_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, _mean(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpyield_0d_jerk_v108_signal(gp, sharesbas, closeadj):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(ps, closeadj)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgpricespread_252d_jerk_v109_signal(revenue, sharesbas, closeadj):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    pricg = closeadj.pct_change(periods=252)
    result = psg - pricg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgqual_63d_jerk_v110_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgqual_126d_jerk_v111_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    g = ps.pct_change(periods=126)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpgqual_252d_jerk_v112_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    g = ps.pct_change(periods=252)
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpslopez_252d_jerk_v113_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfslopez_252d_jerk_v114_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gplognetcompound_252d_jerk_v115_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    gplog = np.log(_safe_div(gp, gp.shift(252)))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = gplog - shlog + ps * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcflognetcompound_252d_jerk_v116_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    fcflog = np.log(_safe_div(fcf.abs() + 1.0, fcf.shift(252).abs() + 1.0))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = fcflog - shlog + ps * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gppsg_84d_jerk_v117_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfpsg_189d_jerk_v118_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spswag_504d_jerk_v119_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpsg_189d_jerk_v120_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgann_126d_jerk_v121_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgann_252d_jerk_v122_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgann_252d_jerk_v123_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = np.log(_safe_div(ps.abs() + 1.0, ps.shift(252).abs() + 1.0))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgdisp_504d_jerk_v124_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = _std(g, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgdisp_252d_jerk_v125_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=63)
    result = _std(g, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psewm_126d_jerk_v126_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpewm_63d_jerk_v127_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpewm_252d_jerk_v128_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=252, min_periods=84).mean() * 252.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfconvchg_252d_jerk_v129_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    conv = _safe_div(fps, sps)
    result = conv.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpmarginchg_252d_jerk_v130_signal(gp, revenue, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    margin = _safe_div(gpps, sps)
    result = margin.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsbvpchg_252d_jerk_v131_signal(revenue, equity, sharesbas):
    sps = _f25_ps(revenue, sharesbas)
    bvps = _f25_bvps(equity, sharesbas)
    ratio = _safe_div(sps, bvps)
    result = ratio.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zfcflev_252d_jerk_v132_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _z(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zpslev_504d_jerk_v133_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _z(ps, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zbvplev_252d_jerk_v134_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _z(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zgpnetcreate_252d_jerk_v135_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_zfcfnetcreate_252d_jerk_v136_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpdualshare_252d_jerk_v137_signal(gp, sharesbas, shareswa):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    wadil = shareswa.pct_change(periods=252)
    result = psg - wadil
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_wadilution_126d_jerk_v138_signal(revenue, shareswa):
    psg = _f25_psgrowth(revenue, shareswa, 126)
    shg = shareswa.pct_change(periods=126)
    result = psg - shg
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_spsgsmooth_252d_jerk_v139_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 252), 63)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgrank_252d_jerk_v140_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpgrank_252d_jerk_v141_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgsurp_252d_jerk_v142_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 252)
    result = g - _mean(g, 126)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgsurp_126d_jerk_v143_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=126)
    result = g - _mean(g, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_psgratio_63_252_jerk_v144_signal(revenue, sharesbas):
    s = _f25_psgrowth(revenue, sharesbas, 63)
    l = _f25_psgrowth(revenue, sharesbas, 252)
    result = _safe_div(s, l.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_gpgratio_126_252_jerk_v145_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    s = ps.pct_change(periods=126)
    l = ps.pct_change(periods=252)
    result = _safe_div(s, l.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_pssmoothslope_252d_jerk_v146_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    sm = _mean(ps, 21)
    result = _safe_div(_slope(sm, 252), _mean(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_valuecomposite_252d_jerk_v147_signal(revenue, gp, fcf, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = (rg + gg + fg) / 3.0 - shg
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_fcfgblend_multi_jerk_v148_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = (ps.pct_change(periods=126)
              + ps.pct_change(periods=252)
              + ps.pct_change(periods=504)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_bvpgblend_multi_jerk_v149_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = (ps.pct_change(periods=126)
              + ps.pct_change(periods=252)
              + ps.pct_change(periods=504)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25dg_f25_dilution_adjusted_growth_netcreatez_504d_jerk_v150_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 504)
    shg = sharesbas.pct_change(periods=504)
    result = _z(psg - shg, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f25dg_f25_dilution_adjusted_growth_sps_level_0d_jerk_v001_signal,    f25dg_f25_dilution_adjusted_growth_spswa_level_0d_jerk_v002_signal,    f25dg_f25_dilution_adjusted_growth_fcfps_level_0d_jerk_v003_signal,    f25dg_f25_dilution_adjusted_growth_gpps_level_0d_jerk_v004_signal,    f25dg_f25_dilution_adjusted_growth_bvps_level_0d_jerk_v005_signal,    f25dg_f25_dilution_adjusted_growth_spsg_63d_jerk_v006_signal,    f25dg_f25_dilution_adjusted_growth_spsg_126d_jerk_v007_signal,    f25dg_f25_dilution_adjusted_growth_spsg_252d_jerk_v008_signal,    f25dg_f25_dilution_adjusted_growth_spsg_504d_jerk_v009_signal,    f25dg_f25_dilution_adjusted_growth_fcfpsg_126d_jerk_v010_signal,    f25dg_f25_dilution_adjusted_growth_fcfpsg_252d_jerk_v011_signal,    f25dg_f25_dilution_adjusted_growth_gppsg_126d_jerk_v012_signal,    f25dg_f25_dilution_adjusted_growth_gppsg_252d_jerk_v013_signal,    f25dg_f25_dilution_adjusted_growth_bvpsg_252d_jerk_v014_signal,    f25dg_f25_dilution_adjusted_growth_netcreate_252d_jerk_v015_signal,    f25dg_f25_dilution_adjusted_growth_netcreate_126d_jerk_v016_signal,    f25dg_f25_dilution_adjusted_growth_fcfnetcreate_252d_jerk_v017_signal,    f25dg_f25_dilution_adjusted_growth_dilutiondrag_252d_jerk_v018_signal,    f25dg_f25_dilution_adjusted_growth_zspsg_63d_jerk_v019_signal,    f25dg_f25_dilution_adjusted_growth_zspsg_126d_jerk_v020_signal,    f25dg_f25_dilution_adjusted_growth_zfcfpsg_126d_jerk_v021_signal,    f25dg_f25_dilution_adjusted_growth_spsslope_126d_jerk_v022_signal,    f25dg_f25_dilution_adjusted_growth_spsslope_252d_jerk_v023_signal,    f25dg_f25_dilution_adjusted_growth_spsnslope_126d_jerk_v024_signal,    f25dg_f25_dilution_adjusted_growth_fcfnslope_252d_jerk_v025_signal,    f25dg_f25_dilution_adjusted_growth_logcompound_126d_jerk_v026_signal,    f25dg_f25_dilution_adjusted_growth_logcompound_252d_jerk_v027_signal,    f25dg_f25_dilution_adjusted_growth_fcflogcompound_252d_jerk_v028_signal,    f25dg_f25_dilution_adjusted_growth_psgrank_63d_jerk_v029_signal,    f25dg_f25_dilution_adjusted_growth_psgrank_126d_jerk_v030_signal,    f25dg_f25_dilution_adjusted_growth_pslevrank_252d_jerk_v031_signal,    f25dg_f25_dilution_adjusted_growth_spsg_84d_jerk_v032_signal,    f25dg_f25_dilution_adjusted_growth_spsg_189d_jerk_v033_signal,    f25dg_f25_dilution_adjusted_growth_spsg_315d_jerk_v034_signal,    f25dg_f25_dilution_adjusted_growth_spsg_378d_jerk_v035_signal,    f25dg_f25_dilution_adjusted_growth_spswag_252d_jerk_v036_signal,    f25dg_f25_dilution_adjusted_growth_gpwag_252d_jerk_v037_signal,    f25dg_f25_dilution_adjusted_growth_spsgsmooth_63d_jerk_v038_signal,    f25dg_f25_dilution_adjusted_growth_spsgsmooth_126d_jerk_v039_signal,    f25dg_f25_dilution_adjusted_growth_psgaccel_63_126_jerk_v040_signal,    f25dg_f25_dilution_adjusted_growth_psgaccel_126_252_jerk_v041_signal,    f25dg_f25_dilution_adjusted_growth_fcfgaccel_126_252_jerk_v042_signal,    f25dg_f25_dilution_adjusted_growth_revgpspread_252d_jerk_v043_signal,    f25dg_f25_dilution_adjusted_growth_fcfrevspread_252d_jerk_v044_signal,    f25dg_f25_dilution_adjusted_growth_pslevratio_252d_jerk_v045_signal,    f25dg_f25_dilution_adjusted_growth_fcflevratio_252d_jerk_v046_signal,    f25dg_f25_dilution_adjusted_growth_bvplevratio_252d_jerk_v047_signal,    f25dg_f25_dilution_adjusted_growth_bvplog_252d_jerk_v048_signal,    f25dg_f25_dilution_adjusted_growth_spsyield_0d_jerk_v049_signal,    f25dg_f25_dilution_adjusted_growth_fcfyield_0d_jerk_v050_signal,    f25dg_f25_dilution_adjusted_growth_bvpyield_0d_jerk_v051_signal,    f25dg_f25_dilution_adjusted_growth_zspsg126w_63d_jerk_v052_signal,    f25dg_f25_dilution_adjusted_growth_znetcreate_252d_jerk_v053_signal,    f25dg_f25_dilution_adjusted_growth_gpnetcreate_252d_jerk_v054_signal,    f25dg_f25_dilution_adjusted_growth_psgqual_126d_jerk_v055_signal,    f25dg_f25_dilution_adjusted_growth_fcfgqual_252d_jerk_v056_signal,    f25dg_f25_dilution_adjusted_growth_spsslopez_252d_jerk_v057_signal,    f25dg_f25_dilution_adjusted_growth_lognetcompound_252d_jerk_v058_signal,    f25dg_f25_dilution_adjusted_growth_bvpnetcreate_252d_jerk_v059_signal,    f25dg_f25_dilution_adjusted_growth_spsg_42d_jerk_v060_signal,    f25dg_f25_dilution_adjusted_growth_spsg_21d_jerk_v061_signal,    f25dg_f25_dilution_adjusted_growth_gppsg_63d_jerk_v062_signal,    f25dg_f25_dilution_adjusted_growth_fcfpsg_63d_jerk_v063_signal,    f25dg_f25_dilution_adjusted_growth_bvpsg_126d_jerk_v064_signal,    f25dg_f25_dilution_adjusted_growth_psewm_63d_jerk_v065_signal,    f25dg_f25_dilution_adjusted_growth_fcfewm_126d_jerk_v066_signal,    f25dg_f25_dilution_adjusted_growth_psgdisp_252d_jerk_v067_signal,    f25dg_f25_dilution_adjusted_growth_psgdisp_126d_jerk_v068_signal,    f25dg_f25_dilution_adjusted_growth_spsbvpspread_0d_jerk_v069_signal,    f25dg_f25_dilution_adjusted_growth_fcfconv_0d_jerk_v070_signal,    f25dg_f25_dilution_adjusted_growth_gpmargin_0d_jerk_v071_signal,    f25dg_f25_dilution_adjusted_growth_spsgann_63d_jerk_v072_signal,    f25dg_f25_dilution_adjusted_growth_spsgann_504d_jerk_v073_signal,    f25dg_f25_dilution_adjusted_growth_dualshare_252d_jerk_v074_signal,    f25dg_f25_dilution_adjusted_growth_psgblend_multi_jerk_v075_signal,    f25dg_f25_dilution_adjusted_growth_gppsg_504d_jerk_v076_signal,    f25dg_f25_dilution_adjusted_growth_fcfpsg_504d_jerk_v077_signal,    f25dg_f25_dilution_adjusted_growth_bvpsg_504d_jerk_v078_signal,    f25dg_f25_dilution_adjusted_growth_spswag_21d_jerk_v079_signal,    f25dg_f25_dilution_adjusted_growth_spswag_126d_jerk_v080_signal,    f25dg_f25_dilution_adjusted_growth_zspsg_252d_jerk_v081_signal,    f25dg_f25_dilution_adjusted_growth_zgppsg_126d_jerk_v082_signal,    f25dg_f25_dilution_adjusted_growth_zbvpsg_252d_jerk_v083_signal,    f25dg_f25_dilution_adjusted_growth_gpslope_252d_jerk_v084_signal,    f25dg_f25_dilution_adjusted_growth_bvpslope_252d_jerk_v085_signal,    f25dg_f25_dilution_adjusted_growth_gpnslope_126d_jerk_v086_signal,    f25dg_f25_dilution_adjusted_growth_bvpnslope_252d_jerk_v087_signal,    f25dg_f25_dilution_adjusted_growth_gplogcompound_252d_jerk_v088_signal,    f25dg_f25_dilution_adjusted_growth_bvplogcompound_126d_jerk_v089_signal,    f25dg_f25_dilution_adjusted_growth_fcfgrank_126d_jerk_v090_signal,    f25dg_f25_dilution_adjusted_growth_gpgrank_252d_jerk_v091_signal,    f25dg_f25_dilution_adjusted_growth_fcflevrank_252d_jerk_v092_signal,    f25dg_f25_dilution_adjusted_growth_netcreate_504d_jerk_v093_signal,    f25dg_f25_dilution_adjusted_growth_netcreate_63d_jerk_v094_signal,    f25dg_f25_dilution_adjusted_growth_fcfnetcreate_126d_jerk_v095_signal,    f25dg_f25_dilution_adjusted_growth_gpnetcreate_126d_jerk_v096_signal,    f25dg_f25_dilution_adjusted_growth_fcfdilutiondrag_252d_jerk_v097_signal,    f25dg_f25_dilution_adjusted_growth_gpdilutiondrag_252d_jerk_v098_signal,    f25dg_f25_dilution_adjusted_growth_gpgsmooth_126d_jerk_v099_signal,    f25dg_f25_dilution_adjusted_growth_fcfgsmooth_126d_jerk_v100_signal,    f25dg_f25_dilution_adjusted_growth_gpgaccel_63_126_jerk_v101_signal,    f25dg_f25_dilution_adjusted_growth_bvpgaccel_126_252_jerk_v102_signal,    f25dg_f25_dilution_adjusted_growth_psgaccel_21_63_jerk_v103_signal,    f25dg_f25_dilution_adjusted_growth_revbvpspread_252d_jerk_v104_signal,    f25dg_f25_dilution_adjusted_growth_gpfcfspread_252d_jerk_v105_signal,    f25dg_f25_dilution_adjusted_growth_gplevratio_252d_jerk_v106_signal,    f25dg_f25_dilution_adjusted_growth_pslevratio_126d_jerk_v107_signal,    f25dg_f25_dilution_adjusted_growth_gpyield_0d_jerk_v108_signal,    f25dg_f25_dilution_adjusted_growth_psgpricespread_252d_jerk_v109_signal,    f25dg_f25_dilution_adjusted_growth_psgqual_63d_jerk_v110_signal,    f25dg_f25_dilution_adjusted_growth_gpgqual_126d_jerk_v111_signal,    f25dg_f25_dilution_adjusted_growth_bvpgqual_252d_jerk_v112_signal,    f25dg_f25_dilution_adjusted_growth_gpslopez_252d_jerk_v113_signal,    f25dg_f25_dilution_adjusted_growth_fcfslopez_252d_jerk_v114_signal,    f25dg_f25_dilution_adjusted_growth_gplognetcompound_252d_jerk_v115_signal,    f25dg_f25_dilution_adjusted_growth_fcflognetcompound_252d_jerk_v116_signal,    f25dg_f25_dilution_adjusted_growth_gppsg_84d_jerk_v117_signal,    f25dg_f25_dilution_adjusted_growth_fcfpsg_189d_jerk_v118_signal,    f25dg_f25_dilution_adjusted_growth_spswag_504d_jerk_v119_signal,    f25dg_f25_dilution_adjusted_growth_bvpsg_189d_jerk_v120_signal,    f25dg_f25_dilution_adjusted_growth_spsgann_126d_jerk_v121_signal,    f25dg_f25_dilution_adjusted_growth_gpgann_252d_jerk_v122_signal,    f25dg_f25_dilution_adjusted_growth_fcfgann_252d_jerk_v123_signal,    f25dg_f25_dilution_adjusted_growth_psgdisp_504d_jerk_v124_signal,    f25dg_f25_dilution_adjusted_growth_fcfgdisp_252d_jerk_v125_signal,    f25dg_f25_dilution_adjusted_growth_psewm_126d_jerk_v126_signal,    f25dg_f25_dilution_adjusted_growth_gpewm_63d_jerk_v127_signal,    f25dg_f25_dilution_adjusted_growth_bvpewm_252d_jerk_v128_signal,    f25dg_f25_dilution_adjusted_growth_fcfconvchg_252d_jerk_v129_signal,    f25dg_f25_dilution_adjusted_growth_gpmarginchg_252d_jerk_v130_signal,    f25dg_f25_dilution_adjusted_growth_spsbvpchg_252d_jerk_v131_signal,    f25dg_f25_dilution_adjusted_growth_zfcflev_252d_jerk_v132_signal,    f25dg_f25_dilution_adjusted_growth_zpslev_504d_jerk_v133_signal,    f25dg_f25_dilution_adjusted_growth_zbvplev_252d_jerk_v134_signal,    f25dg_f25_dilution_adjusted_growth_zgpnetcreate_252d_jerk_v135_signal,    f25dg_f25_dilution_adjusted_growth_zfcfnetcreate_252d_jerk_v136_signal,    f25dg_f25_dilution_adjusted_growth_gpdualshare_252d_jerk_v137_signal,    f25dg_f25_dilution_adjusted_growth_wadilution_126d_jerk_v138_signal,    f25dg_f25_dilution_adjusted_growth_spsgsmooth_252d_jerk_v139_signal,    f25dg_f25_dilution_adjusted_growth_fcfgrank_252d_jerk_v140_signal,    f25dg_f25_dilution_adjusted_growth_bvpgrank_252d_jerk_v141_signal,    f25dg_f25_dilution_adjusted_growth_psgsurp_252d_jerk_v142_signal,    f25dg_f25_dilution_adjusted_growth_fcfgsurp_126d_jerk_v143_signal,    f25dg_f25_dilution_adjusted_growth_psgratio_63_252_jerk_v144_signal,    f25dg_f25_dilution_adjusted_growth_gpgratio_126_252_jerk_v145_signal,    f25dg_f25_dilution_adjusted_growth_pssmoothslope_252d_jerk_v146_signal,    f25dg_f25_dilution_adjusted_growth_valuecomposite_252d_jerk_v147_signal,    f25dg_f25_dilution_adjusted_growth_fcfgblend_multi_jerk_v148_signal,    f25dg_f25_dilution_adjusted_growth_bvpgblend_multi_jerk_v149_signal,    f25dg_f25_dilution_adjusted_growth_netcreatez_504d_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_DILUTION_ADJUSTED_GROWTH_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f25_ps', '_f25_psgrowth', '_f25_fcfps', '_f25_bvps')
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
    print("OK f25_dilution_adjusted_growth_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
