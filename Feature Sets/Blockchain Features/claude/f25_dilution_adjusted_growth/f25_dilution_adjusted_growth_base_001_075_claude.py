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


# ============ FEATURES 001-075 ============

# revenue per share level (sales per share, sharesbas)
def f25dg_f25_dilution_adjusted_growth_sps_level_0d_base_v001_signal(revenue, sharesbas):
    result = _f25_ps(revenue, sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level using weighted shares
def f25dg_f25_dilution_adjusted_growth_spswa_level_0d_base_v002_signal(revenue, shareswa):
    result = _f25_ps(revenue, shareswa)
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow per share level
def f25dg_f25_dilution_adjusted_growth_fcfps_level_0d_base_v003_signal(fcf, sharesbas):
    result = _f25_fcfps(fcf, sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit per share level
def f25dg_f25_dilution_adjusted_growth_gpps_level_0d_base_v004_signal(gp, sharesbas):
    result = _f25_ps(gp, sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# book value (equity) per share level
def f25dg_f25_dilution_adjusted_growth_bvps_level_0d_base_v005_signal(equity, sharesbas):
    result = _f25_bvps(equity, sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 63d
def f25dg_f25_dilution_adjusted_growth_spsg_63d_base_v006_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 126d
def f25dg_f25_dilution_adjusted_growth_spsg_126d_base_v007_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 252d
def f25dg_f25_dilution_adjusted_growth_spsg_252d_base_v008_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 504d
def f25dg_f25_dilution_adjusted_growth_spsg_504d_base_v009_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth over 126d
def f25dg_f25_dilution_adjusted_growth_fcfpsg_126d_base_v010_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth over 252d
def f25dg_f25_dilution_adjusted_growth_fcfpsg_252d_base_v011_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth over 126d
def f25dg_f25_dilution_adjusted_growth_gppsg_126d_base_v012_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth over 252d
def f25dg_f25_dilution_adjusted_growth_gppsg_252d_base_v013_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# book value/share growth over 252d
def f25dg_f25_dilution_adjusted_growth_bvpsg_252d_base_v014_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation: rev/share growth minus share-count growth (252d)
def f25dg_f25_dilution_adjusted_growth_netcreate_252d_base_v015_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation: rev/share growth minus share-count growth (126d)
def f25dg_f25_dilution_adjusted_growth_netcreate_126d_base_v016_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation: fcf/share growth minus share-count growth (252d)
def f25dg_f25_dilution_adjusted_growth_fcfnetcreate_252d_base_v017_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag: raw revenue growth minus per-share revenue growth (252d)
def f25dg_f25_dilution_adjusted_growth_dilutiondrag_252d_base_v018_signal(revenue, sharesbas):
    rawg = revenue.pct_change(periods=252)
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    result = rawg - psg
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of revenue/share growth (63d) over 252d
def f25dg_f25_dilution_adjusted_growth_zspsg_63d_base_v019_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of revenue/share growth (126d) over 504d
def f25dg_f25_dilution_adjusted_growth_zspsg_126d_base_v020_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of fcf/share growth (126d) over 252d
def f25dg_f25_dilution_adjusted_growth_zfcfpsg_126d_base_v021_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _z(ps.pct_change(periods=126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share trend slope over 126d
def f25dg_f25_dilution_adjusted_growth_spsslope_126d_base_v022_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _slope(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share trend slope over 252d
def f25dg_f25_dilution_adjusted_growth_spsslope_252d_base_v023_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _slope(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized sales-per-share slope (slope / level) over 126d
def f25dg_f25_dilution_adjusted_growth_spsnslope_126d_base_v024_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(_slope(ps, 126), _mean(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# normalized fcf-per-share slope over 252d
def f25dg_f25_dilution_adjusted_growth_fcfnslope_252d_base_v025_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(_slope(ps, 252), _mean(ps.abs(), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted compounding: log per-share growth annualized (126d)
def f25dg_f25_dilution_adjusted_growth_logcompound_126d_base_v026_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted compounding: log per-share growth annualized (252d)
def f25dg_f25_dilution_adjusted_growth_logcompound_252d_base_v027_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted compounding of fcf/share (252d log)
def f25dg_f25_dilution_adjusted_growth_fcflogcompound_252d_base_v028_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = np.log(_safe_div(ps.abs() + 1.0, ps.shift(252).abs() + 1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth percentile rank (63d growth over 252d window)
def f25dg_f25_dilution_adjusted_growth_psgrank_63d_base_v029_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth percentile rank (126d growth over 504d window)
def f25dg_f25_dilution_adjusted_growth_psgrank_126d_base_v030_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share level percentile rank over 252d
def f25dg_f25_dilution_adjusted_growth_pslevrank_252d_base_v031_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = ps.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 84d
def f25dg_f25_dilution_adjusted_growth_spsg_84d_base_v032_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 189d
def f25dg_f25_dilution_adjusted_growth_spsg_189d_base_v033_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 315d
def f25dg_f25_dilution_adjusted_growth_spsg_315d_base_v034_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 378d
def f25dg_f25_dilution_adjusted_growth_spsg_378d_base_v035_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth using weighted shares (252d)
def f25dg_f25_dilution_adjusted_growth_spswag_252d_base_v036_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth using weighted shares (252d)
def f25dg_f25_dilution_adjusted_growth_gpwag_252d_base_v037_signal(gp, shareswa):
    ps = _f25_ps(gp, shareswa)
    result = ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth smoothed (21d mean of 63d growth)
def f25dg_f25_dilution_adjusted_growth_spsgsmooth_63d_base_v038_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth smoothed (42d mean of 126d growth)
def f25dg_f25_dilution_adjusted_growth_spsgsmooth_126d_base_v039_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of per-share growth: 63d growth minus 126d growth
def f25dg_f25_dilution_adjusted_growth_psgaccel_63_126_base_v040_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 63) - _f25_psgrowth(revenue, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of per-share growth: 126d growth minus 252d growth
def f25dg_f25_dilution_adjusted_growth_psgaccel_126_252_base_v041_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 126) - _f25_psgrowth(revenue, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per-share growth acceleration 126 vs 252
def f25dg_f25_dilution_adjusted_growth_fcfgaccel_126_252_base_v042_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=126) - ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth spread: revenue vs gross-profit per-share growth (252d)
def f25dg_f25_dilution_adjusted_growth_revgpspread_252d_base_v043_signal(revenue, gp, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    result = gg - rg
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth spread: fcf vs revenue per-share growth (252d)
def f25dg_f25_dilution_adjusted_growth_fcfrevspread_252d_base_v044_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    result = fg - rg
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of per-share level to its 252d mean (level vs trend)
def f25dg_f25_dilution_adjusted_growth_pslevratio_252d_base_v045_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of fcf-per-share level to its 252d mean
def f25dg_f25_dilution_adjusted_growth_fcflevratio_252d_base_v046_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# book-value-per-share ratio to its 252d mean
def f25dg_f25_dilution_adjusted_growth_bvplevratio_252d_base_v047_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# log book-value-per-share growth (252d)
def f25dg_f25_dilution_adjusted_growth_bvplog_252d_base_v048_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share scaled by price (sales yield per share) using closeadj
def f25dg_f25_dilution_adjusted_growth_spsyield_0d_base_v049_signal(revenue, sharesbas, closeadj):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share scaled by price (fcf yield per share)
def f25dg_f25_dilution_adjusted_growth_fcfyield_0d_base_v050_signal(fcf, sharesbas, closeadj):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(ps, closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share scaled by price (book yield, inverse P/B per share)
def f25dg_f25_dilution_adjusted_growth_bvpyield_0d_base_v051_signal(equity, sharesbas, closeadj):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(ps, closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth z over 126d (short window standardization)
def f25dg_f25_dilution_adjusted_growth_zspsg126w_63d_base_v052_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation z-score over 252d (504d growth window net of dilution)
def f25dg_f25_dilution_adjusted_growth_znetcreate_252d_base_v053_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count-adjusted gp growth net of dilution (252d)
def f25dg_f25_dilution_adjusted_growth_gpnetcreate_252d_base_v054_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share momentum quality: growth / dispersion of growth (126d)
def f25dg_f25_dilution_adjusted_growth_psgqual_126d_base_v055_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share momentum quality (252d growth / dispersion)
def f25dg_f25_dilution_adjusted_growth_fcfgqual_252d_base_v056_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=252)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# per-share level trend slope normalized by its dispersion (252d)
def f25dg_f25_dilution_adjusted_growth_spsslopez_252d_base_v057_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted compounding net of share growth (log, 252d)
def f25dg_f25_dilution_adjusted_growth_lognetcompound_252d_base_v058_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    revlog = np.log(_safe_div(revenue, revenue.shift(252)))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = revlog - shlog + ps * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity-per-share growth net of dilution (252d)
def f25dg_f25_dilution_adjusted_growth_bvpnetcreate_252d_base_v059_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 42d (short horizon)
def f25dg_f25_dilution_adjusted_growth_spsg_42d_base_v060_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 21d (monthly)
def f25dg_f25_dilution_adjusted_growth_spsg_21d_base_v061_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth over 63d
def f25dg_f25_dilution_adjusted_growth_gppsg_63d_base_v062_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth over 63d
def f25dg_f25_dilution_adjusted_growth_fcfpsg_63d_base_v063_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# book value/share growth over 126d
def f25dg_f25_dilution_adjusted_growth_bvpsg_126d_base_v064_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share EWMA-smoothed growth (span 63 on daily-equiv per-share log return)
def f25dg_f25_dilution_adjusted_growth_psewm_63d_base_v065_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share EWMA-smoothed growth (span 126)
def f25dg_f25_dilution_adjusted_growth_fcfewm_126d_base_v066_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    lr = np.log(_safe_div(ps.abs() + 1.0, ps.shift(1).abs() + 1.0))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth dispersion (volatility of 63d growth over 252d)
def f25dg_f25_dilution_adjusted_growth_psgdisp_252d_base_v067_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = _std(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth dispersion (volatility of 21d growth over 126d)
def f25dg_f25_dilution_adjusted_growth_psgdisp_126d_base_v068_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 21)
    result = _std(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share vs book value per share spread (operating leverage proxy)
def f25dg_f25_dilution_adjusted_growth_spsbvpspread_0d_base_v069_signal(revenue, equity, sharesbas):
    sps = _f25_ps(revenue, sharesbas)
    bvps = _f25_bvps(equity, sharesbas)
    result = _safe_div(sps, bvps)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share vs revenue per share conversion ratio
def f25dg_f25_dilution_adjusted_growth_fcfconv_0d_base_v070_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    result = _safe_div(fps, sps)
    return result.replace([np.inf, -np.inf], np.nan)


# gp per share vs revenue per share (gross margin per share proxy)
def f25dg_f25_dilution_adjusted_growth_gpmargin_0d_base_v071_signal(gp, revenue, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    result = _safe_div(gpps, sps)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth annualized from 63d
def f25dg_f25_dilution_adjusted_growth_spsgann_63d_base_v072_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(63))) * (252.0 / 63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth annualized from 504d
def f25dg_f25_dilution_adjusted_growth_spsgann_504d_base_v073_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(504))) * (252.0 / 504.0)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth minus weighted-share dilution (uses both share counts, 252d)
def f25dg_f25_dilution_adjusted_growth_dualshare_252d_base_v074_signal(revenue, sharesbas, shareswa):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    wadil = shareswa.pct_change(periods=252)
    result = psg - wadil
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon per-share growth composite (63/126/252)
def f25dg_f25_dilution_adjusted_growth_psgblend_multi_base_v075_signal(revenue, sharesbas):
    result = (_f25_psgrowth(revenue, sharesbas, 63)
              + _f25_psgrowth(revenue, sharesbas, 126)
              + _f25_psgrowth(revenue, sharesbas, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25dg_f25_dilution_adjusted_growth_sps_level_0d_base_v001_signal,
    f25dg_f25_dilution_adjusted_growth_spswa_level_0d_base_v002_signal,
    f25dg_f25_dilution_adjusted_growth_fcfps_level_0d_base_v003_signal,
    f25dg_f25_dilution_adjusted_growth_gpps_level_0d_base_v004_signal,
    f25dg_f25_dilution_adjusted_growth_bvps_level_0d_base_v005_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_63d_base_v006_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_126d_base_v007_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_252d_base_v008_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_504d_base_v009_signal,
    f25dg_f25_dilution_adjusted_growth_fcfpsg_126d_base_v010_signal,
    f25dg_f25_dilution_adjusted_growth_fcfpsg_252d_base_v011_signal,
    f25dg_f25_dilution_adjusted_growth_gppsg_126d_base_v012_signal,
    f25dg_f25_dilution_adjusted_growth_gppsg_252d_base_v013_signal,
    f25dg_f25_dilution_adjusted_growth_bvpsg_252d_base_v014_signal,
    f25dg_f25_dilution_adjusted_growth_netcreate_252d_base_v015_signal,
    f25dg_f25_dilution_adjusted_growth_netcreate_126d_base_v016_signal,
    f25dg_f25_dilution_adjusted_growth_fcfnetcreate_252d_base_v017_signal,
    f25dg_f25_dilution_adjusted_growth_dilutiondrag_252d_base_v018_signal,
    f25dg_f25_dilution_adjusted_growth_zspsg_63d_base_v019_signal,
    f25dg_f25_dilution_adjusted_growth_zspsg_126d_base_v020_signal,
    f25dg_f25_dilution_adjusted_growth_zfcfpsg_126d_base_v021_signal,
    f25dg_f25_dilution_adjusted_growth_spsslope_126d_base_v022_signal,
    f25dg_f25_dilution_adjusted_growth_spsslope_252d_base_v023_signal,
    f25dg_f25_dilution_adjusted_growth_spsnslope_126d_base_v024_signal,
    f25dg_f25_dilution_adjusted_growth_fcfnslope_252d_base_v025_signal,
    f25dg_f25_dilution_adjusted_growth_logcompound_126d_base_v026_signal,
    f25dg_f25_dilution_adjusted_growth_logcompound_252d_base_v027_signal,
    f25dg_f25_dilution_adjusted_growth_fcflogcompound_252d_base_v028_signal,
    f25dg_f25_dilution_adjusted_growth_psgrank_63d_base_v029_signal,
    f25dg_f25_dilution_adjusted_growth_psgrank_126d_base_v030_signal,
    f25dg_f25_dilution_adjusted_growth_pslevrank_252d_base_v031_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_84d_base_v032_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_189d_base_v033_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_315d_base_v034_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_378d_base_v035_signal,
    f25dg_f25_dilution_adjusted_growth_spswag_252d_base_v036_signal,
    f25dg_f25_dilution_adjusted_growth_gpwag_252d_base_v037_signal,
    f25dg_f25_dilution_adjusted_growth_spsgsmooth_63d_base_v038_signal,
    f25dg_f25_dilution_adjusted_growth_spsgsmooth_126d_base_v039_signal,
    f25dg_f25_dilution_adjusted_growth_psgaccel_63_126_base_v040_signal,
    f25dg_f25_dilution_adjusted_growth_psgaccel_126_252_base_v041_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgaccel_126_252_base_v042_signal,
    f25dg_f25_dilution_adjusted_growth_revgpspread_252d_base_v043_signal,
    f25dg_f25_dilution_adjusted_growth_fcfrevspread_252d_base_v044_signal,
    f25dg_f25_dilution_adjusted_growth_pslevratio_252d_base_v045_signal,
    f25dg_f25_dilution_adjusted_growth_fcflevratio_252d_base_v046_signal,
    f25dg_f25_dilution_adjusted_growth_bvplevratio_252d_base_v047_signal,
    f25dg_f25_dilution_adjusted_growth_bvplog_252d_base_v048_signal,
    f25dg_f25_dilution_adjusted_growth_spsyield_0d_base_v049_signal,
    f25dg_f25_dilution_adjusted_growth_fcfyield_0d_base_v050_signal,
    f25dg_f25_dilution_adjusted_growth_bvpyield_0d_base_v051_signal,
    f25dg_f25_dilution_adjusted_growth_zspsg126w_63d_base_v052_signal,
    f25dg_f25_dilution_adjusted_growth_znetcreate_252d_base_v053_signal,
    f25dg_f25_dilution_adjusted_growth_gpnetcreate_252d_base_v054_signal,
    f25dg_f25_dilution_adjusted_growth_psgqual_126d_base_v055_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgqual_252d_base_v056_signal,
    f25dg_f25_dilution_adjusted_growth_spsslopez_252d_base_v057_signal,
    f25dg_f25_dilution_adjusted_growth_lognetcompound_252d_base_v058_signal,
    f25dg_f25_dilution_adjusted_growth_bvpnetcreate_252d_base_v059_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_42d_base_v060_signal,
    f25dg_f25_dilution_adjusted_growth_spsg_21d_base_v061_signal,
    f25dg_f25_dilution_adjusted_growth_gppsg_63d_base_v062_signal,
    f25dg_f25_dilution_adjusted_growth_fcfpsg_63d_base_v063_signal,
    f25dg_f25_dilution_adjusted_growth_bvpsg_126d_base_v064_signal,
    f25dg_f25_dilution_adjusted_growth_psewm_63d_base_v065_signal,
    f25dg_f25_dilution_adjusted_growth_fcfewm_126d_base_v066_signal,
    f25dg_f25_dilution_adjusted_growth_psgdisp_252d_base_v067_signal,
    f25dg_f25_dilution_adjusted_growth_psgdisp_126d_base_v068_signal,
    f25dg_f25_dilution_adjusted_growth_spsbvpspread_0d_base_v069_signal,
    f25dg_f25_dilution_adjusted_growth_fcfconv_0d_base_v070_signal,
    f25dg_f25_dilution_adjusted_growth_gpmargin_0d_base_v071_signal,
    f25dg_f25_dilution_adjusted_growth_spsgann_63d_base_v072_signal,
    f25dg_f25_dilution_adjusted_growth_spsgann_504d_base_v073_signal,
    f25dg_f25_dilution_adjusted_growth_dualshare_252d_base_v074_signal,
    f25dg_f25_dilution_adjusted_growth_psgblend_multi_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_DILUTION_ADJUSTED_GROWTH_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume", "marketcap",
           "ev", "assets", "assetsc", "equity", "revenue", "gp", "ebitda", "ppnenet",
           "sharesbas", "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "intangibles", "evebitda", "evebit", "pe", "pb", "ps",
           "currentratio", "bvps", "sps", "shrvalue", "shrunits", "totalvalue",
           "percentoftotal", "sf3a_shares", "sf3a_value", "sf3b_shares", "sf3b_value",
           "grossmargin", "beta1y", "beta5y", "invcap", "debt", "fcf"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + np.abs(np.random.normal(0, 0.02, n))), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - np.abs(np.random.normal(0, 0.02, n))), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f25_ps", "_f25_psgrowth", "_f25_fcfps", "_f25_bvps")
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
    print(f"OK f25_dilution_adjusted_growth_base_001_075_claude: {n_features} features pass")
